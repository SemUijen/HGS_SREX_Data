import pickle

from pyvrp import read, Solution


def read_input(instance_name: str):

    with open(f"data/solutions/{instance_name}.pkl", 'rb') as handle:
        sol_data = pickle.load(handle)

    INSTANCE = read(f"data/route_instances/{instance_name}.vrp", round_func="round")

    solution_list = []
    for solution_route in sol_data['solution_routes']:
        sol = Solution(data=INSTANCE, routes=solution_route)
        solution_list.append(sol)

    return solution_list, sol_data['solution_id'], sol_data['sol_group_indices']