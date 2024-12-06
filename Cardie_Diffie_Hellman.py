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

#encryption function from https://www.youtube.com/watch?v=GYCVmMCRmTM
def AESencrypt(message):
  cipher = AES.new(key, AES.MODE_EAX)
  nonce = cipher.nonce
  ciphertext, tag = cipher.encrypt_and_digest(message.encode('ascii'))
  return nonce, ciphertext, tag

#decryption function from https://www.youtube.com/watch?v=GYCVmMCRmTM
def AESdecrypt(nonce, ciphertext, tag):
  cipher = AES.new(key, AES.MODE_EAX, nonce = nonce)
  plaintext = cipher.decrypt(ciphertext)
  return plaintext.decode('ascii')



#key to encrypt in AES
key = diffie_hellman()

#make key into a 16 byte sequence to be used in AES
key = sha256(str(key).encode()).digest()[:16]

#enter a message to be encrypted and encrypt it
#(from https://www.youtube.com/watch?v=GYCVmMCRmTM)
nonce, ciphertext, tag = AESencrypt(input('Enter a message: '))
#decrypt (from https://www.youtube.com/watch?v=GYCVmMCRmTM)
plaintext = AESdecrypt(nonce, ciphertext, tag)
#print encrypted message and decrypted message
print ("ciphtertext = ", ciphertext)
print("plaintext = ", plaintext)






