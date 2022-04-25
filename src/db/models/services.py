from sqlalchemy import Column, Integer, Boolean

from db.base_class import Base

class Services(Base):
    __tablename__ = 'services'
    salon_id = Column(Integer, primary_key=True)
    coloring = Column(Boolean)
    blowout = Column(Boolean)
    hair_treatment = Column(Boolean)
    kids_haircut = Column(Boolean)
    bridal_service = Column(Boolean)
    hair_extension = Column(Boolean)
    hairsyling = Column(Boolean)
    makeup = Column(Boolean)
    mens_haircut = Column(Boolean)
    womens_haircut = Column(Boolean)