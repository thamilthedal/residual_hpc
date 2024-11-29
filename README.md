# COMMAND LINE INTERFACE FOR MONITORING RESIDUALS FOR A ANSYS FLUENT SIMULATION IN ROCKS CLUSTER:

## Command:
monitor

## Getting Started

1. Download the repository
2. Use Python 3.12 or above.
3. Run following command
```
pip install -e .
```
4. Change the HOST_NAME, UNAME and PASS for the Cluster in .env file
5. Run the monitor by following command
```
monitor
```

## Extrass:
- Convergence line in red is currently kept at 1e-5 which can also be changed in .env


## TODO:
- Cut Down the data once it exceeds the limit of 100000 iterations. How to do that??

