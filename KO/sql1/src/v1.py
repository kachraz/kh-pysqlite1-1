# Setting up the DATABASE
from http.client import HTTPException
from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from typing import Optional

# Pretty Errors
from rich.traceback import install

install(show_locals=True)

# Importing FastAPI
from fastapi import FastAPI, Depends

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


# sqlite db intialization function - THis remains constant in every project
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Pydantic Model for users creation
class UserCreate(BaseModel):
    name: str
    fetish: str
    email: str


# Pydantic model for getting the response
class UserResponse(BaseModel):
    id: int
    name: str
    fetish: str
    email: str

    class Config:
        from_attributes = True  # Update to the new configuration key


# Post Endpoint for populating DB
@my_db_pussy.post("/sluts/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(name=user.name, fetish=user.fetish, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user  # Return the created User instance


# Add a route for the root path - This was not necessary
@my_db_pussy.get("/")
def read_root():
    return {"message": "Welcome to the API"}


# Generic Get Endpoint
@my_db_pussy.get("/sluts/", response_model=list[UserResponse])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = db.query(User).offset(skip).limit(limit).all()
    return users


# Getting the user with the ID which was defined earlier int he Db model
@my_db_pussy.get("/sluts/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# Update the user with the ID which was defined earlier int he Db model


# Pydantic Model for doing updated
class UserUpdate(BaseModel):
    name: Optional[str] = None
    fetish: Optional[str] = None
    email: Optional[str] = None


# Actuak update endpoint


@my_db_pussy.put("/sluts/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if user_update.name is not None:
        user.name = user_update.name
    if user_update.fetish is not None:
        user.fetish = user_update.fetish
    if user_update.email is not None:
        user.email = user_update.email
    db.commit()
    db.refresh(user)
    return user
