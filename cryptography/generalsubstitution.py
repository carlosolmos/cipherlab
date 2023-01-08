import random


def gs_generate_cipher(alphabet):
    random.seed()
    return random.sample(alphabet, len(alphabet))
