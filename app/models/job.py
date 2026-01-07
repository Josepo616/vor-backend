from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import TimestampModel

# Use string for the type hint to avoid circular import
if TYPE_CHECKING:
    from app.models.user import User
    from app.models.candidate import Candidate

class JobReq(TimestampModel):
    __tablename__ = "jobs"

    title: Mapped[str] = mapped_column(index=True)
    description: Mapped[str] = mapped_column(Text)

    recruiter_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    # Usa comillas para referenciar las clases
    recruiter: Mapped["User"] = relationship(back_populates="jobs")
    candidates: Mapped[list["Candidate"]] = relationship(back_populates="job")
