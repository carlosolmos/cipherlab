import streamlit as st
from cryptography.common import *
from cryptography.generalsubstitution import *

st.header("General substitution cipher with nulls")

st.markdown("""
The monoalphabetic substitution ciphers dominated the world of cryptography for centuries until \
the Arabs invented the science of cryptanalysis -circa the ninth century- thanks to their mastery \
of mathematics, statistics, and linguistics. Arab scientist al-Kindi wrote about the use of \
**Frequency Analysis** to decipher secrets encoded with monoalphabetic substitution ciphers. Much \
later, in the 16th century, European scholars and cryptoanalysts in France and Venice would \
consolidate the frequency analysis techniques.
European cryptographers made some efforts to increase the security of substitution ciphers. \

One of the earliest improvements was the introduction of ***nulls***: characters or symbols \
representing nothing.

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
A random sequence of the characters in the plain alphabet, plus a set of *nulls* to obfuscate the cipher.
""")

nulls_set = st.text_input('Enter your nulls separated by comma, for example:', '%,#')

cipher_alphabet = gs_generate_cipher_with_nulls(nulls_set, pa)

st.markdown(':blue[Key (cipher alphabet):] {}'.format(cipher_alphabet['alphabet']))
st.markdown(':blue[Nulls:] {}'.format(cipher_alphabet['nulls']))

st.markdown("""
### 3. The encryption algorithm
1. Substitute each character in the message for the corresponding position in the cipher alphabet. 
2. Add some null characters at random positions.
3. To decipher the message, reverse the process switching the alphabets and ignoring the nulls.

We will reuse the function *cipher_substitution(...)* from the general substitution cipher.
""")
snippet = '''
def cipher_substitution_with_nulls(message: str, message_alphabet: list, cipher_alphabet: list, nulls_set: list):
    random.seed()
    output = ""
    if len(message) == 0:
        return output
    message = message.lower()
    first_stage = cipher_substitution(message, message_alphabet, cipher_alphabet)
    first_stage_len = len(first_stage)
    null_positions = []
    if len(nulls_set) > 0:
        # add a percentage of nulls, but at least 4
        nulls_count = round(first_stage_len * .20)
        if nulls_count < 4:
            nulls_count = 4
        # add nulls at random positions
        null_positions = random.sample(range(0, first_stage_len - 1), nulls_count)
    position = 0
    for c in first_stage:
        if position in null_positions:
            n = random.sample(nulls_set, 1)
            output += n[0]
        output += c
        position += 1
    return output


def decipher_substitution_with_nulls(message: str, message_alphabet: list, cipher_alphabet: list, nulls_set: list):
    output = ""
    if len(message) == 0:
        return output
    message = message.lower()
    first_stage = cipher_substitution(message, message_alphabet, cipher_alphabet)
    for c in first_stage:
        if c not in nulls_set:
            output += c
    return output

'''

st.code(snippet)

st.markdown("""### 4. Let's encrypt a message to test the algorithm""")

message = st.text_input('Enter your message:', '')
ciphertext = cipher_substitution_with_nulls(message, plain_alphabet, cipher_alphabet['alphabet'],
                                            cipher_alphabet['nulls'])
deciphered = decipher_substitution_with_nulls(ciphertext, cipher_alphabet['alphabet'], plain_alphabet,
                                              cipher_alphabet['nulls'])

st.markdown(":blue[plaintext:]\t{}".format(message))
st.markdown(":blue[ciphertext:]\t:red[*{}*]".format(ciphertext))
st.write(":blue[deciphered text]:\t{}".format(deciphered))

st.markdown("""
---
#### References:

[1] Singh, Simon, The Code Book: The Science of Secrecy From Ancient Egypt to Quantum Cryptography. New York, Anchor Books, 2000. Singh, Simon. The Code Book: The Science of Secrecy From Ancient Egypt to Quantum Cryptography.
""")
