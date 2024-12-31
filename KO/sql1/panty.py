from src.v1 import v1a
from rich import print as rprint
from rich.traceback import install

install(show_locals=True)


def main():
    rprint("[blue] Running sv1a [/blue]")
    v1a()


if __name__ == "__main__":
    main()
