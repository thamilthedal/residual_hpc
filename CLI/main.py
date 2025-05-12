# super_cli/my_cli.py
import click
from bin.commands import _monitor, _jobs, _file, _clear_pyc

@click.group()
def monitor():
    _jobs()

@monitor.command()
def residue():
    _monitor()
    _clear_pyc()

@monitor.command()
def file():
    _file()
    _clear_pyc()



if __name__ == '__main__':
    super()
