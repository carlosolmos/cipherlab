"""
The Code Book - p9

The Kama-Sutra recommends that women should study 64 arts. The number 45 is the "Art of Secret Writing" or "mlecchita-vikalpa".

The methods used are substituion ciphers.

One of the recommended thecniques -according to the book- is to randomly pair letters of the alphabet, and then replace each letter in the plain text message with its pair in the cipher.

"""

import random
import string
random.seed()


# alphabet of 26 letters
alphabet = string.ascii_lowercase #+ string.digits
print(alphabet)

# select half of the random characters
setLen=int(len(alphabet)/2)
set1 = random.sample(alphabet,k=setLen)
print(set1)

# pair them
set2=[]
for l in alphabet:
    if l not in set1:
        set2.append(l)    
print(set2)



def mlecchita(input):
    global alphabet
    global set1
    global set2
    output=""
    for p in input:
        if p in alphabet:  #any non-alphabethic character will be lost
            inx=-1
            c=""
            if p in set1:
                inx = set1.index(p)
                c=set2[inx]
            else:
                inx = set2.index(p)
                c=set1[inx]
            output += c
    
    return output


plaintext="hola cipher"
print(plaintext)

ciphertext = mlecchita(plaintext)
print(ciphertext)

deciphertext=mlecchita(ciphertext)
print(deciphertext)
