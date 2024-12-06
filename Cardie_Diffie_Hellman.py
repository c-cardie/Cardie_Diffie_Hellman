import Crypto
from Crypto.Util import number
from sympy import primitive_root
import random

#returns an n-bit prime number
def n_bit_prime(n):
  return number.getPrime(n)
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




