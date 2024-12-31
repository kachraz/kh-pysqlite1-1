# Rich Prettifier Code
# ------------------------------------------------------
from rich import print as rprint  # For rprinting
from rich.pretty import pprint  # For pretty printing
from rich import inspect  # For inspect
from rich.console import Console  # For console.print
from rich.markdown import Markdown  # For markdow
from rich.panel import Panel  # For Panel()
from rich import box  # For Panel Boxes
from rich.prompt import Prompt  # For Prompting
from rich.style import Style  # For styles colors
from rich.text import Text  # For text Styles

console = Console()  # Standard code to access console
from rich.traceback import install

install(show_locals=True)
# -------------------------------------------------------


def cprint(name):
    console.print(
        f"""{name}""",
        style="bold",
        justify="center",
    )
