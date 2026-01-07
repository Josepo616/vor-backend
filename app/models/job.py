from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import TimestampModel
from app.models.user import User
from app.models.candidate import Candidate

# Use string for the type hint to avoid circular import

class JobReq(TimestampModel):
    __tablename__ = "jobs"

    title: Mapped[str] = mapped_column(index=True)
    description: Mapped[str] = mapped_column(Text) # Text allows for longer descriptions
    description: Mapped[str] = mapped_column(Text)

    # Foreign key to link to the recruiter (user)
    recruiter_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    # Relationship
    recruiter: Mapped["User"] = relationship(back_populates="jobs")
    candidates: Mapped[list["Candidate"]] = relationship(back_populates="job")
