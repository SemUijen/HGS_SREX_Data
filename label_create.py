import pickle
from itertools import permutations
from tqdm import tqdm
import numpy as np
import time
import datetime
from utils.label_functions import solve_srex_options

from pyvrp import read
import logging

def main_grid(iter_id, instance_name, solutions, solution_ids):

    start = time.perf_counter()
    logging.warning(f"started_{iter_id} -- nrGroups: {len(solution_ids)} -- started at: {datetime.datetime.now()}")
    print(f"started_{iter_id} -- nrGroups: {len(solution_ids)} -- started at: {datetime.datetime.now()}")
    for group_id in range(len(solution_ids)):

        if instance_name[group_id] in ["R2_8_9", 'R1_4_10']:
            INSTANCE = read(f"data/route_instances/{instance_name[group_id]}.vrp", round_func="round", instance_format="solomon")
        else:
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
        couple_id_list.extend(couple_ids)
        solution_list.extend(solutions)
        couple_iter = permutations([1, 2, 3, 4], r=2)

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
            logging.warning(f"started_{instance_name[group_id]} -- label shape: {label_shape} -- started at: {datetime.datetime.now()}")
            # alternate starting indices
            # grid_id is used to create a grid within the matrix that is calculated
            if begin_id == 1:
                grid_id = 2
                begin_id = 2
            else:
                grid_id = 1
                begin_id = 1

            for idx1 in range(0, numR_P1):
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

            logging.warning(
                f"finished_{instance_name[group_id]} -- label shape: {label_shape} -- started at: {datetime.datetime.now()}")
            total_options = numR_P1 * numR_P2 * (Max_to_move - 1)
            limited_options = max(numR_P1, numR_P2) * (Max_to_move - 1)
            labels.append(label_improv)
            labels_cat.append(label_categ)
            random_acc_list.append(total_improvements / total_options)
            lim_random_acc_list.append(limited_improvements / limited_options)


    raw_data = {
        "parent_routes": solution_list,
        "parent_couple_idx": couple_id_list,
        "labels": labels,
        "labels_cat": labels_cat,
        "random_acc": random_acc_list,
        "random_acc_limit": lim_random_acc_list,
    }
    with open(f"data/raw_model_data/batch_{iter_id}_rawdata.pkl", "wb") as handle:
        pickle.dump(raw_data, handle)

    logging.info(f"Process finished {iter_id}: time in minutes= {(time.perf_counter() - start) / 60}")
    return f"Process finished {iter_id}: time in minutes= {(time.perf_counter() - start)/60}"


def main_full(iter_id, instance_name, solutions, solution_ids):

    start = time.perf_counter()
    logging.warning(f"started_{iter_id} -- nrGroups: {len(solution_ids)} -- started at: {datetime.datetime.now()}")

    for group_id in range(len(solution_ids)):

        if instance_name[group_id] in ["R2_8_9", 'R1_4_10']:
            INSTANCE = read(f"data/route_instances/{instance_name[group_id]}.vrp", round_func="round", instance_format="solomon")
        else:
            INSTANCE = read(f"data/route_instances/{instance_name[group_id]}.vrp", round_func="round")

        labels = []
        labels_cat = []

        random_acc_list = []
        lim_random_acc_list = []
        couple_id_list = []
        solution_list = []
        couple_id = 0
        cap_pen = 200
        tw_pen = 4

        couple_ids = list(map(tuple, permutations(solution_ids[group_id], r=2)))
        couple_id_list.extend(couple_ids)
        solution_list.extend(solutions)
        couple_iter = permutations([1, 2, 3, 4], r=2)

        sol_group = solutions[group_id]

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

            for idx1 in range(0, numR_P1):
                for idx2 in range(0, numR_P2):
                    for numRoutesMove in range(1, Max_to_move):

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

            logging.warning(f"finished: {instance_name[group_id]}-{iter_id} -- label shape: {label_shape} -- at: {datetime.datetime.now()}")
            total_options = numR_P1 * numR_P2 * (Max_to_move - 1)
            limited_options = max(numR_P1, numR_P2) * (Max_to_move - 1)
            labels.append(label_improv)
            labels_cat.append(label_categ)
            random_acc_list.append(total_improvements / total_options)
            lim_random_acc_list.append(limited_improvements / limited_options)



    raw_data = {
        "parent_routes": solutions,
        "parent_couple_idx": couple_id_list,
        "labels": labels,
        "labels_cat": labels_cat,
        "random_acc": random_acc_list,
        "random_acc_limit": lim_random_acc_list,
        "runtime": (time.perf_counter() - start)/60,
    }
    with open(f"data/raw_model_data/batch_{iter_id}_rawdata.pkl", "wb") as handle:
        pickle.dump(raw_data, handle)
    logging.warning(f"Process finished {instance_name}-{iter_id}: time in minutes= {(time.perf_counter() - start)/60}")
    return f"Process finished {iter_id}: time in minutes= {(time.perf_counter() - start)/60}"
