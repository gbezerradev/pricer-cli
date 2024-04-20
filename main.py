import click

from commands.item import item


@click.group()
def cli():
    """
    Pricer-CLI
    """
    pass


cli.add_command(item)

if __name__ == "__main__":
    cli()
