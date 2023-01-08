


def cc_generate_cipher(alphabet, cc_shift_positions):
    cipher = []
    alphabet_len = len(alphabet)
    for p in range(alphabet_len):
        c = (p + cc_shift_positions) % alphabet_len
        cipher.append(alphabet[c])
    return cipher


def cipher_caesar_shift(message, message_alphabet, cipher_alphabet):
    output = ""
    for p in message:
        if p in message_alphabet:
            inx = message_alphabet.index(p)
            output += cipher_alphabet[inx]
        else:
            output += p
    return output
