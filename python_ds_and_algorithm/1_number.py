# integer : immutable type
# 정수를 나타내는데 필요한 바이트 수
print((999).bit_length()) # 10


# integer casting
s = '11'

# 1) 10진법
d = int(s)
print(d) # 11

# 2) 2진법
b = int(s, 2)
print(b) # 3
# print(int(12, 2)) # TypeError: int() can't convert non-string with explicit base 

# 부동소수점
# float : immutable type


# 부동소수점끼리 비교하기

print(0.2 * 3 == 0.6) # False
print(1.2 - 0.2 == 1.0) # True
print(1.2 - 0.1 == 1.1) # False
print(0.1 * 0.1 == 0.01) # False

# equality test
import unittest

#class TestEquality(unittest.TestCase):
#    def test_equal(self):
#        self.assertAlmostEqual(0.2 * 3, 0.6)
#        self.assertAlmostEqual(1.2 - 0.2, 1.0)
#        self.assertAlmostEqual(1.2 - 0.1, 1.1)
#        self.assertAlmostEqual(0.1 * 0.1, 0.01)
#
#if __name__ == '__main__':
#    unittest.main()
    

def a(x, y, places=7):
    return round(abs(x-y), places) == 0

print(a(10, 2, places=7))

# Complex Number 
z = complex(5, 3)
print(z.real) # 실수
print(z.imag) # 허수
print(z.conjugate())

import cmath

# Deciaml Module

print(sum(0.1 for i in range(10)) == 1.0)

from decimal import Decimal
print(sum(Decimal("0.1") for i in range(10)) == Decimal("1.0"))
