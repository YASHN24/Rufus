from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from rufus.agent import RufusAgent

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to Rufus API!"}

@app.post("/nested_scrape")
def nested_scrape(url: str, prompt: str, max_depth: int = 2):
    try:
        agent = RufusAgent()
        result = agent.crawl_website(url, prompt, max_depth)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/crawl_and_synthesize")
def crawl_and_synthesize(
    url: str,
    prompt: str,
    output_format: str = "json",
    max_depth: int = 2,
    output_path: str = "output.json"
):
    try:
        agent = RufusAgent()
        file_path = agent.crawl_and_synthesize(
            url, prompt, output_format, output_path, max_depth
        )
        return {"message": "Data synthesized successfully", "file": file_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/download")
def download(file_path: str):
    try:
        return FileResponse(file_path, filename=file_path.split("/")[-1])
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found.")
