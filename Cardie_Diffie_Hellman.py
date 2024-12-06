
import Crypto
from Crypto.Util import number

def n_bit_prime(n):
  return number.getPrime(n)

from sympy import primitive_root
g = primitive_root(n_bit_prime(256))
print(g)




