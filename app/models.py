from sqlalchemy import Column, Integer, String
from .database import Base

class QueryLog(Base):
    __tablename__ = 'query_log'
    id = Column(Integer, primary_key=True, index=True)
    natural_language_query = Column(String, index=True)
    pseudo_sql_query = Column(String)
    explanation = Column(String)


