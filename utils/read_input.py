import pickle
import numpy as np
from pyvrp import read, Solution

def read_input(instance_name: str, solomon: bool = False):
    with open(f"data/solutions/{instance_name}.pkl", 'rb') as handle:
        sol_data = pickle.load(handle)

    if solomon:
        INSTANCE = read(f"data/route_instances/{instance_name}.vrp", round_func="round", instance_format="solomon")
    else:
        INSTANCE = read(f"data/route_instances/{instance_name}.vrp", round_func="round")


    solution_list = []
    for solution_route in sol_data['solution_routes']:
        sol = Solution(data=INSTANCE, routes=solution_route)
        solution_list.append(sol)

    return np.array(solution_list), np.array(sol_data['solution_id']), np.array(sol_data['sol_group_indices']), sol_data['sol_group_idx_sample']
