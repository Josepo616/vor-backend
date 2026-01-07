from typing import Any
from sqlalchemy import ForeignKey, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import TimestampModel

class Candidate(TimestampModel):
    __tablename__ = "candidates"

    name: Mapped[str] = mapped_column(index=True)
    email: Mapped[str] = mapped_column(index=True)

    # Raw data
    resume_text: Mapped[str | None] = mapped_column(Text) # Extracted text from PDF

    # Rich data stored as JSONB (essential to save variable structures from LinkedIn/IA))
    # i.e., {"skills": ["Python", "Swift"], "linkedin_summary": "..."}
    parsed_data: Mapped[dict[str, Any] | None] = mapped_column(JSONB, default={})

    # Foreign key to link to the job position
    job_id: Mapped[int] = mapped_column(ForeignKey("jobs.id"))

    # Relationship
    job: Mapped["JobReq"] = relationship(back_populates="candidates")