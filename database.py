from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Using MySQL
#you should create database named 'db'or you can modify this code and naming the db names like otheres

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://haha:1234qwer@13.210.217.204:3306/db?charset=utf8"

#mysql url 받아옴

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
#create_engine은 DB로 접속이 가능하도록 해줌

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#SessionLocal 인스턴스를 생성하면 실제 데이터베이스 세션이 됨

Base = declarative_base()
#declarative_base(): 상속클래스들을 자동으로 인지하고 알아서 매핑해줌.