# super_cli/my_cli.py
import click
from bin.commands import _monitor

@click.command()
def monitor():
    _monitor()


if __name__ == '__main__':
    super()
