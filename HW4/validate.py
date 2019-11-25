# calculate the difference between two files(matrices)

import sys
import numpy as np

# ===============================

matrix1 = np.loadtxt(sys.argv[1])
matrix2 = np.loadtxt(sys.argv[2])
diff = np.sum(np.abs(matrix1 - matrix2).ravel(), axis = 0)

print('Difference: %f' % diff)
