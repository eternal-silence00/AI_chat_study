from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base
from pgvector.sqlalchemy import Vector

class Document(Base):
    
    __tablename__ = "document"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(nullable=False)
    embedding: Mapped[list] = mapped_column(Vector(384), nullable=False)