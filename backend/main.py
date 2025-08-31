from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from models import IngestRequest, QueryRequest, QueryResponse, IngestResponse

# 1. Import the new functions from our services file
from services import ingest_text_data, process_query


# Create the FastAPI app instance
app = FastAPI(
    title="Mini RAG API",
    description="An API for a Retrieval-Augmented Generation system.",
    version="1.0.0"
)

# Allow our frontend to talk to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # For simplicity, allow all. In production, you'd list your frontend's URL.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- API Endpoints (with placeholder logic for now) ---

@app.get("/health", tags=["General"])
async def health_check():
    """Health check endpoint required by the assessment."""
    return {"status": "ok"}

# First, add `Request` to your import at the top of the file
# from fastapi import FastAPI, HTTPException, Request

@app.post("/ingest", tags=["RAG"], response_model=IngestResponse)
async def ingest_text(request: Request): # <-- Change here
    """
    Endpoint to process and store text into the vector database.
    """
    try:
        # Manually parse the JSON data from the request body
        data = await request.json()
        source_name = data.get("source_name")
        text = data.get("text")

        if not source_name or not text:
            raise HTTPException(status_code=400, detail="Missing source_name or text")

        print(f"Successfully parsed ingestion data for source: {source_name}")

        ingest_text_data(source_name, text)
        return {"message": f"Successfully ingested text from {source_name}."}
    except Exception as e:
        print(f"Error during ingestion: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/query", tags=["RAG"], response_model=QueryResponse)
async def answer_query(request: QueryRequest):
    """
    Endpoint to ask a question and get a RAG-powered answer.
    """
    try:
        # 3. Connect the query endpoint to the real logic
        response_data = process_query(request.query)
        return response_data
    except Exception as e:
        # This provides a more informative error if something goes wrong during querying
        print(f"Error during query: {e}")
        raise HTTPException(status_code=500, detail=str(e))