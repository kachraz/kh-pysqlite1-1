# Version1 Testing
from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from fastapi import FastAPI

# -- Setting up the connection to the sqlite databse ---
my_db_pussy = FastAPI()

DATABASE_URL = "sqlite:///./pusy.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Defining the table here
class User(Base):
    __tablename__ = "sluts"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    fetish = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
