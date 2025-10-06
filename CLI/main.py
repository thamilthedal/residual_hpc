# super_cli/my_cli.py
import click

@click.group()
def monitor():
    from CLI.bin.commands import _jobs
    _jobs()

@monitor.command()
def file():
    from CLI.bin.commands import _clear_pyc
    from CLI.bin.multifile import multi_file_monitor
    multi_file_monitor()
    _clear_pyc()

@monitor.command()
def residue():
    from CLI.bin.commands import _clear_pyc
    from CLI.bin.multiresidue import multi_residue_monitor
    multi_residue_monitor()
    _clear_pyc()

if __name__ == '__main__':
    super()
