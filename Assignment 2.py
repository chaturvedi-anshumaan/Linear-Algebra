import numpy as np

x = np.array([1, 1])
y = np.array([3, 4])


def gen_projection_matrix(a):
    return np.outer(a, a) / a.dot(a)


def calc_projection(b, proj_matrix):
    return proj_matrix.dot(b.T)


P = gen_projection_matrix(y)
p = calc_projection(x, P)

print("Projection_Matrix: \n", P)
print("Projection: ", p)

