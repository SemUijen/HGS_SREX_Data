
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
for i in range(6 ,8):
    i1, i2, i3, i4, i5, i6, i7, i8, i9 = i ,i ,i ,i ,i ,i ,i ,i ,i
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

pool_iterable = [(12, ["X-n439-k37"], sol1[:1], sol1_id[:1]), (22, ["X-n502-k39"], sol2[:1], sol2_id[:1]), (32, ["X-n449-k29"], sol3[:1], sol3_id[:1]) ,(42, [ "ORTEC-n405-k18"], sol4[:1], sol4_id[:1])
                 ,(52, ["ORTEC-n510-k23"], sol5[:1], sol5_id[:1]) ,(62, ["ORTEC-n455-k41"], sol6[:1], sol6_id[:1]), (72, ["ORTEC-VRPTW-ASYM-0bdff870-d1-n458-k35"], sol7[:1], sol7_id[:1])
                 ,(82, ["R2_8_9"], sol8[:1], sol8_id[:1]) ,(92, ['RC2_10_5'], sol9[:1], sol9_id[:1]), (112, ["X-n439-k37"], sol1[1:2], sol1_id[1:2]), (212, ["X-n502-k39"], sol2[1:2], sol2_id[1:2]), (312, ["X-n449-k29"], sol3[1:2], sol3_id[1:2]) ,(412, [ "ORTEC-n405-k18"], sol4[1:2], sol4_id[1:2])
                 ,(512, ["ORTEC-n510-k23"], sol5[1:2], sol5_id[1:2]) ,(612, ["ORTEC-n455-k41"], sol6[1:2], sol6_id[1:2]), (712, ["ORTEC-VRPTW-ASYM-0bdff870-d1-n458-k35"], sol7[1:2], sol7_id[1:2]), (812, ["R2_8_9"], sol8[1:2], sol8_id[1:2]), (912, ['RC2_10_5'], sol9[1:2], sol9_id[1:2])]
