from Problem import *    

problems = {}

def test1(closure):
    return True
problems[1] = Problem(intro="""Echo test. 
This problem can be passed by any legal python program that doesn't have any python errors (eg divide by 0).
""",test=test1,init="""print "abc" """)

def test2(closure):
    def f(n):
      if (n == 0): return 1
      else: return n * f(n-1)
    for i in range(10):
      assert(closure['fact'](i) == f(i))
problems[2] = Problem(intro='Calculates the factorial of n.',test=test2,init="def fact(n):")

def test3(closure):
    last = closure['last']
    assert(last([1,2,3]) == 3)
problems[3] = Problem(intro='Find the last element of a list.',test=test3,init="def last(l):")

def test4(closure):
    palindrome = closure['is_palindrome']
    assert(palindrome(['a','b','a']))
problems[4] = Problem(intro='Find out whether a list is a palindrome. A palindrome can be read forward or backward; e.g. [x,a,m,a,x].',test=test4,init="def is_palindrome(s):")
