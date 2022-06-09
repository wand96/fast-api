from typing import List

from fastapi import Depends, FastAPI, File, UploadFile
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

import base64

#pip install fastapi
#pip install uvicorn
#pip install sqlalchemy


models.Base.metadata.create_all(bind=engine)
#Android에서 retrofit 설치하기 ^^..

#uvicorn main:app --reload

#AI_input for get by model

# Dependency
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# @app.post("/face-image/", response_model = schemas.FaceImageCreate)
# async def create_image(faceimage: str, db:Session=Depends(get_db)):
#     rps = crud.create_faceimage(db=db, faceimage=faceimage)
#     return rps

# @app.get("/face-image/{id}", response_model = schemas.FaceImageCreate)
# async def read_image(id: int, db: Session = Depends(get_db)):
#     db_image = crud.get_faceimage(db = db, user_id = id)
#     return db_image

#수신 api
#1. 이미지 정보를 faceimages에 저장
#2. 분석 api 호출
#3.

#분석 api
#1. 수신 api의 호출을 받음
#2. ai 모델 실행(DB에 저장된 faceimages를 이용)
#3. 결과를 infos에 저장
#4. 추천 api로? json으로 응답

#추천 api
#1. 분석 api호출을 받음
#2. 빅데이터 모델 실행
#3. 결과를 recommands에 저장
#4. json으로 응답

import requests
#수신

async def ai_model(faceimage:str):

    return {'gender':'F', 'age':1}

async def bigdata_model(user_gender, user_age):

    return {'category1' : 'niniz', 'category2' : 'nike', 'category3' : 'love'}

@app.post("/create-image/")
async def create_image(faceimage: str, db: Session = Depends(get_db)):
    user_id = crud.create_faceimage(db=db, faceimage=faceimage).id
    res1 = requests.post(url="127.0.0.1:8000/ai-model", data={"faceimage":faceimage, "user_id":user_id})
    # faceimage path와 user_id 보내기
    infos = res1.json()

    res2 = requests.post(url="127.0.0.1:8000/recommend-model", data=infos)
    return infos


#분석 api
@app.post("/ai-model/", response_model = schemas.CreateInfo)
async def create_info(user_id : int, faceimage : str, db: Session = Depends(get_db)):
    result = await ai_model(faceimage)
    db_image = crud.create_info(db = db,
                                user_gender=result['gender'],
                                user_age=result['age'],
                                user_id = user_id)
    return db_image

#추천 api
@app.post("/recommend-model/", response_model = schemas.CreateRecommendation)
async def create_recommendation(user_id : int, user_gender: str, user_age : int, db: Session = Depends(get_db)):
    result = bigdata_model(user_gender, user_age)
    return crud.create_recommendation(db = db,
                                      category1=result['category1'],
                                      category2 = result['category2'],
                                      category3 = result['category3'])

