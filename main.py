from rufus.agent import RufusAgent

if __name__ == "__main__":
    print("Initializing Rufus...")
    agent = RufusAgent()
    # Example usage
    result = agent.crawl_website("https://quotes.toscrape.com/", prompt="Extract FAQs")
    print(result)


agent = RufusAgent()
agent.crawl_and_synthesize(
    url="https://quotes.toscrape.com/",
    prompt="Extract contact information",
    output_format="csv",
    output_path="output.csv",
    max_depth=2
)
