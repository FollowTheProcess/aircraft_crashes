"""
Invoke tasks for easy project automation.
"""

from pathlib import Path

from invoke import task
from rich import print as rprint

PROJECT_ROOT = Path(__file__).parent.resolve()


@task
def style(c):
    """
    Runs style checking and linting tools on the project.
    """
    rprint("[bold blue]Formatting... [/bold blue]")
    c.run("isort .")
    c.run("black .")
    rprint("[bold blue]Linting... [/bold blue]")
    c.run("flake8 .")
    rprint("[bold blue]Type Checking... [/bold blue]")
    c.run("mypy .")
