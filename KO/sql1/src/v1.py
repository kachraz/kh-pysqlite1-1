# Version1 Testing
from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from fastapi import FastAPI

# -- Setting up the connection to the sqlite databse ---
app = FastAPI()

DATABASE_URL = "sqlite:///./pusy.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def v1a():
    print("hey")
