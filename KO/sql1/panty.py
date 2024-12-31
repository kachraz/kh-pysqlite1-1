from rich import print as rprint
from rich.traceback import install
from src.uti import label
from fastapi import FastAPI
from src.v1 import my_db_pussy, DATABASE_URL, engine, SessionLocal, Base
import uvicorn

install(show_locals=True)

if __name__ == "__main__":
    uvicorn.run(
        my_db_pussy,
        host="0.0.0.0",
        port=9000,
    )
