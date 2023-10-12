from multiprocessing import Pool
import pickle
import numpy as np
import os
from itertools import permutations
from tqdm import tqdm

from utils.label_functions import solve_srex_options
from utils.read_input import read_input
from utils.IndexSampler import IndexSampler

from pyvrp import read, Solution


def main(iter_id, instance_name, solutions, solution_ids):
    print(f"started_{iter_id}")
    for group_id in range(len(solution_ids)):

        INSTANCE = read(f"data/route_instances/{instance_name[group_id]}.vrp", round_func="round")

        labels = []
        labels_cat = []

        random_acc_list = []
        lim_random_acc_list = []
        couple_id_list = []
        solution_list = []
        couple_id = 0
        cap_pen = 400
        tw_pen = 6

        couple_ids = list(map(tuple, permutations(solution_ids[group_id], r=2)))
        couple_iter = permutations([1, 2, 3, 4], r=2)

        print(couple_ids)
        sol_group = solutions[group_id]
        begin_id = 1

        for sol_idx1, sol_idx2 in couple_iter:

            total_improvements = 0
            limited_improvements = 0
            parent1, parent2 = sol_group[sol_idx1 - 1], sol_group[sol_idx2 - 1]

            numR_P1 = parent1.num_routes()
            numR_P2 = parent2.num_routes()
            Max_to_move = min(numR_P1, numR_P2)

            label_shape = (numR_P1, numR_P2, Max_to_move - 1)
            label_improv = np.zeros(label_shape, dtype=float)
            label_categ = np.zeros(label_shape, dtype=int)

            # alternate starting indices
            # grid_id is used to create a grid within the matrix that is calculated
            if begin_id == 1:
                grid_id = 2
                begin_id = 2
            else:
                grid_id = 1
                begin_id = 1

            for idx1 in tqdm(range(0, numR_P1)):
                if numR_P2 % 2 == 0:
                    grid_id = 2 if grid_id == 1 else 1
                for idx2 in range(0, numR_P2):
                    grid_id = 2 if grid_id == 1 else 1
                    for numRoutesMove in range(grid_id, Max_to_move, 2):

                        abs_improv, category = solve_srex_options(data=INSTANCE, seed=42, couple=(parent1, parent2),
                                                                  idx=(idx1, idx2), couple_id=couple_id, capP=cap_pen,
                                                                  twP=tw_pen, moves=numRoutesMove)
                        label_improv[(idx1, idx2, numRoutesMove - 1)] = abs_improv
                        label_categ[(idx1, idx2, numRoutesMove - 1)] = category

                        # Calculating accuracy
                        if category == 4:
                            total_improvements += 1
                            if idx1 == idx2 or idx2 == 0:
                                limited_improvements += 1

            total_options = numR_P1 * numR_P2 * (Max_to_move - 1)
            limited_options = max(numR_P1, numR_P2) * (Max_to_move - 1)
            labels.append(label_improv)
            labels_cat.append(label_categ)
            random_acc_list.append(total_improvements / total_options)
            lim_random_acc_list.append(limited_improvements / limited_options)
            couple_id_list.extend(couple_ids)
            solution_list.extend(solutions)

    raw_data = {
        "parent_routes": solutions,
        "parent_couple_idx": couple_id_list,
        "labels": labels,
        "labels_cat": labels_cat,
        "random_acc": random_acc_list,
        "random_acc_limit": lim_random_acc_list,
    }
    with open(f"data/raw_model_data/batch_{iter_id}_rawdata.pkl", "wb") as handle:
        pickle.dump(raw_data, handle)

    return f"Process finished {iter_id}"


if __name__ == "__main__":

    sol1, sol1_ids, sol1_group_idx = read_input("X-n439-k37")

    array_group1 = np.array(sol1_group_idx)
    array_sol1 = np.array(sol1)
    array_sol1_ids = np.array(sol1_ids)
    pool_iterable = []
    instance_names = ["X-n439-k37", "X-n439-k37", "X-n439-k37"]

    indexSampler = IndexSampler(array_group1.max())

    for i in range(array_group1.max()):
        temp_ids = []
        temp_sols = []

        i1, i2, i3, i4, i5, i6 = indexSampler.sample_index()

        temp_sols.append(list(array_sol1[array_group1 == i1]))
        temp_sols.append(list(array_sol1[array_group1 == i2]))
        temp_sols.append(list(array_sol1[array_group1 == i3]))
        temp_sols.append(list(array_sol1[array_group1 == i4]))
        temp_sols.append(list(array_sol1[array_group1 == i5]))
        temp_sols.append(list(array_sol1[array_group1 == i6]))

        temp_ids.append(list(array_sol1_ids[array_group1 == i1]))
        temp_ids.append(list(array_sol1_ids[array_group1 == i2]))
        temp_ids.append(list(array_sol1_ids[array_group1 == i3]))
        temp_ids.append(list(array_sol1_ids[array_group1 == i4]))
        temp_ids.append(list(array_sol1_ids[array_group1 == i5]))
        temp_ids.append(list(array_sol1_ids[array_group1 == i6]))


        pool_iterable.append((i, instance_names, temp_sols, temp_ids))




    """    with Pool(processes=2) as pool:
        iter_batches = pool.starmap(main, pool_iterable)

        for iter_batch in iter_batches:
            print(iter_batch)"""

