def is_prime(n):
    for i in range(2, n):
        if (n % i == 0):
            return False
    return True
    
def nth_prime(n):
    i = 2
    while n > 0:
        i += 1
        if is_prime(i):
            n -= 1
    return i
    
def primorial(n):
    i = 1
    t = 1
    while i <= n:
        if is_prime(i):
            t *= i
        i += 1
    return t
    
from math import e, log

def log_primorial(n):
    i = 1
    t = 0
    while i <= n:
        if is_prime(i):
            t += log(i)
        i += 1
    return t
    
print [i / primorial(i) for i in range(2,50)]
print [log_primorial(i) for i in range(500)]
#print [(e**i) / primorial(i) for i in range(15)]

ans = [(5,0,1),(1,5,0),(2,0,2),(1,3,1),(0,6,0),(1,1,2)]
