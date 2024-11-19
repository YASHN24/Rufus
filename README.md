# Rufus: Intelligent Web Data Extraction for LLMs
Rufus is cutting-edge AI-driven intelligent site crawling developed to extract relevant data from sites based on user-defined prompts and then produce it in structured formats like JSON or CSV. This piece of software may be very useful in preparing data for RAG (Retrieval-Augmented Generation) pipelines in language models.

# Features
Intelligent Crawling: Nested links, dynamically loaded content, and user-defined crawling depth.
Prompt-Based Data Extraction: Filters and returns only the required data as requested from a given prompt.
Structured Output: The output is in JSON or CSV files, ready to be used immediately for downstream applications.
Dynamic Content Support: Uses Playwright to scrape dynamically rendered content that may have been induced by JavaScript.
Error Handling & Logging: Strong error handling technique and log details for debugging and monitoring.

# Project Structure
rufus/
├── data/
├── docs/
├── rufus/
│   ├── __init__.py
│   ├── agent.py
│   ├── scraper.py
│   ├── synthesizer.py
│   ├── api.py
│   ├── logger.py
├── tests/
├── requirements.txt
├── setup.py
├── README.md
├── main.py
└── .gitignore

# Installation
Clone the repository:


git clone https://github.com/your-username/rufus.git
cd rufus
Create a virtual environment and activate it:


python -m venv venv
venv\Scripts\activate  # Windows
Install dependencies:


pip install -r requirements.txt
Install Playwright (for dynamic content scraping):


playwright install


# Usage
1. Command-Line
Run Rufus from the terminal:
python main.py

3. API (FastAPI)
Start the API server:
uvicorn rufus.api:app --reload
Available Endpoints:
GET /: Welcome message.
POST /nested_scrape: Crawl nested links.
POST /crawl_and_synthesize: Crawl and synthesize data into structured formats.
Example request for /crawl_and_synthesize:
{
  "url": "https://example.com",
  "prompt": "Extract FAQs and pricing information",
  "output_format": "json",
  "max_depth": 2
}
3. Programmatic Usage
python
Copy code
from rufus.agent import RufusAgent

agent = RufusAgent()
agent.crawl_and_synthesize(
    url="https://example.com",
    prompt="Extract contact information",
    output_format="csv",
    output_path="output.csv",
    max_depth=2
)
Testing
Run all tests using pytest:

pytest
Logging
All logs are stored in rufus.log. Tail the logs for debugging:

tail -f rufus.log

# Challenges Solved
Handling nested links and dynamic content.
Extracting relevant data based on user-defined prompts.
Ensuring robust error handling and user-friendly logging.
