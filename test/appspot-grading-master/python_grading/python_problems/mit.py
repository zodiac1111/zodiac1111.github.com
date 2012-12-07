from Problem import *    

problems_1 = {}

def test_is_prime(closure):
    is_prime = closure['is_prime']
    primes = [2,3,5,7,11,13,17,19,23,29]
    for p in range(2,30):
        if (p in primes):
            assert(is_prime(p))
        else:
            assert(not(is_prime(p)))
problems_1[0] = Problem(intro="""Prime testing

Determine if a number is prime.""",test=test_is_prime,init="def is_prime(n):")

def test_nth_prime(closure):
    nth_prime = closure['nth_prime']

problems_1[1] = Problem(intro="""Find the nth prime. 

The 0th prime is 2.""",test=test_nth_prime,init="def nth_prime(n):")

def test_primorial(closure):
    primorial = closure['primorial']
    assert([primorial(i) for i in range(12)] == [1, 1, 2, 6, 6, 30, 30, 210, 210, 210, 210, 2310])
problems_1[2] = Problem(intro="""Primorial function n#


In this problem we investigate the properties of the primorial function n#, the product of all primes below n. Write such a function. You should have

0# = 1
1# = 1
2# = 2
3# = 6
4# = 6
5# = 30
6# = 30
7# = 120
8# = 210
9# = 210

Verify that n# < 4**n for n > 1. Prove it if you want.

""",test=test_primorial,init="def primorial(n):")

def test_log_primorial(closure):
    log_primorial = closure['log_primorial']
    [log_primorial(i) for i in range(2,50)]
    return True
    
problems_1[3] = Problem(intro="""More primorials

The tightest exponential bound on n# states that

n# ~ e**n

in the sense that the ratio approaches one. 

However, we cannot work directly with n# as it will be too large. Instead we can write it as

log n# ~ n

write something to calculate log n#.""",test=test_log_primorial,init="def log_primorial(n):")

problems_2 = {}

def test_ans(closure):
    ans = closure['ans']
    
    def lc_from_tuple(t):
        (a,b,c) = t
        return 6*a + 9*b + 20*c
    
    assert(map(lc_from_tuple,ans) == [50,51,52,53,54,55])
    
problems_2[0] = Problem(intro="""McNuggets

ans = [(5,0,1),(1,5,0),(2,0,2),(1,3,1),(0,6,0),(1,1,2)]

prove the following

Theorem: If it is possible to buy x, x+1,..., x+5 sets of McNuggets, for some x, then it is possible to buy any number of McNuggets >= x, given that McNuggets come in 6, 9 and 20 packs.

""",test=test_ans,init="ans = [(0,0,0), (1,0,0),...]")
