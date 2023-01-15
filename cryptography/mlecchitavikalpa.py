import random


def cipher_mlecchita_vikalpa(message: str, alphabet: list, cipherset1: list, cipherset2: list):
    output = ""
    for p in message:
        if p in alphabet:  # any non-alphabethic character will be lost
            inx = -1
            c = ""
            if p in cipherset1:
                inx = cipherset1.index(p)
                c = cipherset2[inx]
            else:
                inx = cipherset2.index(p)
                c = cipherset1[inx]
            output += c

    return output


def mv_generate_cipher_sets(alphabet: list):
    random.seed()
    # select half of the characters in the alphabet randomly in Set #1
    setLen = int(len(alphabet) / 2)
    set1 = random.sample(alphabet, k=setLen)
    # pair them in Set #2 with the remaining letters of the alphabet
    set2 = []
    for l in alphabet:
        if l not in set1:
            set2.append(l)
    return [set1, set2]
