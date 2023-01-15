import string
import random


def generate_alphabet():
    return string.ascii_lowercase


def cipher_substitution(message: str, message_alphabet: list, cipher_alphabet: list):
    output = ""
    if len(message) == 0:
        return output
    message = message.lower()
    for p in message:
        if p in message_alphabet:
            inx = message_alphabet.index(p)
            output += cipher_alphabet[inx]
        else:
            output += p
    return output


def cipher_substitution_with_nulls(message: str, message_alphabet: list, cipher_alphabet: list, nulls_set: list):
    random.seed()
    output = ""
    if len(message) == 0:
        return output
    message = message.lower()
    first_stage = cipher_substitution(message, message_alphabet, cipher_alphabet)
    first_stage_len = len(first_stage)
    null_positions = []
    if len(nulls_set) > 0:
        # add a percentage of nulls, but at least 4
        nulls_count = round(first_stage_len * .20)
        if nulls_count < 4:
            nulls_count = 4
        # add nulls at random positions
        null_positions = random.sample(range(0, first_stage_len - 1), nulls_count)
    position = 0
    for c in first_stage:
        if position in null_positions:
            n = random.sample(nulls_set, 1)
            output += n[0]
        output += c
        position += 1
    return output


def decipher_substitution_with_nulls(message: str, cipher_alphabet: list, message_alphabet: list, nulls_set: list):
    output = ""
    if len(message) == 0:
        return output
    message = message.lower()
    first_stage = cipher_substitution(message, cipher_alphabet, message_alphabet)
    for c in first_stage:
        if c not in nulls_set:
            output += c
    return output


def cipher_substitution_with_codes(message: str, message_alphabet: list, cipher_alphabet: list, codewords: dict):
    random.seed()
    output = ""
    if len(message) == 0:
        return output
    message = message.lower()
    # split message in words
    words = message.split(' ')
    for i, w in enumerate(words):
        # if we have a code for the word, replace it.
        # else use the regular cipher
        if w in codewords:
            words[i] = codewords[w]
        else:
            words[i] = cipher_substitution(w, message_alphabet, cipher_alphabet)
    output = ' '.join(words)
    return output


def decipher_substitution_with_codes(message: str, cipher_alphabet: list, message_alphabet: list, codewords: dict):
    output = ""
    if len(message) == 0:
        return output
    message = message.lower()
    # reverse the codeword dict
    decoder = dict()
    for key, value in codewords.items():
        decoder[value]=key
    # split message in words
    words = message.split(' ')
    for i, w in enumerate(words):
        # if we have a codeword replace it.
        # else use the regular cipher
        if w in decoder:
            words[i] = decoder[w]
        else:
            words[i] = cipher_substitution(w, cipher_alphabet, message_alphabet)
    output = ' '.join(words)
    return output

