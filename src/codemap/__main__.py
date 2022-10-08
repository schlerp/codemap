import click
from codemap.entrypoints import run_api
from codemap.entrypoints import run_prompt


@click.group()
def cli():
    """
    A tool for managing codesets with an API allowing
    you to get mappings on the fly
    """
    pass


@click.command()
def api():
    """run the api"""
    run_api()


@click.command()
def shell():
    """run an interactive shell"""
    run_prompt()


cli.add_command(api)
cli.add_command(shell)

cli()
