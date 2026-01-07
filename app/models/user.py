from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import TimestampModel
from app.models.job import JobReq

class User(TimestampModel):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column()
    full_name: Mapped[str | None] = mapped_column(default=None)
    is_active: Mapped[bool] = mapped_column(default=True)

    # Relationship: one recruiter(user) can have many job postings
    jobs: Mapped[list["JobReq"]] = relationship(back_populates="recruiter")
