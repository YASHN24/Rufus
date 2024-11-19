from bs4 import BeautifulSoup
import requests
from playwright.sync_api import sync_playwright
from rufus.logger import logger


class WebScraper:
    def __init__(self):
        self.visited_urls = set()

    def scrape_page(self, url):
        """
        Scrapes a single web page for content.
        :param url: Target URL
        :return: Raw HTML content
        """
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return BeautifulSoup(response.content, "html.parser")
        except requests.exceptions.RequestException as e:
            print(f"Error scraping {url}: {e}")
            return None

    def crawl_site(self, start_url, max_depth=2):
        """
        Crawls a website starting from the given URL, following nested links up to a specified depth.
        :param start_url: Starting point URL
        :param max_depth: Maximum depth to crawl
        :return: Dictionary of URLs and their content
        """
        crawled_data = {}
        self._crawl_recursive(start_url, crawled_data, 0, max_depth)
        return crawled_data

    def _crawl_recursive(self, url, crawled_data, current_depth, max_depth):
        if current_depth > max_depth or url in self.visited_urls:
            return
        print(f"Crawling: {url} at depth {current_depth}")
        self.visited_urls.add(url)

        soup = self.scrape_page(url)
        if soup:
            crawled_data[url] = soup.text[:1000]
            links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith('http')]
            for link in links:
                self._crawl_recursive(link, crawled_data, current_depth + 1, max_depth)


class WebScraperWithDynamicSupport(WebScraper):
    def scrape_dynamic_page(self, url):
        try:
            with sync_playwright() as p:
                logger.info(f"Launching browser for {url}")
                browser = p.chromium.launch(headless=True)
                page = browser.new_page()
                page.goto(url, timeout=10000)
                content = page.content()
                browser.close()
                logger.info(f"Successfully scraped dynamic page: {url}")
                return BeautifulSoup(content, "html.parser")
        except Exception as e:
            logger.error(f"Error scraping dynamic page {url}: {e}")
            return None