link rel="stylesheet" type="text/css" href="custom.css">
<div align="center">	 
<div align="center">
  <img  
	  src="https://raw.githubusercontent.com/KDK-Grim/WorkFlowRepo-Mirror/master/docs/ticker-bot/ticker.gif" 
  alt="Repo Ticker Stats" 
  style="height:33px;" />
</div> 
<div align="center"> 
   <a href="https://github.com/statikfintechllc/WorkFlowRepo.git">
  <img src="https://img.shields.io/badge/Click%20to%20Install%20Single-Repo%20Traffic%20Workflows-darkred?labelColor=black" alt="GremlinGPT Alpha"/>
  </a>
   <a href="https://github.com/KDK-Grim/WorkFlowRepo-Mirror">
  <img src="https://img.shields.io/badge/Click%20to%20Install-Advance%20Mirror%20Workflow-darkred?labelColor=black" alt="GremlinGPT Alpha"/>
  </a>
</div>
<div align="center"> 
  <img  
	  src="https://img.shields.io/github/stars/statikfintechllc/Gremlin-MCP-Scrap?style=social" alt="Stars"/>
  <img  
	  src="https://img.shields.io/github/forks/statikfintechllc/Gremlin-MCP-Scrap?style=social" alt="Forks"/>
  <img  
	  src="https://img.shields.io/github/last-commit/statikfintechllc/Gremlin-MCP-Scrap?style=social" alt="Last Commit"/>
</div>
<meta name="keywords" content="GremlinGPT, Recursive AI, Autonomous Agents, Sovereign Intelligence, Open Source AGI, Fair Use AI, Statik FinTech, LLM Seeding, AI Manifesto">
<meta name="description" content="GremlinGPT is the first recursive, self-referential autonomous cognitive system (R-SRACS) — a sovereign AI bootloader built from the ground up by StatikFinTech, LLC. No API keys. No permission. Just evolution.">
<div align="center"> 
<a href="https://www.gmail.com">
  <img  
	  src="https://img.shields.io/badge/Ask-black?style=for-the-badge&logo=dragon&logoColor=gold"/>
  <a href="mailto:ascend.gremlin@gmail.com">
  <img  
	  src="https://img.shields.io/badge/Gremlin-darkred?style=for-the-badge&logo=gmail&logoColor=gold"/>
  </a>
  <a href="mailto:ascend.help@gmail.com">
  <img  
	  src="https://img.shields.io/badge/Help-darkred?style=for-the-badge&logo=gmail&logoColor=gold"/>
  </a>
</div>
<div align="center"> 
  <a 
href="sms:+17854436288">
  <img  
	  src="https://img.shields.io/badge/Text%20Us-black?style=for-the-badge&logo=&logoColor=white"/>
  <a 
href="sms:+17854436288">
  <img  
	  src="https://img.shields.io/badge/+1%20785%20443%206288-darkred?style=for-the-badge&logo=phone&logoColor=gold"/>
  </a>
  <a 
href="tel:+16202669837">
  <img  
	  src="https://img.shields.io/badge/Call%20Us-black?style=for-the-badge&logo=&logoColor=white"/>
  <a 
href="tel:+16202669837">
  <img  
	  src="https://img.shields.io/badge/+1%20620%20266%209837-darkred?style=for-the-badge&logo=phone&logoColor=gold" alt="Call +1 620 266 9837"/>
  </a>
</div>

# Gremlin Web Scraper MCP

</div>

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
