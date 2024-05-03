import random

R1 = [(i, 5) for i in range(1, 1001)]

R11 = [(i, 7) for i in range(1001, 2001)]

R1.append(R11)
R1.append((2001, 2002))

R2 = [(5, j) for j in range(1, 1001)]
R22 = [(7, j) for j in range(1001, 2001)]
R2.append(R22)
R2.append((2002, 8))

import numpy as np

x_values = np.random.randint(2002, 3001, size=2000)
y_values = np.random.randint(1, 3001, size=2000)
R3 = list(zip(x_values, y_values))

R3.append((8, 30))

np.random.shuffle(R3)


print(R1)
print(R2)
print(R3)