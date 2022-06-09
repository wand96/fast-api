from sqlalchemy import BLOB
from sqlalchemy.orm import Session 

from sqlalchemy.orm import Session

import models, schemas


#AI_Input

#RPi post 
def create_faceimage(db: Session, faceimage: str):
    db_image = models.FaceImage(image= faceimage)
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image

#Ai Model post
def create_info(db: Session, user_gender: str, user_age: int, user_id: int):
    db_info = models.Info(user_id = user_id, gender=user_gender, age=user_age)
    db.add(db_info)
    db.commit()
    db.refresh(db_info)
    return db_info

#Big Data Model post
def create_recommendation(db: Session, category1 : str, category2 : str, category3 : str):
    db_reco = models.Recommendation(category1 = category1, category2 = category2, category3 = category3)
    db.add(db_reco)
    db.commit()
    db.refresh(db_reco)
    return db_reco