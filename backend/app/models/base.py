from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, DateTime
from sqlmodel import Field, SQLModel
from typing import Optional
from datetime import datetime
from sqlalchemy.sql import func

class Base(DeclarativeBase):
    pass

class TimestampMixin(SQLModel):
    created_at: Optional[datetime] = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now())
    )

    updated_at: Optional[datetime] = Field(
        sa_column=Column(
            DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
        )
    )