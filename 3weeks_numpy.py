import numpy as np


def get_L2_norm(array):
    norm = [val ** 2 for val in array]
    return np.sqrt(sum(norm))


def is_singular(array):
    if np.linalg.det(array):
        return False
    return True


mat = np.array([1, 3, 1])
print(get_L2_norm(mat))

mat_2 = np.array([[1, -1], [-1, 1]])
print(is_singular(mat_2))