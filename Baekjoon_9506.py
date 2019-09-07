from divisor_B1 import Divisor
from divisors_sum_B1 import Divisors_sum
from Checking_P_or_NP_B1 import Checking

n = input()  # 2 < n < 100, 000
div = []  # divisor
dsum = 0 # divisors sum

div = Divisor(n, div)
dsum = Divisors_sum(div, dsum)
Checking(n, dsum)