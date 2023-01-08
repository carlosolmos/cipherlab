import string


def generate_alphabet():
    return string.ascii_lowercase


def cipher_substitution(message, message_alphabet, cipher_alphabet):
    output = ""
    for p in message:
        if p in message_alphabet:
            inx = message_alphabet.index(p)
            output += cipher_alphabet[inx]
        else:
            output += p
    return output