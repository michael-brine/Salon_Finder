
from sqlalchemy import Column, Integer, String

from db.base_class import Base

class Hour(Base):
    __tablename__ = 'hours'
    salon_id = Column(Integer, primary_key=True)
    day = Column(Integer)
    open_time = Column(String)
    close_time = Column(String)