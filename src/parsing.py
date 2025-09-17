# src/parsing.py
from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import datetime

class Job(BaseModel):
    id: str
    title: str
    company: Optional[str] = None
    location: Optional[str] = None
    url: Optional[HttpUrl] = None
    source: str
    published_at: Optional[datetime] = None
    snippet: Optional[str] = None
    cluster: Optional[str] = None
    score: Optional[float] = None