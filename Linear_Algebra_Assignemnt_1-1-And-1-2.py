from scipy.linalg import norm
import numpy as np


def norms_for_vectors():
    arr = np.array([6, 8, -7])
    print(arr)
    norm_l1 = norm(arr, 1)
    print("L1 norm: ", norm_l1)
    print("====================================")
    print("L2 norm for:", arr)
    norm_l2 = norm(arr)
    print("L2 norm:", norm_l2)
    print("====================================")
    print("L-infinity norm for :", arr)
    norm_l_infinity = max(abs(arr))
    print("L-infinity norm:", norm_l_infinity)


norms_for_vectors()


def inner_product():
    x = np.array([6, 8, -7])
    y = np.array([-1, 0, 1])

    # Display the vectors
    print("Vector x...\n", x)
    print("\nVector y...\n", y)

    # To get the Inner product of two arrays, use the numpy.inner() method in Python
    print("\nResult (Inner Product)...\n", np.inner(x, y))


inner_product()


def outer_product():
    x = np.array([6, 8, -7])
    y = np.array([-1, 0, 1])

    # Display the vectors
    print("Vector x...\n", x)
    print("\nVector y...\n", y)

    # To get the Inner product of two arrays, use the numpy.inner() method in Python
    print("\nResult (Outer Product)...\n", np.outer(x, y))


outer_product()
