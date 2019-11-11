import numpy as np

# key should be a numpy array
def mod_inv(key):
    '''
    Modular inverse. Only for mod 31.

    Arguments:
        key: a 2-D numpy array

    Return:
        modinv: modular inverse of key
    '''
    det = int(round(np.linalg.det(key)))    # determinant of key
    adj = np.linalg.inv(key) * det          # adjugate matrix of key
    assert det % 31 != 0
    moddet = np.mod(det ** 29, 31)          # Fermat's Little Theorem
    modinv = np.around(np.mod(adj * moddet, 31)).astype(int)
    return modinv
