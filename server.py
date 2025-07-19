from flask import Flask, request, jsonify
from flask_cors import CORS
import asyncio, json
from bs4 import BeautifulSoup
from loguru import logger
import requests
from mcp_crawler import AsyncWebCrawler

app = Flask("gremlin_scraper")
CORS(app)

logger.add("gremlin_scraper.log", rotation="1 MB")  # log file w/ rotation

@app.route("/scrape", methods=["POST"])
def scrape():
    data = request.json or {}
    url = data.get("url")
    if not url:
        logger.warning("Scrape attempt with missing URL.")
        return jsonify({"error": "Missing 'url'"}), 400

    logger.info(f"Scraping URL: {url}")
    try:
        headers = {
            "User-Agent": "GremlinScraper/1.0 (+https://github.com/statikfintechllc)"
        }
        resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()

        if "text/html" not in resp.headers.get("Content-Type", ""):
            logger.warning("Non-HTML content detected.")
            return jsonify({"error": "Non-HTML content returned"}), 415

        soup = BeautifulSoup(resp.text, "html.parser")
        text = soup.get_text(separator="\n")
        trimmed_text = text.strip()[:5000]  # safety cap

        logger.success(f"Scraping completed — {len(trimmed_text)} characters extracted.")
        return jsonify({"text": trimmed_text})

    except requests.exceptions.Timeout:
        logger.error("Request timed out.")
        return jsonify({"error": "Request timed out"}), 504
    except requests.exceptions.RequestException as req_err:
        logger.error(f"Request failed: {req_err}")
        return jsonify({"error": f"Request failed: {str(req_err)}"}), 502
    except Exception as e:
        logger.exception("Unhandled exception during scrape")
        return jsonify({"error": str(e)}), 500


@app.route("/crawl", methods=["POST"])
def crawl():
    cfg = request.json or {}
    start = cfg.get("url")
    if not start:
        return jsonify({"error": "Missing 'url'"}), 400

    crawler = AsyncWebCrawler(
        max_pages=int(cfg.get("max_pages", 50)),
        max_depth=int(cfg.get("max_depth", 2)),
        concurrency=int(cfg.get("concurrency", 5))
    )

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        results = loop.run_until_complete(crawler.crawl(start))
        return jsonify(results)
    finally:
        loop.close()


@app.route("/crawl-stream", methods=["POST"])
def crawl_stream():
    cfg = request.json or {}
    start = cfg.get("url")
    if not start:
        return jsonify({"error": "Missing 'url'"}), 400

    crawler = AsyncWebCrawler(
        max_pages=int(cfg.get("max_pages", 50)),
        max_depth=int(cfg.get("max_depth", 2)),
        concurrency=int(cfg.get("concurrency", 5))
    )

    async def gen():
        pages = await crawler.crawl(start)
        for url, text in pages.items():
            yield json.dumps({"url": url, "text": text}) + "\n"

    return app.response_class(gen(), mimetype="application/json")


@app.route("/mcp/metadata", methods=["GET"])
def metadata():
    return jsonify({
        "name": "Gremlin Web Scraper",
        "description": "Scrapes and crawls text from URLs.",
        "version": "0.0.1",
        "author": "StatikFintech LLC",
        "tags": ["scraping", "crawl", "MCP", "runtime"],
        "endpoints": [
            {"path": "/scrape",       "method": "POST", "description": "Single-page text scrape"},
            {"path": "/crawl",        "method": "POST", "description": "Multi-page crawl up to max_pages/depth"},
            {"path": "/crawl-stream", "method": "POST", "description": "Streaming multi-page crawl"},
            {"path": "/ping",         "method": "GET",  "description": "Health check"},
            {"path": "/mcp/metadata", "method": "GET",  "description": "Service metadata"}
        ]
    })


@app.route("/ping", methods=["GET"])
def ping():
    return "pong", 200


if __name__ == "__main__":
    logger.info("🚀 Gremlin Scraper MCP starting on port 8742")
    app.run(host="0.0.0.0", port=8742)
