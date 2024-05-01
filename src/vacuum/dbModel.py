from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass

class MainItem(Base):
    __tablename__ = "MainItem"
    id: Mapped[int] = mapped_column(primary_key=True)
    ProductTitle: Mapped[str] = Mapped[Optional[str]]
    PublishDate : Mapped[str] = Mapped[Optional[str]]
    Contact : Mapped[str] = Mapped[Optional[str]]
    PublishLink : Mapped[str] = Mapped[Optional[str]]
    ProductPrice : Mapped[str] = Mapped[Optional[str]]
    VendorLocation : Mapped[str] = Mapped[Optional[str]]
    CreatedAt : Mapped[str] = Mapped[Optional[str]]