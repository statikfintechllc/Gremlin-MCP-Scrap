from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask("gremlin_scraper")

@app.route("/scrape", methods=["POST"])
def scrape():
    data = request.json
    url = data.get("url")
    if not url:
        return jsonify({"error": "Missing 'url'"}), 400
    try:
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, "html.parser")
        text = soup.get_text(separator="\n")
        return jsonify({"text": text.strip()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/mcp/metadata", methods=["GET"])
def metadata():
    return jsonify({
        "name": "Gremlin Web Scraper",
        "description": "Scrapes readable text from a URL.",
        "version": "0.0.1"
    })

if __name__ == "__main__":
    app.run(port=8742)
