from rufus.scrapper import WebScraperWithDynamicSupport
from rufus.synthesizer import ContentSynthesizer
from rufus.logger import logger


class RufusAgent:
    def __init__(self):
        self.scraper = WebScraperWithDynamicSupport()
        self.synthesizer = ContentSynthesizer()
        logger.info("RufusAgent initialized.")

    def crawl_website(self, url, prompt, max_depth=2):
        logger.info(f"Starting crawl on {url} with prompt: {prompt}")
        try:
            raw_data = self.scraper.crawl_site(url, max_depth)
            logger.info(f"Successfully crawled {len(raw_data)} pages.")
            return {"status": "success", "data": raw_data}
        except Exception as e:
            logger.error(f"Error during crawl: {e}")
            return {"status": "error", "message": str(e)}

    def crawl_and_synthesize(self, url, prompt, output_format="json", output_path="output.json", max_depth=2):
        logger.info(f"Starting crawl and synthesis on {url}")
        raw_data = self.scraper.crawl_site(url, max_depth)

        logger.info("Filtering data based on prompt relevance.")
        filtered_data = self.synthesizer.filter_relevant_content(raw_data, prompt)

        if output_format == "json":
            self.synthesizer.synthesize_to_json(filtered_data, output_path)
        elif output_format == "csv":
            self.synthesizer.synthesize_to_csv(filtered_data, output_path)
        else:
            raise ValueError("Unsupported format. Choose 'json' or 'csv'.")

        logger.info(f"Data saved to {output_path}")
        return output_path
