# residual_hpc
A Python project to monitor residuals of ANSYS Fluent simulations running on a HPC Cluster from a local machine through SSH.

- Plots the residual graph from the out file of a Fluent simulation and updates it over an interval.
- Cannot yet plot when the number of equations are increased in the middle of simulation and will throw error.

## To Run
```
python residue.py <path_to_output_file_in_Cluster>
```
