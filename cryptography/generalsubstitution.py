import random


def gs_generate_cipher(alphabet: list):
    random.seed()
    return random.sample(alphabet, len(alphabet))


def gs_generate_cipher_with_keyword(keyword: str, alphabet: list):
    cipher_alphabet = []
    if len(keyword) == 0:
        return cipher_alphabet
    if len(keyword) > 26:
        keyword = keyword[0:25]

    # first the clean keyword
    keyword = keyword.lower()
    for c in keyword:
        if c in alphabet and c not in cipher_alphabet:
            cipher_alphabet.append(c)
    # add the remaining letters of the alphabet from the last letter of the keyword
    keyword_len = len(cipher_alphabet)
    letter_inx = alphabet.index(cipher_alphabet[keyword_len - 1])
    alphabet_len = len(alphabet)
    for i in range(alphabet_len):
        c = alphabet[letter_inx]
        if c not in cipher_alphabet:
            cipher_alphabet.append(c)
        letter_inx = (letter_inx + 1) % alphabet_len
    return cipher_alphabet
