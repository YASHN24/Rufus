from rufus.agent import RufusAgent
from rufus.synthesizer import ContentSynthesizer


def test_crawl_website():
    agent = RufusAgent()
    result = agent.crawl_website("https://quotes.toscrape.com/m", "Extract FAQs")
    assert result["status"] == "success"


def test_filter_relevant_content():
    synthesizer = ContentSynthesizer()
    data = {
        "https://quotes.toscrape.com/": "This page contains FAQs about our product.",
        "https://books.toscrape.com/": "Unrelated content here."
    }
    prompt = "FAQs"
    filtered = synthesizer.filter_relevant_content(data, prompt)
    assert len(filtered) == 1
    assert "https://quotes.toscrape.com/" in filtered
