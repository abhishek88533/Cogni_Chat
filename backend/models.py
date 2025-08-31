from pydantic import BaseModel
from typing import List

# --- Request Models ---
class IngestRequest(BaseModel):
    """
    Model for ingestion requests.
    """
    sorce_name: str
    text: str

class QueryRequest(BaseModel):
    """
    Model for query requests.
    """
    query: str

# --- Response Models ---
class Source(BaseModel):
    id: int
    text: str

class QueryResponse(BaseModel):
    answer: str
    sources: List[Source]

class IngestResponse(BaseModel):
    message: str