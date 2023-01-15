
def cc_generate_cipher(alphabet: list, n_shift_positions: int):
    cipher = []
    alphabet_len = len(alphabet)
    for p in range(alphabet_len):
        c = (p + n_shift_positions) % alphabet_len
        cipher.append(alphabet[c])
    return cipher
