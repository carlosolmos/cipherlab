import streamlit as st
from cryptography.common import *
from cryptography.caesarcipher import *

st.header("Caesar cipher")

st.markdown("""
Julius Caesar used different techniques for secret writing. One of his known substitution ciphers consists 
of shifting the letters in the alphabet a constant number of positions. Each letter in a plain message is 
replaced by the letter that is, say, 3 positions ahead in the alphabet.

## Implementation
    
### 1. The Plain Alphabet

We establish the valid plain alphabet. Let's take, for example, the 26 letters in the english 
language alphabet.

""")

# alphabet
plain_alphabet = generate_alphabet()
pa = [char for char in plain_alphabet]
st.markdown(':blue[plain alphabet:] {}'.format(pa))

st.markdown("""
### 2. The Cypher Alphabet
The cypher alphabet shifts each character by 3 positions.
""")

snippet = '''
def cc_generate_cipher(alphabet, cc_shift_positions):
    cipher = []
    alphabet_len = len(alphabet)
    for p in range(alphabet_len):
        c = (p + cc_shift_positions) % alphabet_len
        cipher.append(alphabet[c])
    return cipher
'''
st.code(snippet)

cipher_alphabet = cc_generate_cipher(pa, 3)
st.markdown(':blue[cypher alphabet:] {}'.format(cipher_alphabet))

st.markdown("""
### 3. The encryption algorithm
Substitute each character in the message for the corresponding position in the cipher alphabet.
""")
snippet = '''
def cipher_caesar_shift(message, message_alphabet, cipher_alphabet):
    output = ""
    for p in message:
        if p in message_alphabet:
            inx = message_alphabet.index(p)
            output += cipher_alphabet[inx]
        else:
            output += p
    return output
'''
st.code(snippet)

st.markdown("""### 4. Let's encrypt a message to test the algorithm""")

message = st.text_input('Enter your message', '')
ciphertext = cipher_caesar_shift(message, plain_alphabet, cipher_alphabet)
decipheredtext = cipher_caesar_shift(message, plain_alphabet, plain_alphabet)

st.markdown(":blue[plaintext:]\t{}".format(message))
st.markdown(":blue[ciphertext:]\t:red[*{}*]".format(ciphertext))

st.markdown(
    """
    To decipher the message we simply have to reverse the process with the plain alphabet.
    """
)
st.write(":blue[deciphered text]:\t{}".format(decipheredtext))


st.markdown("""
---
#### References:

[1] Singh, Simon, The Code Book: The Science of Secrecy From Ancient Egypt to Quantum Cryptography. New York, Anchor Books, 2000. Singh, Simon. The Code Book: The Science of Secrecy From Ancient Egypt to Quantum Cryptography.
""")
