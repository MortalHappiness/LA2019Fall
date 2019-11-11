import numpy as np
from util import mod_inv

# ==============================

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.,?!'

# ==============================

def text_to_matrix(text):
    while len(text) % 3 != 0:
        text += text[-1]
    text = [LETTERS.index(i) for i in text]
    text = np.reshape(text, (-1, 3)).T
    return text

def matrix_to_text(matrix):
    return ''.join([LETTERS[x] for x in matrix.T.flatten()])

def get_key(cipher, plain):
    '''
    Calculate public key with cipher text and plain text.

    Arguments:
        cipher: str, cipher text
        plain: str, plain text

    Return:
        key: str, public key
    '''
    cipher = text_to_matrix(cipher[:9])
    plain = text_to_matrix(plain[:9])
    public_key = np.mod(np.dot(cipher, mod_inv(plain)), 31)

    key = ' '.join([str(x) for x in public_key.flatten()])
    return key

