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

## 📦 Endpoints

- POST /scrape

  ```bash
  {
    "url": "https://example.com"
  }
  ```

- Returns:

  ```bash
  {
    "url": "https://example.com"
  }
  ```

- GET /mcp/metadata

`Returns MCP metadata so VS Code knows what this thing is.`

---

## 🗂 Metadata

> Name: Gremlin Web Scraper MCP  
> Author: StatikFinTech LLC  
> License: MIT  
> Tags: #scraping, #text, #runtime, #gremlin

---

## 🐾 Future Add-ons

- PDF / EPUB / Markdown parsing
- DOM element filtering
- Scraping scheduling
- Memory injection to GremlinGPT core

---

“Split. Streamlined. Sovereign.”
StatikFinTech Systems • 2025
