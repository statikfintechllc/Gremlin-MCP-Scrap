## Gremlins MCP Scraper

```
mcp-gremlin-scraper/
    ├── LICENSE          
    ├── package.json          # npm metadata + MCP descriptor
    ├── index.js              # Node launcher: installs deps & boots Flask server
    ├── server.py             # Flask app exposing /scrape, /crawl, /crawl-stream, /mcp/metadata, /ping
    ├── mcp_crawler.py        # AsyncWebCrawler: multi‐page crawler implementation
    ├── mcp.json              # Standalone MCP metadata file
    ├── requirements.txt      # Python dependencies for Flask, httpx, BeautifulSoup, Loguru
    └── docs/
          ├── STRUCTURE.md      # This file: directory overview
          ├── DESCRIPTION.md    # Detailed service description & usage examples
          └── README.md         # Getting-started guide & installation instructions
```
