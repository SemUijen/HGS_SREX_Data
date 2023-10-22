from multiprocessing import Pool
import multiprocessing
import pickle
import numpy as np
import os

from utils.read_input import read_input
from utils.IndexSampler import IndexSampler

from pyvrp import read
from label_create import main_grid, main_full

if __name__ == "__main__":

    instance_names = ["X-n439-k37", "X-n393-k38", "X-n449-k29", "ORTEC-n405-k18", "ORTEC-n510-k23", "X-n573-k30",
                      "ORTEC-VRPTW-ASYM-0bdff870-d1-n458-k35", "R2_8_9", 'R1_4_10']

    array_sol1, array_sol1_ids, array_group1, sampler1 = read_input("X-n439-k37")
    array_sol2, array_sol2_ids, array_group2, sampler2 = read_input("X-n393-k38")
    array_sol3, array_sol3_ids, array_group3, sampler3 = read_input("X-n449-k29")
    array_sol4, array_sol4_ids, array_group4, sampler4 = read_input("ORTEC-n405-k18")
    array_sol5, array_sol5_ids, array_group5, sampler5 = read_input("ORTEC-n510-k23")
    array_sol6, array_sol6_ids, array_group6, sampler6 = read_input("X-n573-k30")
    array_sol7, array_sol7_ids, array_group7, sampler7 = read_input("ORTEC-VRPTW-ASYM-0bdff870-d1-n458-k35")
    array_sol8, array_sol8_ids, array_group8, sampler8 = read_input("R2_8_9", solomon=True)
    array_sol9, array_sol9_ids, array_group9, sampler9 = read_input('R1_4_10', solomon=True)

    sampler1 = IndexSampler(list(sampler1))
    sampler2 = IndexSampler(list(sampler2))
    sampler3 = IndexSampler(list(sampler3))
    sampler4 = IndexSampler(list(sampler4))
    sampler5 = IndexSampler(list(sampler5))
    sampler6 = IndexSampler(list(sampler6))
    sampler7 = IndexSampler(list(sampler7))
    sampler8 = IndexSampler(list(sampler8))
    sampler9 = IndexSampler(list(sampler9))

    c1_groups_used = {}
    c2_groups_used = {}
    tw_groups_used = {}

    cvrp = 0
    tw = 0
    pool_iterable = []
    for _ in range(4):
        i1 = sampler1.sample_index()
        i2 = sampler2.sample_index()
        i3 = sampler3.sample_index()
        i4 = sampler4.sample_index()
        i5 = sampler5.sample_index()
        i6 = sampler6.sample_index()
        i7 = sampler7.sample_index()
        i8 = sampler8.sample_index()
        i9 = sampler9.sample_index()

        # CVRP group1
        temp_ids = []
        temp_sols = []
        instance_names = ["X-n439-k37", "X-n393-k38", "ORTEC-n405-k18"]
        temp_sols.append(list(array_sol1[array_group1 == i1]))
        temp_sols.append(list(array_sol2[array_group2 == i2]))
        temp_sols.append(list(array_sol4[array_group4 == i4]))

        temp_ids.append(list(array_sol1_ids[array_group1 == i1]))
        temp_ids.append(list(array_sol2_ids[array_group2 == i2]))
        temp_ids.append(list(array_sol4_ids[array_group4 == i4]))

        pool_iterable.append((f'cvrp_{cvrp}', instance_names, temp_sols, temp_ids))
        c1_groups_used[cvrp] = [i1, i2, i4]
        cvrp += 1

        # CVRP group2
        temp_ids = []
        temp_sols = []
        instance_names = ["X-n449-k29", "ORTEC-n510-k23", "X-n573-k30"]
        temp_sols.append(list(array_sol3[array_group3 == i3]))
        temp_sols.append(list(array_sol5[array_group5 == i5]))
        temp_sols.append(list(array_sol6[array_group6 == i6]))

        temp_ids.append(list(array_sol3_ids[array_group3 == i3]))
        temp_ids.append(list(array_sol5_ids[array_group5 == i5]))
        temp_ids.append(list(array_sol6_ids[array_group6 == i6]))

        pool_iterable.append((f'cvrp_{cvrp}', instance_names, temp_sols, temp_ids))
        c2_groups_used[cvrp] = [i3, i5, i6]
        cvrp += 1

        # VPRTW-instances
        temp_ids = []
        temp_sols = []
        instance_names = ["ORTEC-VRPTW-ASYM-0bdff870-d1-n458-k35", "R2_8_9", 'R1_4_10']
        temp_sols.append(list(array_sol7[array_group7 == i7]))
        temp_sols.append(list(array_sol8[array_group8 == i8]))
        temp_sols.append(list(array_sol9[array_group9 == i9]))

        temp_ids.append(list(array_sol7_ids[array_group7 == i7]))
        temp_ids.append(list(array_sol8_ids[array_group8 == i8]))
        temp_ids.append(list(array_sol9_ids[array_group9 == i9]))

        pool_iterable.append((f'tw_{tw}', instance_names, temp_sols, temp_ids))
        tw_groups_used[tw] = [i7, i8, i9]
        tw += 1

    print(c_groups_used)

    """
    with Pool() as pool:
        iter_batches = pool.starmap(main_full, pool_iterable)

        for iter_batch in iter_batches:
            print(iter_batch)"""
