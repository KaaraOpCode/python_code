"""def display_a():
    print('start a')
    display_c()
    print('c executed')
    print('end a')

def display_b():
    print('start b')
    display_a()
    print('a executed')
    print('end b')

def display_c():
    print('start c')
    display_b()
    print('b executed')
    print('end c')

display_c()
"""
"""
n = int(input('Enter: `'))

def fact(n):
    if n == 0:
        return 1
    else:
        return n + fact(n - 1)

print(fact(n))"""

def fibonacci(n):   # A recursive implementation of the Fibonacci function
    if n <= 1:
        return n
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))    # F_n = F_(n-1) + F_(n-2)
    
nterms = int(input('How many Fibonacci numbers do you want?'))

# Cannot find Fibonacci number if it is negative
if nterms <= 0:
    print('Error : Enter a positive number.')
else:
    print('Fibonacci sequence:', end = ' ')
    for i in range(nterms):
        print(fibonacci(i), end = ' ')