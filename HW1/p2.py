import numpy as np

def p2_has_cycle(sets):
    # TODO
    # return True if the graph has cycle; return False if not
    '''
      HINT: You can `print(sets)` to show what the matrix looks like
        If we have a directed graph with 2->3 4->1 3->5 5->2 0->1
               0  1  2  3  4  5
            0  0  1  0  0  0  0
            1  0  0  0  0  0  0
            2  0  0  0  1  0  0
            3  0  0  0  0  0  1
            4  0  1  0  0  0  0
            5  0  0  1  0  0  0
        The size of the matrix is (6,6)
    '''
    matrix = np.array(sets)
    n_row, n_col = matrix.shape

    for _ in range(n_row):
        matrix = np.dot(matrix, matrix)

        # check the diagonal for cycle
        for i in range(n_row):
            if matrix[i][i] >= 1:
                return True

    return False
