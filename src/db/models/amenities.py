from sqlalchemy import Column, Integer, Boolean

from db.base_class import Base

class Amenities(Base):
    __tablename__ = 'amenities'
    salon_id = Column(Integer, primary_key=True)
    mask_required = Column(Boolean)
    accepts_card = Column(Boolean)
    accepts_andriod = Column(Boolean)
    accepts_apple = Column(Boolean)
    good_for_kids = Column(Boolean)
    car_parking = Column(Boolean)
    bike_parking = Column(Boolean)
    free_wifi = Column(Boolean)
    wheelchair_access = Column(Boolean)
    restrooms = Column(Boolean)
    appointments = Column(Boolean)