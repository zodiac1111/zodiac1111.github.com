#Exercise 1.3.  Define a procedure that takes three numbers as arguments and returns the sum of the squares of the two larger numbers. 
def proc(a,b,c):
    if (a >= c and b >= c):
        return (a**2 + b**2)
    if (a >= b and c >= b):
        return (a**2 + c**2)
    return (b**2 + c**2)

print proc(2,3,5)

def square(x): return x * x

def good_enough(guess, x):
   return abs(square(guess) - x) < 0.001

def average(x, y):
   return (x + y) / 2.0

def improve(guess, x):
   return average(guess, float(x) / guess)

def sqrt_iter(guess, x):
   if good_enough(guess, x):
      return guess
   else:
      return sqrt_iter(improve(guess, x), x)

def sqrt(x):
   return sqrt_iter(1.0, float(x))

print (sqrt(9))
print (sqrt(100 + 37))
print (sqrt(sqrt(2)+sqrt(3)))
print (square(sqrt(1000)))

#Exercise 1.7.  The good-enough? test used in computing square roots will not be very effective for finding the square roots of very small numbers. Also, in real computers, arithmetic operations are almost always performed with limited precision. This makes our test inadequate for very large numbers. Explain these statements, with examples showing how the test fails for small and large numbers. An alternative strategy for implementing good-enough? is to watch how guess changes from one iteration to the next and to stop when the change is a very small fraction of the guess. Design a square-root procedure that uses this kind of end test. Does this work better for small and large numbers? 

def good_enough_gp(guess, prev):
   return abs(guess - prev) / guess < 0.001
def sqrt_iter_gp(guess, prev, x):
   if good_enough_gp(guess, prev):
      return guess
   else:
      return sqrt_iter_gp(improve(guess, x), guess, x)
def sqrt_gp(x):
   return sqrt_iter_gp(4.0, 1.0, float(x))

#Exercise 1.8.  Newton's method for cube roots is based on the fact that if y is an approximation to the cube root of x, then a better approximation is given by the value Use this formula to implement a cube-root procedure analogous to the square-root procedure. 

def improve_cube(guess, x):
   return (2.0*guess + float(x)/(guess * guess)) / 3.0
def cube_iter(guess, prev, x):
   if good_enough_gp(guess, prev):
      return guess
   else:
      return cube_iter(improve_cube(guess, x), guess, x)
def cube_root_0(x):
   return cube_iter(27.0, 1.0, x)

#Exercise 1.9.  Each of the following two procedures defines a method for adding two positive integers in terms of the procedures inc, which increments its argument by 1, and dec, which decrements its argument by 1.

def inc(a): return a + 1
def dec(a): return a - 1
def plus(a, b):
   if a == 0:
      return b
   else:
      return inc(plus(dec(a), b))
def plus(a, b):
   if a == 0:
      return b
   else:
      return plus(dec(a), inc(b))

# Exercise 1.10
def a(x, y):
   if y == 0:
      return 0
   elif x == 0:
      return 2 * y
   elif y == 1:
      return 2
   else:
      return a(x - 1, a(x, y - 1))
print (a(1, 10))
print (a(2, 4))
print (a(3, 3))
def f(n): return a(0, n)
def g(n): return a(1, n)
def h(n): return a(2, n)
def k(n): return 5 * n * n

# Exercise 1.11
def f(n):
   if n < 3:
      return n
   else:
      return f(n-1) + 2*f(n-2) + 3*f(n-3)
def f_iter(a, b, c, count):
   if count == 0:
      return c
   else:
      return f_iter(a + 2*b + 3*c, a, b, count-1)
def f(n):
   return f_iter(2, 1, 0, n)

# Exercise 1.12
def pascals_triangle(n, k):
   if n == 0:
      return 1
   elif n == k:
      return 1
   else:
      return pascals_triangle(n-1, k-1) + pascals_triangle(n-1, k)

# Exercise 1.15
def cube(x): return x * x * x
def p(x): return 3.0 * x - 4.0 * cube(x)
def sine(angle):
   if not(abs(angle) > 0.1):
      return angle
   else:
      return p(sine(angle / 3.0))

# 1.2.4 Procedures and the Processes They Generate - Exponentiation

# Linear recursion
def expt(b, n):
   if n == 0:
      return 1
   else:
      return b * expt(b, n - 1)

# Linear iteration
def expt_iter(b, counter, product):
   if counter == 0:
      return product
   else:
      return expt_iter(b, counter - 1, b * product)
def expt(b, n):
   return expt_iter(b, n, 1)

# Logarithmic iteration
def even(n): return (n % 2) == 0

def fast_expt(b, n):
   if n == 0:
      return 1
   else:
      if even(n):
         return square(fast_expt(b, n / 2))
      else:
         return b * fast_expt(b, n - 1)

# Exercise 1.17
def multiply(a, b):
   if b == 0:
      return 0
   else:
      return plus(a, multiply(a, dec(b)))

#1.18 do it!


# Exercise 1.19
# exercise left to reader to solve for p' and q'
#def fib_iter(a, b, p, q, count):
#   if count == 0:
#      return b
#   else:
#      if even(count):
#         return fib_iter(a, b, p', q', count / 2)
#      else:
#         return fib_iter((b * q) + (a * q) + (a * p), (b * p) + (a * q), p, q, count - 1)
#def fib(n):
#   return fib_iter(1, 0, 0, 1, n)

#Exercise 1.21.  Use the smallest-divisor procedure to find the smallest divisor of each of the following numbers: 199, 1999, 19999. 


