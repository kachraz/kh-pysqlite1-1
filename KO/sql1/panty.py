from src.v1 import v1a
from rich import print as rprint
from rich.traceback import install
from src.uti import label
from fastapi import FastAPI
from src.v1 import app, DATABASE_URL, engine, SessionLocal, Base

install(show_locals=True)


def main():
    label("Execute v1a")
    v1a()


if __name__ == "__main__":
    main()
