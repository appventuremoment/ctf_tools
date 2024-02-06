import numpy as np
def border(n):
    return np.full((n, n), n).view(np.ma.MaskedArray)
    #temp[temp.shape[0]%n or temp.shape[1]%n] = 2

print(border(5))

"""
def top_performers(scores, student_names, subject_index):
    #return np.max(scores, axis=1)
    return scores[]

a = np.array([[[ 65,  90,  95, 100],
        [ 80,  85,  90,  95],
        [ 75,  80,  85,  90]],

       [[ 88,  92,  96, 100],
        [ 82,  86,  90,  94],
        [ 78,  80,  84,  88]]])

b = np.array([['Alice', 'Bob', 'Charlie'],
       ['David', 'Eve', 'Frank']], dtype='<U7')

print(top_performers(a, b, 0))"""