from Problem import *    

problems = {}

def test_a_plus_abs_b(closure):
    a_plus_abs_b = closure['a_plus_abs_b']
    return True
problems[0] = Problem(intro="""Q1. Recall that we can assign new names to existing functions. Fill in the blanks in the following function definition for adding a to the absolute value of b, without calling abs:

>>> a_plus_abs_b(2, 3)
5
>>> a_plus_abs_b(2, -3)
5

""",test=test_a_plus_abs_b,init="""from operator import add, sub

def a_plus_abs_b(a, b):
    if b < 0:
        op = _____
    else:
        op = _____
    return op(a, b)

""")

def two_of_three(closure):
    two_of_three = closure['two_of_three']
    return True
problems[1] = Problem(intro="""Q2. Write a function that takes three positive numbers and returns the sum of the squares of the two largest numbers. Use only a single expression for the body of the function:

Return x*x + y*y, where x and y are the two largest of a, b, c.
""",test=test_a_plus_abs_b,init="""def two_of_three(a, b, c):


    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    "*** YOUR CODE HERE ***"

""")

def two_of_three(closure):
    return True
problems[2] = Problem(intro="""Q3. Let's try to write a function that does the same thing as an if statement:

def if_function(condition, true_result, false_result):
    if condition:
        return true_result
    else:
        return false_result

This function actually does not do the same thing as an if statement in all cases. To prove this fact, write functions c, t, and f such that one of the functions returns the number 1, but the other does not:

""",test=test_a_plus_abs_b,init="""def if_function(condition, true_result, false_result):
    if condition:
        return true_result
    else:
        return false_result
        
def with_if_statement():
    if c():
        return t()
    else:
        return f()

def with_if_function():
    return if_function(c(), t(), f())

def c():
    "*** YOUR CODE HERE ***"

def t():
    "*** YOUR CODE HERE ***"

def f():
    "*** YOUR CODE HERE ***"

""")


def two_of_three(closure):
    two_of_three = closure['two_of_three']
    return True
problems[1] = Problem(intro="""Q2. Write a function that takes three positive numbers and returns the sum of the squares of the two largest numbers. Use only a single expression for the body of the function:

Return x*x + y*y, where x and y are the two largest of a, b, c.
""",test=test_a_plus_abs_b,init="""def two_of_three(a, b, c):


    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    "*** YOUR CODE HERE ***"

""")

def test_hailstone(closure):
    return True
problems[3] = Problem(intro="""Q4. Douglas Hofstadter's Pulitzer-prize-winning book, Godel, Escher, Bach, poses the following mathematical puzzle.

    Pick a positive integer n as the start.
    If n is even, divide it by 2.
    If n is odd, multipy it by 3 and add 1.
    Continue this process until n is 1.

The number n will travel up and down but eventually end at 1 (at least for all numbers that have ever been tried -- nobody has ever proved that the sequence will terminate). Analogously, hailstone travels up and down in the atmosphere before eventually landing on earth.

The sequence of values of n is often called a Hailstone sequence, because hailstones also travel up and down in the atmosphere before falling to earth. Write a function that takes a single argument with formal parameter name n, prints out the hailstone sequence starting at n, and returns the number of steps in the sequence.

Hailstone sequences can get quite long! Try 27. What's the longest you can find? Fill in your solution below:

""",test=test_hailstone,init="""def hailstone(n):

""")

