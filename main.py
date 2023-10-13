from multiprocessing import Pool
import pickle
import numpy as np
import os


from utils.read_input import read_input
from utils.IndexSampler import IndexSampler

from pyvrp import read
from label_create import main_grid, main_full

if __name__ == "__main__":

    instance_names = ["X-n439-k37", "X-n502-k39", "X-n449-k29", "ORTEC-n405-k18", "ORTEC-n510-k23", "ORTEC-n455-k41", "ORTEC-VRPTW-ASYM-0bdff870-d1-n458-k35", "R2_8_9", 'RC2_10_5']

    array_sol1, array_sol1_ids, array_group1 = read_input("X-n439-k37")
    array_sol2, array_sol2_ids, array_group2 = read_input("X-n502-k39")
    array_sol3, array_sol3_ids, array_group3 = read_input("X-n449-k29")
    array_sol4, array_sol4_ids, array_group4 = read_input("ORTEC-n405-k18")
    array_sol5, array_sol5_ids, array_group5 = read_input("ORTEC-n510-k23")
    array_sol6, array_sol6_ids, array_group6 = read_input("ORTEC-n455-k41")
    array_sol7, array_sol7_ids, array_group7 = read_input("ORTEC-VRPTW-ASYM-0bdff870-d1-n458-k35")
    array_sol8, array_sol8_ids, array_group8 = read_input("R2_8_9", solomon=True)
    array_sol9, array_sol9_ids, array_group9 = read_input('RC2_10_5', solomon=True)



    indexSampler = IndexSampler(array_group1.max())



    sol1 = []
    sol2 = []
    sol3 = []
    sol4 = []
    sol5 = []
    sol6 = []
    sol7 = []
    sol8 = []
    sol9 = []
    sol1_id = []
    sol2_id = []
    sol3_id = []
    sol4_id = []
    sol5_id = []
    sol6_id = []
    sol7_id = []
    sol8_id = []
    sol9_id = []
    for i in range(2):
        i1, i2, i3, i4, i5, i6, i7, i8, i9 = i,i,i,i,i,i,i,i,i
        sol1.append(list(array_sol1[array_group1 == i1]))
        sol2.append(list(array_sol2[array_group2 == i2]))
        sol3.append(list(array_sol3[array_group3 == i3]))
        sol4.append(list(array_sol4[array_group4 == i4]))
        sol5.append(list(array_sol5[array_group5 == i5]))
        sol6.append(list(array_sol6[array_group6 == i6]))
        sol7.append(list(array_sol7[array_group7 == i7]))
        sol8.append(list(array_sol8[array_group8 == i8]))
        sol9.append(list(array_sol9[array_group9 == i9]))

        sol1_id.append(list(array_sol1_ids[array_group1 == i1]))
        sol2_id.append(list(array_sol2_ids[array_group2 == i2]))
        sol3_id.append(list(array_sol3_ids[array_group3 == i3]))
        sol4_id.append(list(array_sol4_ids[array_group4 == i4]))
        sol5_id.append(list(array_sol5_ids[array_group5 == i5]))
        sol6_id.append(list(array_sol6_ids[array_group6 == i6]))
        sol7_id.append(list(array_sol7_ids[array_group7 == i7]))
        sol8_id.append(list(array_sol8_ids[array_group8 == i8]))
        sol9_id.append(list(array_sol9_ids[array_group9 == i9]))


    instance_names = ["X-n439-k37", "X-n502-k39", "X-n449-k29", "ORTEC-n405-k18", "ORTEC-n510-k23", "ORTEC-n455-k41", "ORTEC-VRPTW-ASYM-0bdff870-d1-n458-k35", "R2_8_9", 'RC2_10_5']

    pool_iterable = [(1, ["X-n439-k37"], sol1[:1], sol1_id[:1]), (2, ["X-n502-k39"], sol2[:1], sol2_id[:1]), (3, ["X-n449-k29"], sol3[:1], sol3_id[:1]),(4, [ "ORTEC-n405-k18"], sol4[:1], sol4_id[:1]),(5, ["ORTEC-n510-k23"], sol5[:1], sol5_id[:1]),(6, ["ORTEC-n455-k41"], sol6[:1], sol6_id[:1]), (7, ["ORTEC-VRPTW-ASYM-0bdff870-d1-n458-k35"], sol7[:1], sol7_id[:1]),(8, ["R2_8_9"], sol8[:1], sol8_id[:1]),(9, ['RC2_10_5'], sol9[:1], sol9_id[:1]), (11, ["X-n439-k37"], sol1[1:2], sol1_id[1:2]), (21, ["X-n502-k39"], sol2[1:2], sol2_id[1:2]), (31, ["X-n449-k29"], sol3[1:2], sol3_id[1:2]),(41, [ "ORTEC-n405-k18"], sol4[1:2], sol4_id[1:2]),(51, ["ORTEC-n510-k23"], sol5[1:2], sol5_id[1:2]),(61, ["ORTEC-n455-k41"], sol6[1:2], sol6_id[1:2]), (71, ["ORTEC-VRPTW-ASYM-0bdff870-d1-n458-k35"], sol7[1:2], sol7_id[1:2]), (81, ["R2_8_9"], sol8[1:2], sol8_id[1:2]), (91, ['RC2_10_5'], sol9[1:2], sol9_id[1:2])]

    with Pool() as pool:
        iter_batches = pool.starmap(main_full, pool_iterable)

        for iter_batch in iter_batches:
            print(iter_batch)

    """
    pool_iterable = []
    for i in range(array_group1.max()):
        temp_ids = []
        temp_sols = []

        i1, i2, i3, i4, i5, i6, i7, i8, i9 = indexSampler.sample_index()

        temp_sols.append(list(array_sol1[array_group1 == i1]))
        temp_sols.append(list(array_sol2[array_group2 == i2]))
        temp_sols.append(list(array_sol3[array_group3 == i3]))
        temp_sols.append(list(array_sol4[array_group4 == i4]))
        temp_sols.append(list(array_sol5[array_group5 == i5]))
        temp_sols.append(list(array_sol6[array_group6 == i6]))
        temp_sols.append(list(array_sol7[array_group7 == i7]))
        temp_sols.append(list(array_sol8[array_group8 == i8]))
        temp_sols.append(list(array_sol9[array_group9 == i9]))

        temp_ids.append(list(array_sol1_ids[array_group1 == i1]))
        temp_ids.append(list(array_sol2_ids[array_group2 == i2]))
        temp_ids.append(list(array_sol3_ids[array_group3 == i3]))
        temp_ids.append(list(array_sol4_ids[array_group4 == i4]))
        temp_ids.append(list(array_sol5_ids[array_group5 == i5]))
        temp_ids.append(list(array_sol6_ids[array_group6 == i6]))
        temp_ids.append(list(array_sol7_ids[array_group7 == i7]))
        temp_ids.append(list(array_sol8_ids[array_group8 == i8]))
        temp_ids.append(list(array_sol9_ids[array_group9 == i9]))


        pool_iterable.append((i, instance_names, temp_sols, temp_ids))"""




