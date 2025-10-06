import random

simulation_data = {}

def fetch_latest_residue_data(case_id, residual_names):
    """Placeholder function. Replace with your data fetching logic."""
    if case_id not in simulation_data:
        simulation_data[case_id] = {
            'iterations': [],
            'residuals': {name: [] for name in residual_names},
            'last_resids': {name: random.uniform(0.5, 1.5) for name in residual_names}
        }

    state = simulation_data[case_id]
    current_iter = len(state['iterations'])
    
    for i in range(5):
        new_iter = current_iter + i + 1
        state['iterations'].append(new_iter)
        for name in residual_names:
            last_resid = state['last_resids'][name]
            new_resid = last_resid * (0.95 - random.uniform(0, 0.01))
            state['residuals'][name].append(new_resid)
            state['last_resids'][name] = new_resid

    return state['iterations'], state['residuals']
