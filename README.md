# residual_hpc
A Python project to monitor residuals of ANSYS Fluent simulations running on a HPC Cluster from a local machine through SSH.

- Plots the residual graph from the out file of a Fluent simulation and updates it over an interval.
- Show once the results are converged.
- Cannot yet plot when the number of equations are increased in the middle of simulation and will throw error.

## Settings to change
- Change HOST_NAME, USER, PWD in monitor/data.py to your SSH Credentials when you use.
- Any other plot related settings, size, font, color, etc., can be changed in lib/plot_utils.py

## To Run
```
python residue.py <path_to_output_file_in_Cluster>
```

## Dependencies
- Paramiko
- Pandas
- Numpy
- Matplotlib
