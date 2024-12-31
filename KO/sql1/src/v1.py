# Setting up the DATABASE
from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

# Importing FastAPI
from fastapi import FastAPI

# Validating the input into the db
from pydantic import BaseModel

# -- Setting up the connection to the sqlite databse ---
# Note these are all the things which you will import into your main.py

# This can be a custom name - Note that the name can be anything you want- eg: my_stinky_Lady , you hav to use this in the app.route
my_db_pussy = FastAPI()

DATABASE_URL = "sqlite:///./pusy.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Defining the table structure here
class User(Base):
    __tablename__ = "sluts"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    fetish = Column(String, index=True)
    email = Column(String, unique=True, index=True)


# Creating the Table
Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# The code here was written to undestand how the post operation would work
# @my_db_pussy.post("sluts/", response_model=User)
# def create_user(user: User, db: Session = Depends(get_db)):
#     db_user = User(name=user.name, fetish=user.fetish, email=user.email)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user
