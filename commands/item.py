import click


@click.group("item")
def item():
    pass


@item.command("add")
def add():
    click.echo("Item added")


if __name__ == "__main__":
    item()
