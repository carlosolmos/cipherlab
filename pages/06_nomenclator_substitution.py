import streamlit as st
from cryptography.common import *
from cryptography.generalsubstitution import *

st.header("Nomenclator - Monoalphabetic substitution cipher with codes")

st.markdown("""
Another improvement to the monoalphabetic substitution cipher consisted of the inclusion \
of codes or codewords. A code is a substitution at the level of words. The combination \
of a cipher alphabet with a set of codewords is known as ***Nomenclator***. With a nomenclator,  \
the cipher alphabet encrypts most of the message except for the codewords. While adding \
codewords increases the complexity of the cipher text, it does not increase the overall \
strength of the encryption, which is still vulnerable to frequency analysis.

## Implementation
    
### 1. The Plain Alphabet

We establish the valid plain alphabet. Let's take, for example, the 26 letters in the english 
language alphabet.
""")

# alphabet
plain_alphabet = generate_alphabet()
pa = [char for char in plain_alphabet]
st.markdown(':blue[Plain alphabet:] {}'.format(pa))

# codes
st.markdown("""
### 2. The Key
A Nomenclator relies on a cipher alphabet and a set of codewords. The cipher alphabet is created using \
the usual technique of scrambling the plain alphabet. The codewords are defined in advanced using numbers or symbols. 
""")

st.markdown('Define the codes as code=value pairs separated by commas. We can use special characters, numbers, \
even emojis!.')
code_set = st.text_input('Enter your codewords:', 'everything=42,friend=:wolf:,document=#')
st.markdown('> For a list of valid emoji codes refer to: https://github.com/markdown-templates/markdown-emojis')

cipher_alphabet = gs_generate_nomenclator(code_set, pa)

st.markdown("**The Nomenclator**")
st.markdown(':blue[Cipher alphabet:] {}'.format(cipher_alphabet['alphabet']))
st.markdown(':blue[Codewords:] {}'.format(cipher_alphabet['codewords']))

st.markdown("""
### 3. The encryption algorithm
1. Substitute the special words for their codeword
1. Substitute each remaining character in the message for the corresponding position in the cipher alphabet. 
3. To decipher the message, reverse the process switching the alphabets and replacing the codewords.

We will reuse the function *cipher_substitution(...)* from the general substitution cipher.
""")
snippet = '''
def cipher_substitution_with_codes(message: str, message_alphabet: list, cipher_alphabet: list, codewords: dict):
    random.seed()
    output = ""
    if len(message) == 0:
        return output
    message = message.lower()
    # split message in words
    words = message.split(' ')
    for i, w in enumerate(words):
        # if we have a code for the word, replace it.
        # else use the regular cipher
        if w in codewords:
            words[i] = codewords[w]
        else:
            words[i] = cipher_substitution(w, message_alphabet, cipher_alphabet)
    output = ' '.join(words)
    return output


def decipher_substitution_with_codes(message: str, cipher_alphabet: list, message_alphabet: list, codewords: dict):
    output = ""
    if len(message) == 0:
        return output
    message = message.lower()
    # reverse the codeword dict
    decoder = dict()
    for key, value in codewords.items():
        decoder[value]=key
    # split message in words
    words = message.split(' ')
    for i, w in enumerate(words):
        # if we have a codeword replace it.
        # else use the regular cipher
        if w in decoder:
            words[i] = decoder[w]
        else:
            words[i] = cipher_substitution(w, cipher_alphabet, message_alphabet)
    output = ' '.join(words)
    return output

'''
st.code(snippet)

st.markdown("""### 4. Let's encrypt a message to test the algorithm""")

message = st.text_input('Enter your message (include some of the special words):', 'send document to friend')

ciphertext = cipher_substitution_with_codes(message, plain_alphabet, cipher_alphabet['alphabet'],
                                            cipher_alphabet['codewords'])

deciphered = decipher_substitution_with_codes(ciphertext, cipher_alphabet['alphabet'], plain_alphabet,
                                              cipher_alphabet['codewords'])

st.markdown(":blue[plaintext:]\t{}".format(message))
st.markdown(":blue[ciphertext:]\t:red[*{}*]".format(ciphertext))
st.write(":blue[deciphered text]:\t{}".format(deciphered))

st.markdown("""
---
#### References:

[1] Singh, Simon, The Code Book: The Science of Secrecy From Ancient Egypt to Quantum Cryptography. New York, Anchor Books, 2000. Singh, Simon. The Code Book: The Science of Secrecy From Ancient Egypt to Quantum Cryptography.
""")
