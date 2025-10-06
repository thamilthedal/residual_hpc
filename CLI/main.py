# super_cli/my_cli.py
import click

@click.group()
def monitor():
    from bin.commands import _jobs
    _jobs()

@monitor.command()
def file():
    from bin.commands import _clear_pyc
    from bin.multifile import multi_file_monitor
    multi_file_monitor()
    _clear_pyc()

@monitor.command()
def residue():
    from bin.commands import _clear_pyc
    from bin.multiresidue import multi_residue_monitor
    multi_residue_monitor()
    _clear_pyc()

if __name__ == '__main__':
    super()
