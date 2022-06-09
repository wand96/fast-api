from sqlalchemy import VARCHAR, Column, ForeignKey, Integer, BLOB
from sqlalchemy.orm import relationship

from database import Base

class FaceImage(Base):
    __tablename__ = "faceimages"

    id = Column(Integer, primary_key=True, index=True, autoincrement = True)
    image = Column(VARCHAR(40), index=True)

    infos = relationship("Info", back_populates = "images")

class Info(Base):
    __tablename__ = "infos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    gender = Column(VARCHAR(40), unique=False, index=True)
    age = Column(Integer, unique=False, index=True)
    user_id = Column(Integer, ForeignKey("faceimages.id"))

    images = relationship("FaceImage", back_populates = "infos")
    
class Recommendation(Base):
    __tablename__ = "recommendations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer,  ForeignKey("infos.id"))
    category1 = Column(VARCHAR(50))
    category2 = Column(VARCHAR(50))
    category3 = Column(VARCHAR(50))
    """
    what is the output of the bigdata model? 
    """

class Ad(Base):
    __tablename__ = "ads"

    id = Column(Integer, primary_key = True, index=True)
    ad_image = Column(BLOB, index=True)
    category = Column(VARCHAR(50), index=True)
    store_name = Column(VARCHAR(50))

class StoreMapImage(Base):
    __tablename__ = "storemapimages"

    id = Column(Integer, primary_key=True, index=True)
    store_name = Column(VARCHAR(50))