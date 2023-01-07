import string
import random

def CipherMlecchitaVikalpa(input, alphabet, cipherSet1, cipherSet2):
    output = ""
    for p in input:
        if p in alphabet:  # any non-alphabethic character will be lost
            inx = -1
            c = ""
            if p in cipherSet1:
                inx = cipherSet1.index(p)
                c = cipherSet2[inx]
            else:
                inx = cipherSet2.index(p)
                c = cipherSet1[inx]
            output += c

    return output

def GenerateAlphabet():
    return string.ascii_lowercase


def GenerateCipherSets(alphabet):
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