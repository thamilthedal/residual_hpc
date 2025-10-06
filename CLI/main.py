# super_cli/my_cli.py
import click

@click.group()
def monitor():
    from CLI.bin.cluster import print_jobs
    print_jobs()

@monitor.command()
def file():
    from CLI.bin.clearing import _clear_pyc
    from CLI.bin.multifile import multi_file_monitor
    multi_file_monitor()
    _clear_pyc()

@monitor.command()
def residue():
    from CLI.bin.clearing import _clear_pyc
    from CLI.bin.multiresidue import multi_residue_monitor
    multi_residue_monitor()
    _clear_pyc()

if __name__ == '__main__':
    super()
