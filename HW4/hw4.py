import sys
import numpy as np
import pandas as pd

# ===================================

def load(fname):
    f = open(fname, 'r').readlines()
    n = len(f)
    ret = {}
    for l in f:
        l = l.split('\n')[0].split(',')
        i = int(l[0])
        ret[i] = {}
        for j in range(n):
            if str(j) in l[1:]:
                ret[i][j] = 1
            else:
                ret[i][j] = 0
    ret = pd.DataFrame(ret).values
    return ret

def get_tran(g):
    column_sum = np.sum(g, axis = 0)
    # avoid divided by zero
    dividend = np.where(column_sum == 0, 1, column_sum)
    return g / dividend

def cal_rank(t, d = 0.85, max_iterations = 1000, alpha = 0.001):
    # If the transition matrix contains zero columns,
    # make the column be all 1/n.
    n = t.shape[0]
    column_sum = np.sum(t, axis = 0)
    for i, x in enumerate(column_sum):
        if x == 0:
            t[:, i] += (1/n)

    # prepare the (1-d)/N vector for each iteration
    rand_surf_vec = np.array([(1-d)/n] * n)

    # initialize the transition vector
    trans_vec = np.array([1/n] * n)

    for _ in range(max_iterations):
        new_trans_vec = d * np.dot(t, trans_vec) + rand_surf_vec
        if dist(trans_vec, new_trans_vec) <= alpha:
            break
        trans_vec = new_trans_vec

    # get the first ten most important nodes
    ans = np.argsort(trans_vec)[-1:-11:-1].astype(int)

    return ans

def save(t, r):
    np.savetxt('1.txt', t)
    np.savetxt('2.txt', r, fmt = '%d')

def dist(a, b):
    return np.sum(np.abs(a-b))

def main():
    graph = load(sys.argv[1])
    transition_matrix = get_tran(graph)
    rank = cal_rank(transition_matrix)
    save(transition_matrix, rank)

# ====================================

if __name__ == '__main__':
    main()
