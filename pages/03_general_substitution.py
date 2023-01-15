import streamlit as st
from cryptography.common import *
from cryptography.generalsubstitution import *

st.header("General substitution cipher")

st.markdown("""
The strength of a cipher system depends on keeping the *key* secret and on having a wide range of potential keys [1].
The Caesar Cipher is not very strong because it only has 25 possible keys (shift positions) but if instead we allow for any
possible combination of the plain alphabet, then we would have an immense set of keys:

  *P(n,r) = P(26,26) = 403291461126605635584000000*
  
## Implementation
    
### 1. The Plain Alphabet

We establish the valid plain alphabet. Let's take, for example, the 26 letters in the english 
language alphabet.
""")

# alphabet
plain_alphabet = generate_alphabet()
pa = [char for char in plain_alphabet]
st.markdown(':blue[Plain alphabet:] {}'.format(pa))

st.markdown("""
### 2. The Key
A random sequence of the characters in the plain alphabet 
""")

cipher_alphabet = gs_generate_cipher(pa)

if st.button('Push to re-generate the Key'):
    cipher_alphabet = gs_generate_cipher(pa)

st.markdown(':blue[Key (cipher alphabet):] {}'.format(cipher_alphabet))

st.markdown("""
### 3. The encryption algorithm
Substitute each character in the message for the corresponding position in the cipher alphabet.
""")
snippet = '''
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
'''
st.code(snippet)

st.markdown("""### 4. Let's encrypt a message to test the algorithm""")

message = st.text_input('Enter your message', '')
ciphertext = cipher_substitution(message, plain_alphabet, cipher_alphabet)
decipheredtext = cipher_substitution(ciphertext, cipher_alphabet, plain_alphabet)

st.markdown(":blue[plaintext:]\t{}".format(message))
st.markdown(":blue[ciphertext:]\t:red[*{}*]".format(ciphertext))

st.markdown(
    """
    To decipher the message we simply have to reverse the process switching the alphabets.
    """
)
st.write(":blue[deciphered text]:\t{}".format(decipheredtext))


st.markdown("""
---
#### References:

[1] Singh, Simon, The Code Book: The Science of Secrecy From Ancient Egypt to Quantum Cryptography. New York, Anchor Books, 2000. Singh, Simon. The Code Book: The Science of Secrecy From Ancient Egypt to Quantum Cryptography.
""")

