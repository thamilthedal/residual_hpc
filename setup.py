# setup.py
from setuptools import setup, find_packages

setup(
    name="monitor-cli",
    version="1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'pandas',
        'numpy',
        'paramiko',
        'matplotlib',
        'python-dotenv'
    ],
    entry_points={
        'console_scripts': [
            'monitor=CLI.main:monitor',
        ],
    },
)
