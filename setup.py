from rufus.agent import RufusAgent

agent = RufusAgent()
agent.crawl_and_synthesize(
    url="https://quotes.toscrape.com/",
    prompt="Extract contact information",
    output_format="csv",
    output_path="output.csv",
    max_depth=2
)
