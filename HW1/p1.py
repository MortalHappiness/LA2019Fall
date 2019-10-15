import numpy as np

def p1_has_cycle(sets):
    # TODO
    # return True if the graph has cycle; return False if not
    '''
      HINT: You can `print(sets)` to show what the matrix looks like
        If we have a directed graph with 2->3 4->1 3->5 5->2 0->1
               0  1  2  3  4  5
            0  0  0 -1  1  0  0
            1  0  1  0  0 -1  0
            2  0  0  0 -1  0  1
            3  0  0  1  0  0 -1
            4 -1  1  0  0  0  0
        The size of the matrix is (5,6)
    '''
    matrix = np.array(sets)
    n_row, n_col = matrix.shape

    for _ in range(n_row):
        # find the position of 1 in the first row
        col_idx = -1
        for i in range(n_col):
            if matrix[0][i] == 1:
                col_idx = i
                break
        if col_idx == -1:
            raise Exception("Something wrong!")

        # do row additions
        new_rows = list()
        for row in matrix[1:]:
            if row[col_idx] == -1:
                new_row = matrix[0] + row
                # check whether the new row is all zeros
                if not np.any(new_row):
                    return True
                new_rows.append(new_row)

        # concatenate new rows with original matrix
        if new_rows:
            new_rows = np.array(new_rows)
            matrix = np.concatenate((matrix, new_rows), axis = 0)

        # discard the first row
        matrix = matrix[1:]

    return False
