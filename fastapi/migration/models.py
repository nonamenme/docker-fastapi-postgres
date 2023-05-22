from datetime import datetime

from sqlalchemy import create_engine, Column, String, Integer, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from core.config import get_env

# Engine の作成
Engine = create_engine(
    get_env().database_url,
    encoding="utf-8",
    echo=False
)

BaseModel = declarative_base()

class User(BaseModel):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    login_id = Column(String(20), unique=True, nullable=False)
    password = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.now, nullable=False)