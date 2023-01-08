import streamlit as st
from cryptography.mlecchitavikalpa import *
from cryptography.common import *


st.header('mlecchita-vikalpa - the Art of Secret Writing')

st.markdown(
    """
    The “Art of Secret Writing” is the 44th of 64 arts that all people should study to become more attractive. This \
    according to the Kamasutra.[2] \
    The methods for concealing messages taught in the ancient text are different types of substitution and \
    transposition ciphers.
    One of the recommended techniques, according to Simon Singh [1], asks to randomly pair the letters of the alphabet,\
    and then replace each character in the plaintext message with its partner to produce a ciphertext.
    
    ## Implementation
    
    ### 1. The Plain Alphabet
    
    It begins by establishing the valid plain alphabet. Let's take, for example, the 26 letters in the english language alphabet.
    """
)

snippet = '''
alphabet = string.ascii_lowercase
'''
st.code(snippet)

# alphabet
alphabet = generate_alphabet()
st.markdown(':blue[alphabet:] {}'.format(alphabet))

st.markdown(
    """
    ### 2. The Cipher Alphabet
    
    We create the cipher alphabet by dividing the plain alphabet in half to create random pairs in 2 sets \
     of unique characters. 
    
    I used Python's `random.sample()` for this example:
    """
)
snippet = '''
    # select half of the characters in the alphabet randomly in Set #1
    setLen = int(len(alphabet) / 2)
    set1 = random.sample(alphabet, k=setLen)
    # pair them in Set #2 with the remaining letters of the alphabet
    set2 = []
    for l in alphabet:
        if l not in set1:
            set2.append(l)
'''
st.code(snippet)

cipherSets = mv_generate_cipher_sets(alphabet)
st.markdown("""#### Cipher Alphabet 

Each character in Set 1 is paired with a character in Set 2, and vice-versa.""")
st.write(cipherSets[0])
st.write(cipherSets[1])
st.markdown('In this case, the letter *"{}"* is paired with *"{}"*, \
 *"{}"* is paired with *"{}"*, and so on.'.format(cipherSets[0][0],
                                         cipherSets[1][0],
                                         cipherSets[0][1],
                                         cipherSets[1][1]))

st.markdown("""
### 3. The encryption algorithm 

This is a simple cipher that replaces each letter in the message by its partner in the other set. The characters not \
in the alphabet will be lost.""")

snippet = '''
def cipher_mlecchita_vikalpa(message, alphabet, cipherset1, cipherset2):
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
'''
st.code(snippet)

st.markdown("""### 4. Let's encrypt a message to test our algorithm""")

message = st.text_input('Enter your message', '')
ciphertext = cipher_mlecchita_vikalpa(message, alphabet, cipherSets[0], cipherSets[1])
decipheredtext = cipher_mlecchita_vikalpa(ciphertext, alphabet, cipherSets[0], cipherSets[1])

st.markdown(":blue[plaintext:]\t{}".format(message))
st.markdown(":blue[ciphertext:]\t:red[*{}*]".format(ciphertext))

st.markdown(
    """
    To decipher the message we simply repeat the process with the cipher text and the same alphabet sets.
    """
)
st.write(":blue[deciphered text]:\t{}".format(decipheredtext))

st.markdown("""
---
#### References:

[1] Singh, Simon, The Code Book: The Science of Secrecy From Ancient Egypt to Quantum Cryptography. New York, Anchor Books, 2000. Singh, Simon. The Code Book: The Science of Secrecy From Ancient Egypt to Quantum Cryptography.

[2] https://en.wikipedia.org/wiki/Mlecchita_vikalpa
""")
