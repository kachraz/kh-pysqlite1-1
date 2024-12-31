from src.v1 import v1a
from rich import print as rprint
from rich.traceback import install
from src.uti import label

install(show_locals=True)


def main():
    label("Execute v1a")
    v1a()


if __name__ == "__main__":
    main()
