from sqlalchemy import Column, Integer, String

from db.base_class import Base

class Salon(Base):
    __tablename__ = 'salon'
    salon_id = Column(Integer, primary_key=True)
    budget = Column(String)
    salon_name = Column(String)
    rating = Column(Integer)
    reviews = Column(Integer)
    website = Column(String)
    phone = Column(String)
    address = Column(String)