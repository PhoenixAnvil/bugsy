from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID, uuid4

class Issue(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str
    description: Optional[str] = None
    status: str = "open"  # open, in_progress, closed
