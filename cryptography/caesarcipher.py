


def cc_generate_cipher(alphabet, n_shift_positions):
    cipher = []
    alphabet_len = len(alphabet)
    for p in range(alphabet_len):
        c = (p + n_shift_positions) % alphabet_len
        cipher.append(alphabet[c])
    return cipher



