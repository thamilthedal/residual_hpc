# super_cli/my_cli.py
import click
from bin.commands import _monitor, _jobs, _file

@click.group()
def monitor():
    _jobs()

@monitor.command()
def residue():
    _monitor()

@monitor.command()
def file():
    _file()



if __name__ == '__main__':
    super()
