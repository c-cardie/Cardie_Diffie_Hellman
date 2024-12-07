import Crypto
from Crypto.Util import number
from sympy import primitive_root
import random
from Crypto.Cipher import AES
from hashlib import sha256

#returns an n-bit prime number
def n_bit_prime(n):
  return number.getPrime(n)

#returns k: the shared secret
def diffie_hellman():
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
  print("shared key: ", k)

  return k

#using key from Diffie-Hellman to encrypt a message in AES
#using CBC mode for AES
def pad(plaintext):

  #each block is 16 bits
  #because the key is 128 bits
  block_size = 16

  #calculate the padding needed 
  remainder = len(plaintext) % block_size
  padding_needed = block_size - remainder

  #return plaintext concatenated w/ spaces
  #no of spaces determined by padding_needed
  return plaintext + padding_needed * ' '

s = pad("Claire")

#removes whitespace from padding
def unpad(plaintext):
  return plaintext.rstrip()

print(unpad(s))

def encrypt(key, plaintext):

  #IV is like a salt for the vector
  #must be the same size as the block size
  IV = random.randbytes(16)

  padded_plaintext = pad(plaintext)
  print("padded_plaintext = ", padded_plaintext)

  #convert integer key passed in by diffie hellman
  #to a 16-byte string
  #to be useed by AES.new
  key_to_bytes = key.to_bytes(16)
  print("key_to_bytes = ", key_to_bytes)
  
  #create cipher
  #algorithm used to encrypt and decrypt the message
  cipher = AES.new(key_to_bytes, AES.MODE_CBC, IV)

  #change plaintext to bytes
  plaintext_to_bytes = padded_plaintext.encode('utf-8')
  print("plaintext_to_bytes = ", plaintext_to_bytes)

  #encrypt the plaintext
  ciphertext = cipher.encrypt(plaintext_to_bytes)
  print("ciphertext = ", ciphertext)

  return ciphertext, IV, key_to_bytes


ciphertext, IV, key_to_bytes = encrypt(6, "Claire")
print("ciphertext = ", ciphertext)
print("IV = ", IV)
print("key_to_bytes = ", key_to_bytes)

def decrypt(ciphertext, IV, key_to_bytes):
  print("IV = ", IV)
  #create a new cipher for decryption
  #uses all the same info as the cipher from the encryption
  cipher = AES.new(key_to_bytes, AES.MODE_CBC, IV)

  #decrypt the ciphertext
  #turns into plaintext in its byte form
  plaintext_still_bytes = cipher.decrypt(ciphertext)
  print("plaintext_still_bytes = ", plaintext_still_bytes)
  padded_plaintext = plaintext_still_bytes.decode('utf-8')
  print("padded_plaintext = ", padded_plaintext)
  plaintext = unpad(padded_plaintext)
  print("plaintext = ", plaintext)

  return

decrypt(ciphertext, IV, key_to_bytes)
  
  
  




























#encryption function from https://www.youtube.com/watch?v=GYCVmMCRmTM
#def AESencrypt(message):
#  cipher = AES.new(key, AES.MODE_EAX)
 # nonce = cipher.nonce
 # ciphertext, tag = cipher.encrypt_and_digest(message.encode('ascii'))
 # return nonce, ciphertext, tag

#decryption function from https://www.youtube.com/watch?v=GYCVmMCRmTM
#def AESdecrypt(nonce, ciphertext, tag):
 # cipher = AES.new(key, AES.MODE_EAX, nonce = nonce)
 # plaintext = cipher.decrypt(ciphertext)
 # return plaintext.decode('ascii')



#key to encrypt in AES
#key = diffie_hellman()

#make key into a 16 byte sequence to be used in AES
#key = sha256(str(key).encode()).digest()[:16]

#enter a message to be encrypted and encrypt it
#(from https://www.youtube.com/watch?v=GYCVmMCRmTM)
#nonce, ciphertext, tag = AESencrypt(input('Enter a message: '))
#decrypt (from https://www.youtube.com/watch?v=GYCVmMCRmTM)
#plaintext = AESdecrypt(nonce, ciphertext, tag)
#print encrypted message and decrypted message
#print ("ciphtertext = ", ciphertext)
#print("plaintext = ", plaintext)






