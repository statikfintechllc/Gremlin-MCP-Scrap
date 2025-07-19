import asyncio
from loguru import logger
import httpx
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urldefrag


class AsyncWebCrawler:
    def __init__(self, max_pages: int = 50, max_depth: int = 2, concurrency: int = 5):
        self.max_pages = max_pages
        self.max_depth = max_depth
        self.seen = set()
        self.to_visit = asyncio.Queue()
        self.client = httpx.AsyncClient(timeout=30)
        self.semaphore = asyncio.Semaphore(concurrency)

    async def crawl(self, start_url: str) -> dict:
        """Crawl up to max_pages within max_depth, returning a dict of {url: text}."""
        await self.to_visit.put((start_url, 0))
        results = {}

        async def worker():
            while not self.to_visit.empty() and len(self.seen) < self.max_pages:
                url, depth = await self.to_visit.get()
                if url in self.seen or depth > self.max_depth:
                    continue
                self.seen.add(url)
                async with self.semaphore:
                    try:
                        resp = await self.client.get(url)
                        resp.raise_for_status()
                        text, links = self._parse(resp.text, url)
                        results[url] = text
                        for link in links:
                            if link not in self.seen:
                                await self.to_visit.put((link, depth + 1))
                    except Exception as e:
                        logger.error(f"Crawl failed for {url}: {e}")
                        results[url] = {"error": "fetch failed"}

        # spin up workers
        await asyncio.gather(*[worker() for _ in range(self.semaphore._value)])
        await self.client.aclose()
        return results

    def _parse(self, html: str, base_url: str) -> tuple[str, set[str]]:
        """Extract visible text and same-domain links from HTML."""
        soup = BeautifulSoup(html, "html.parser")
        for script in soup(["script", "style"]):
            script.decompose()
        text = soup.get_text(separator="\n", strip=True)

        links = set()
        for a in soup.find_all("a", href=True):
            href = urljoin(base_url, a["href"])
            href = urldefrag(href)[0]
            if href.startswith(base_url):
                links.add(href)
        return text, links
