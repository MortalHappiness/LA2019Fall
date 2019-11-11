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

def decode(cipher, key):
    '''
    Decode cipher with public key.

    Arguments:
        cipher: str, cipher text
        key: str, public key

    Return:
        plain: str, plain text
    '''
    cipher_matrix = text_to_matrix(cipher)
    public_key = np.array([int(x) for x in key.split()]).reshape(3, 3)
    private_key = mod_inv(public_key)
    decode_matrix = np.mod(np.dot(private_key, cipher_matrix), 31)
    plain = matrix_to_text(decode_matrix)

    return plain
