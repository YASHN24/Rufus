from rufus.scraper import WebScraperWithDynamicSupport

def test_crawl_site():
    scraper = WebScraperWithDynamicSupport()
    result = scraper.crawl_site("https://example.com", max_depth=1)
    assert isinstance(result, dict)
    assert len(result) > 0
