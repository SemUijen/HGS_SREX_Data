from multiprocessing import Pool
import pickle
import numpy as np
import os

from tqdm import tqdm
from utils.label_functions import solve_srex_options

from pyvrp import read
from itertools import product


def main(iter_id, instance_name, solutions, solution_ids):
    print(f"started_{iter_id}")

    INSTANCE = read(f"data/route_instances/{instance_name}.vrp", round_func="round")

    labels = []
    labels_cat = []

    # TODO: add Calculations
    random_acc = []
    random_acc_limit = []

    couple_id = 0
    cap_pen = 400
    tw_pen = 6

    couple_ids = list(map(tuple, product(solution_ids, repeat=2)))
    couple_iter = product(solution_ids, repeat=2)
    print(couple_ids)

    for sol_idx1, sol_idx2 in couple_iter:
        parent1, parent2 = solutions[sol_idx1 - 1], solutions[sol_idx2 - 1]

        numR_P1 = parent1.num_routes()
        numR_P2 = parent2.num_routes()
        Max_to_move = min(numR_P1, numR_P2)

        label_shape = (numR_P1, numR_P2, Max_to_move - 1)
        label_improv = np.zeros(label_shape, dtype=float)
        label_categ = np.zeros(label_shape, dtype=int)
        for idx1 in tqdm(range(0, numR_P1)):
            for idx2 in range(0, numR_P2):
                for numRoutesMove in range(1, Max_to_move):
                    abs_improv, category = solve_srex_options(data=INSTANCE, seed=42, couple=(parent1, parent2),
                                                              idx=(idx1, idx2), couple_id=couple_id, capP=cap_pen,
                                                              twP=tw_pen, moves=numRoutesMove)
                    label_improv[(idx1, idx2, numRoutesMove - 1)] = abs_improv
                    label_categ[(idx1, idx2, numRoutesMove - 1)] = category

        labels.append(label_improv)
        labels_cat.append(label_categ)

    raw_data = {
        "route_instance_name": instance_name}

    with open(f"data/raw_model_data/{instance_name}_rawdata_{iter_id}.pkl", "wb") as handle:
        pickle.dump(raw_data, handle)

    return f"Process finished {iter_id}"


if __name__ == "__main__":

    instance_name = 'X-n439-k37'
    with open(f"data/solutions/just_solutions.pkl", 'rb') as handle:
        solutions = pickle.load(handle)

    main(0, instance_name, solutions[0:2], [1, 2])
