from flask import Flask, request, jsonify
from flask_cors import CORS
from bs4 import BeautifulSoup
from loguru import logger
import requests

app = Flask("gremlin_scraper")
CORS(app)

logger.add("gremlin_scraper.log", rotation="1 MB")  # log file w/ rotation

@app.route("/scrape", methods=["POST"])
def scrape():
    data = request.json
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

@app.route("/mcp/metadata", methods=["GET"])
def metadata():
    return jsonify({
        "name": "Gremlin Web Scraper",
        "description": "Scrapes readable text from a URL.",
        "version": "0.0.1",
        "author": "StatikFintech LLC",
        "tags": ["scraping", "text", "MCP", "runtime"]
    })

@app.route("/ping", methods=["GET"])
def ping():
    return "pong", 200

if __name__ == "__main__":
    logger.info("🚀 Gremlin Scraper MCP starting on port 8742")
    app.run(host="0.0.0.0", port=8742)
