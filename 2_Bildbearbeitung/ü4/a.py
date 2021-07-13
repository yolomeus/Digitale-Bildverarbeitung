import numpy as np

f_a = np.array([[0, 0, 0],
                [1, 4, 1],
                [0, 0, 0]])

f_b = np.array([[0, -1, 0],
                [0, 0, 0],
                [0, 1, 0]])

# original filter
f = f_b @ f_a
print(f)
