from Problem import *    

problems = {}

def test_f(closure):
    f = closure['f']
    return True
problems[0] = Problem(intro="""Exercise 1.3. 

Define a procedure that takes three numbers as arguments and returns the sum of the squares of the two larger numbers. """,test=test_f,init="def f(a,b,c):")

def test_f2(closure):
    f = closure['f']
    return True
problems[1] = Problem(intro="""Exercise 1.11. 

A function f is defined by the rule that f(n) = n if n<3 and f(n) = f(n - 1) + 2f(n - 2) + 3f(n - 3) if n> 3. Write a procedure that computes f by means of a recursive process. Write a procedure that computes f by means of an iterative process.  """,test=test_f2,init="def f(n):")

def test_f3(closure):
    f = closure['p']
    return True
problems[2] = Problem(intro="""Exercise 1.12.  

The following pattern of numbers is called Pascal's triangle.

The numbers at the edge of the triangle are all 1, and each number inside the triangle is the sum of the two numbers above it.35 Write a procedure that computes elements of Pascal's triangle by means of a recursive process.""",test=test_f3,init="def p(n):")

def test_exp(closure):
    exp = closure['exp']
    return True
problems[3] = Problem(intro="""Exercise 1.16.  

Design a procedure that evolves an iterative exponentiation process that uses successive squaring and uses a logarithmic number of steps, as does fast-expt. 

(Hint: Using the observation that (bn/2)2 = (b2)n/2, keep, along with the exponent n and the base b, an additional state variable a, and define the state transformation in such a way that the product a bn is unchanged from state to state. At the beginning of the process a is taken to be 1, and the answer is given by the value of a at the end of the process. In general, the technique of defining an invariant quantity that remains unchanged from state to state is a powerful way to think about the design of iterative algorithms.)""",test=test_exp,init="def exp(n):")


def test_mult(closure):
    mult = closure['mult']
    return True
problems[4] = Problem(intro="""Exercise 1.17.  

The exponentiation algorithms in this section are based on performing exponentiation by means of repeated multiplication. In a similar way, one can perform integer multiplication by means of repeated addition. The following multiplication procedure (in which it is assumed that our language can only add, not multiply) is analogous to the expt procedure:

(define (* a b)
  (if (= b 0)
      0
      (+ a (* a (- b 1)))))

This algorithm takes a number of steps that is linear in b. Now suppose we include, together with addition, operations double, which doubles an integer, and halve, which divides an (even) integer by 2. Using these, design a multiplication procedure analogous to fast-expt that uses a logarithmic number of steps.""",test=test_mult,init="def mult(n):")

def test_mult2(closure):
    mult = closure['mult']
    return True
problems[5] = Problem(intro="""Exercise 1.18.  
Using the results of exercises 1.16 and 1.17, devise a procedure that generates an iterative process for multiplying two integers in terms of adding, doubling, and halving and uses a logarithmic number of steps.40 """,test=test_mult2,init="def mult(n):")


def test_fib(closure):
    fib = closure['fib']
    return True
problems[6] = Problem(intro="""Exercise 1.19.   

There is a clever algorithm for computing the Fibonacci numbers in a logarithmic number of steps. Recall the transformation of the state variables a and b in the fib-iter process of section 1.2.2: a a + b and b a. Call this transformation T, and observe that applying T over and over again n times, starting with 1 and 0, produces the pair Fib(n + 1) and Fib(n). In other words, the Fibonacci numbers are produced by applying Tn, the nth power of the transformation T, starting with the pair (1,0). Now consider T to be the special case of p = 0 and q = 1 in a family of transformations Tpq, where Tpq transforms the pair (a,b) according to a bq + aq + ap and b bp + aq. Show that if we apply such a transformation Tpq twice, the effect is the same as using a single transformation Tp'q' of the same form, and compute p' and q' in terms of p and q. This gives us an explicit way to square these transformations, and thus we can compute Tn using successive squaring, as in the fast-expt procedure. Put this all together to complete the following procedure, which runs in a logarithmic number of steps:41

(define (fib n)
  (fib-iter 1 0 0 1 n))
(define (fib-iter a b p q count)
  (cond ((= count 0) b)
        ((even? count)
         (fib-iter a
                   b
                   <??>      ; compute p'
                   <??>      ; compute q'
                   (/ count 2)))
        (else (fib-iter (+ (* b q) (* a q) (* a p))
                        (+ (* b p) (* a q))
                        p
                        q
                        (- count 1)))))
 """,test=test_mult2,init="def mult(n):")
