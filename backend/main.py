from fastapi import FastAPI, Query
from src.semantic_searcher import SemanticSearcher
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

neural_searcher = SemanticSearcher(collection_name="patent_index")

@app.get("/api/search")
def search_startup(query: str = Query(..., title="Query", description="Enter your search query")):
    logger.info(f"Received search request with query: {query}")
    results = neural_searcher.search(text=query)
    logger.info(f"Search results: {results}")
    return {"results": results}

if __name__ == "__main__":
    import uvicorn

    logger.info("Starting FastAPI server")
    uvicorn.run(app, host="0.0.0.0", port=8000)