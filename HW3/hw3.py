import sys
import numpy as np

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ======================================

def plot_wave(x, path = './wave.png'):
    plt.gcf().clear()
    plt.plot(x)
    plt.xlabel('n')
    plt.ylabel('xn')
    plt.savefig(path)

def plot_ak(a, path = './freq.png'):
    plt.gcf().clear()

    # Only plot the mag of a
    a = np.abs(a)
    plt.plot(a)
    plt.xlabel('k')
    plt.ylabel('ak')
    plt.savefig(path)

def CosineTrans(x, B):
    # implement cosine transform
    return np.dot(np.linalg.inv(B), x)

def InvCosineTrans(a, B):
    # implement inverse cosine transform
    return np.dot(B, a)

def gen_basis(N):
    assert N >= 2
    # b0
    b0 = np.array([1/(N**0.5)] * N).reshape(1, -1)
    # b1 ~
    L = list()
    for i in range(1, N):
        L.append((np.arange(N) + 0.5) * i)
    L = np.array(L)
    L = ((2 / N) ** 0.5) * np.cos(L * np.pi / N)

    basis = np.concatenate((b0, L), axis = 0).T

    return basis

def main(signal_path):
    N = 1000
    x = np.loadtxt(signal_path)
    B = gen_basis(N)
    a = CosineTrans(x, B)
    n_largest_freq = np.sort(np.argsort(a)[-5:])
    f1 = n_largest_freq[0]
    f3 = n_largest_freq[2]
    f1_wave = np.cos(np.arange(N) * f1 * np.pi / N)
    f3_wave = np.cos(np.arange(N) * f3 * np.pi / N)
    np.savetxt("b07901069_f1.txt", f1_wave)
    np.savetxt("b07901069_f3.txt", f3_wave)
    plot_ak(a, "./b07901069_freq.png")

# ==================================

if __name__ == '__main__':
    signal_path = sys.argv[1]
    main(signal_path)
