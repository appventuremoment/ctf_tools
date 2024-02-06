#Finds orthorgonal basis from given basis
#orthorgonal means all vectors in basis are linearly independant, so to visualise it it means they are all not parallel to each other
import numpy as np
#are you orthorgonal because you are a_1v_1 + a_2v_2 + a_3v_3 + ... + a_iv_i = 0, summation of a_i from 1 to i is 0

v = np.array([[4,1,3,-1], [2,1,-3,4], [1,0,-2,7], [6, 2, 9, -5]])
u = [v[0]]
for vi in v[1:]:
    mi = [np.dot(vi, uj) / np.dot(uj, uj) for uj in u]
    u += [vi - sum(mij * uj for (mij, uj) in zip(mi, u))]

print(round(u[3][1], 5))
