from sqlalchemy import Column, Integer, JSON
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Dataset(Base):
    __tablename__ = "datasets"
    id = Column(Integer, primary_key=True)
    dataset = Column(JSON)
    size = Column(Integer)
