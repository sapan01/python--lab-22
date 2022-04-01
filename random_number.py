# Print random number of given length

import random

n = int(input())
if(n == 0):
    print(0)
r = random.randint(10**(n-1), (10**n - 1))
print(r)
