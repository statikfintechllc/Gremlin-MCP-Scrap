# Gremlin Web Scraper MCP

GremlinScraper is a lightweight HTTP MCP module designed to scrape visible text from any publicly accessible webpage. It runs locally, integrates directly with VS Code’s MCP system, and speaks plain JSON. 

> This is Part 1 of the **GremlinOS Runtime Suite** from **StatikFinTech LLC**.

---

## 🧠 Features

- **MCP-Compatible:** Shows up in VS Code’s MCP list with metadata.
- **Simple API:** POST a URL, receive clean text in return.
- **CORS-Ready:** Built-in CORS support for cross-origin requests.
- **Logging:** Uses `loguru` to log all activity to rotating files.
- **Timeouts + Error Handling:** Gracefully deals with slow or weird sites.
- **Human UA Header:** Doesn’t look like a bot (unless you read the name).

---

## 🔧 Usage

1. Clone or drop this repo into your `.vscode/mcps/` or wherever your MCPs live.
2. Add `"gremlinScraper"` to `.mcp.json`.
3. Click “Start Server” in the VS Code MCP tab.
4. Or run it manually:
   ```bash
   pip install -r requirements.txt
   python server.py
   ```

---

## 📦 Endpoints & Examples

**1. POST /scrape**

- Fetch a single page’s visible text:

  ```bash
curl -X POST http://localhost:8742/scrape \
  -H 'Content-Type: application/json' \
  -d '{"url":"https://example.com"}'
  ```

- Response:

```json
{
  "text": "Example Domain\n\nThis domain is for use in illustrative examples in documents.\n..."
}
```

**2. POST /crawl**

- Recursively crawl same-domain links:

```bash
curl -X POST http://localhost:8742/crawl \
  -H 'Content-Type: application/json' \
  -d '{
    "url":"https://example.com",
    "max_pages":10,
    "max_depth":2,
    "concurrency":5
  }'
```

- Response: 

```json
{
  "https://example.com": "Example Domain\n\nThis domain is for use…",
  "https://example.com/about": "About Us\n\n…",
  "...": "…"
}
```

**3. POST /crawl-stream**

- Stream each page as soon as it’s fetched:

```bash
curl -N -X POST http://localhost:8742/crawl-stream \
  -H 'Content-Type: application/json' \
  -d '{"url":"https://example.com","max_pages":5}'
```

- Response (NDJSON):

```json
{"url":"https://example.com","text":"Example Domain\n…"}
{"url":"https://example.com/link1","text":"Link One\n…"}
…
```

**4. GET /ping**

- Health check endpoint:

`curl http://localhost:8742/ping`

- Response:

`pong`

**5. GET /mcp/metadata**

- MCP discovery metadata:

`curl http://localhost:8742/mcp/metadata`

- Response:

```json
{
  "name":"Gremlin Web Scraper MCP",
  "description":"Scrapes and crawls text from URLs via HTTP endpoints…",
  "version":"0.0.1",
  "author":"StatikFinTech LLC",
  "tags":["scraping","crawl","MCP","runtime"],
  "endpoints":[…]
}
```



---

## 🗂 Metadata

> Name: Gremlin Web Scraper MCP  
> Author: StatikFinTech LLC  
> License: MIT  
> Tags: #scraping, #crawl, #runtime, #gremlin

---

## 🐾 Future Add-ons

- PDF / EPUB / Markdown parsing
- Selective DOM element filtering
- Scheduling/recurring crawl and scrap jobs
- Direct Memory injection to GremlinGPT core

---

“Split. Streamlined. Sovereign.”
StatikFinTech Systems • 2025
