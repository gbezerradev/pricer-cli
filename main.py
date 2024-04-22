import click
import pkgutil
import commands


@click.group()
def cli():
    """
    Pricer-CLI
    """
    pass


# Descoberta automática de grupos de comandos
for _, name, _ in pkgutil.iter_modules(commands.__path__, "commands."):
    module = __import__(name, fromlist=["cli"])
    for item in dir(module):
        if isinstance(getattr(module, item), click.Group):
            cli.add_command(getattr(module, item))

if __name__ == "__main__":
    cli()
