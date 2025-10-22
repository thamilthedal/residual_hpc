# CLI tool for monitoring ANSYS Fluent Cases running in ROCKS HPC:

It can simultaneously monitor residuals or report files upto 9 cases running in HPC

## Command:
monitor

### Sub-commands
- residue
- file

## Getting Started

1. Download the repository
2. Use Python 3.12 or above.
3. Create a virtual environment and activate it.
4. Run the following command to install the library
```
pip install -e .
```
4. Change the HOST_NAME, UNAME and PASS for your Cluster in .env file
5. Run the monitor by following command
```
monitor residue
```

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/5f922eae-42da-4b8e-9d7a-04c0eb017cb5" />

6. To monitor report files, (Save in *.csv fileformat)
```
monitor file
```

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/a68ae6f3-7c72-423b-926a-f30e98fb774a" />


## Extrass:
- Automatic Dark Mode based on System time, from 6 PM to 6 AM



