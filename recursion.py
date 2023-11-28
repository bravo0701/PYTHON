'''

a way of solving a problem by calling a function itself

property of recursion -   1. perform same operation multiple time with different inputs
                          2. in every step we try smaller inputs to make the problem smaller
                          3. base condition is needed to stop recursion else infinite loop will occur

it works using stack memory( LIFO )

recursion is less time and space efficient as compared to iteration, but it is useful in cases where the
problem can be divided into similar subproblems

Three steps to write recursion function:

    1. find recursive cse
    2. find base case to stop infinite loop
    3. find the unintentional case or constraints
'''


def recursive_method(n):
    if n<1:
        print("n is less than 1")
    else:
        recursive_method(n-1)
        print(n)


recursive_method(4)

# FACTORIAL


def factorial(n):
    assert n>=0 and int(n) == n, 'The number must be positive integer only!'
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(8))

# FIBONACCI NUMBER


def fibo(n):

    assert n>=0 and int(n) == n, 'The n should be positive integer only!'
    if n in [0, 1]:
        return n
    else:
        return fibo(n-1) + fibo(n-2)


print(fibo(10))
