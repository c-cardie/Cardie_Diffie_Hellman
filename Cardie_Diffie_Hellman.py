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
a = random.randint(1, p)
print("a = ", a)

#Bob's private key
b = random.randint(1, p)
print("b = " , b)




