import Crypto
from Crypto.Util import number
from sympy import primitive_root
import random
from Crypto.Cipher import AES

#Diffie Hellman portion

#returns an n-bit prime number
def n_bit_prime(n):
  return number.getPrime(n)

#returns k: the shared secret
def diffie_hellman():

  print("doing Diffie Hellman key exchange")
  
#p is the the n-bit prime number
  p = n_bit_prime(128)

  #find g, primitive root of p
  g = primitive_root(p)

  #Alice's private key
  a = random.randint(1, p-1)
  print("Alice's private key: ", a)

  #Bob's private key
  b = random.randint(1, p-1)
  print("Bob's private key: " , b)

  #Alice's public key
  x = pow(g, a, p)
  print("Alice's public key: ", x)

  #Bob's public key
  y = pow(g, b, p)
  print("Bob's public key: ", y)

  #Alice's secret key
  #using y, Bob's public key
  ka = pow(y, a, p)
  print("Alice's secret key: ", ka)

  #Bob's secret key
  #using x, Alice's public key
  kb = pow(x, b, p)
  print("Bob's secret key: ", kb)

  #storing shared secret
  k = random.choice([ka, kb])
  print("shared key to be used by AES: ", k)

  return k

#using key from Diffie-Hellman to encrypt a message in AES
#using CBC mode for AES

#padding functions based off:
#https://medium.com/bootdotdev/aes-256-cipher-python-cryptography-examples-b877b9d2e45e
def pad(plaintext):

  #each block is 16 bytes
  #because the key is 128 bits
  block_size = 16

  #calculate the padding needed 
  remainder = len(plaintext) % block_size
  padding_needed = block_size - remainder

  #return plaintext concatenated w/ spaces
  #number of spaces determined by padding_needed
  return plaintext + padding_needed * ' '


#removes whitespace from padding
def unpad(plaintext):
  return plaintext.rstrip()

#encrypt with AES
def encrypt(key, plaintext):

  print("Entering AES encryption function")

  #IV is like a salt for the vector
  #must be the same size as the block size
  IV = random.randbytes(16)

  padded_plaintext = pad(plaintext)

  #convert integer key passed in by diffie hellman
  #to a 16-byte string
  #to be useed by AES.new
  key_to_bytes = key.to_bytes(16)
  
  #create cipher
  #algorithm used to encrypt and decrypt the message
  cipher = AES.new(key_to_bytes, AES.MODE_CBC, IV)

  #change plaintext to bytes
  plaintext_to_bytes = padded_plaintext.encode('utf-8')

  #encrypt the plaintext
  ciphertext = cipher.encrypt(plaintext_to_bytes)
  print("ciphertext = ", ciphertext)

  return ciphertext, IV, key_to_bytes


def decrypt(ciphertext, IV, key_to_bytes):

  print("decrypting...")
  
  #create a new cipher for decryption
  #uses all the same info as the cipher from the encryption
  cipher = AES.new(key_to_bytes, AES.MODE_CBC, IV)

  #decrypt the ciphertext
  #turns into plaintext in its byte form
  plaintext_still_bytes = cipher.decrypt(ciphertext)
  padded_plaintext = plaintext_still_bytes.decode('utf-8')
  plaintext = unpad(padded_plaintext)
  print("plaintext = ", plaintext)

  return plaintext

#main
key = diffie_hellman()
print()
ciphertext, IV, key_to_bytes = encrypt(key, input("insert a message to encrypt: "))
print()
decrypt(ciphertext, IV, key_to_bytes)
  
  
  


































