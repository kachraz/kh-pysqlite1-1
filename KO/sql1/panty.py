from rich import print as rprint
from rich.traceback import install
from src.uti import label
from fastapi import FastAPI
from src.v1 import my_db_pussy, DATABASE_URL, engine, SessionLocal, Base
import uvicorn

install(show_locals=True)


# def main():
#     label("Execute v1a")
#     v1a()


if __name__ == "__main__":
    uvicorn.run(my_db_pussy, host="127.0.0.1", port=8000)
