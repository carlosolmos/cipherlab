import streamlit as st
from cryptography.common import *
from cryptography.generalsubstitution import *

st.header("General substitution with Keyword cipher")

"""
A long random key provides robust security for substitution ciphers. However, a key that is easier \
to remember and avoids misunderstandings could be a better option. If we are willing to have a \
smaller number of potential keys, we can use a simple keyword or key phrase as the basis of the key.

## Implementation
    
### 1. The Plain Alphabet

We establish the valid plain alphabet. Let's take, for example, the 26 letters in the english 
language alphabet.
"""

# alphabet
plain_alphabet = generate_alphabet()
pa = [char for char in plain_alphabet]
st.markdown(':blue[Plain alphabet:] {}'.format(pa))

st.markdown("""
### 2. The Key
* Start with an alphabetic keyword or key phrase. Ideally something simple, easy to remember.
* Remove all characters not present in the plain alphabet -like spaces- and repeated letters.
* Follow the keyword with the remaining letters of the alphabet in order, beginning with the last letter of the keyword.  
""")
keyword = st.text_input('Enter your keyword or key phrase (max 26 letters)', '')
cipher_alphabet = gs_generate_cipher_with_keyword(keyword, pa)

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
deciphered = cipher_substitution(ciphertext, cipher_alphabet, plain_alphabet)

st.markdown(":blue[plaintext:]\t{}".format(message))
st.markdown(":blue[ciphertext:]\t:red[*{}*]".format(ciphertext))

st.markdown(
    """
    To decipher the message we simply have to reverse the process switching the alphabets.
    """
)
st.write(":blue[deciphered text]:\t{}".format(deciphered))


st.markdown("""
---
#### References:

[1] Singh, Simon, The Code Book: The Science of Secrecy From Ancient Egypt to Quantum Cryptography. New York, Anchor Books, 2000. Singh, Simon. The Code Book: The Science of Secrecy From Ancient Egypt to Quantum Cryptography.
""")
