from array import array
from multiprocessing.dummy import Array
from typing import List, Union

from pydantic import BaseModel

#------------------------FaceImage-------------------------

class FaceImage(BaseModel):
    id : int
    class Config:
        orm_mode = True

class FaceImageCreate(FaceImage):
    image : str
    

#------------------------Info-------------------------

class Info(BaseModel):
    id : int  

    class Config:
        orm_mode = True 

class CreateInfo(Info):
    user_id : int   
    gender : str
    age : int 


#------------------------Recommendation-------------------------

class Recommendation(BaseModel):
    id : int 
    user_id : int 

    class config:
        orm_mode = True

class CreateRecommendation(Recommendation):
    category1 : str 
    category2 : str 
    category3 : str

#------------------------Ad-------------------------

class Ad(BaseModel):
    id : int 
    category : str 
    ad_image : str
    store_name : str

    class config:
        orm_mode = True

#------------------------StoreMapImage-------------------------

class StoreMapImage(BaseModel):
    id : int 
    store_name : str

    class config:
        orm_mode = True