def fib(n):
    if(n == 1 or n == 2):
        return 1
    return fib(n - 1) + fib(n - 2)



'''
base, exp
base = 2
exp = 10
2 ** 10 = 1024
'''

def pot(base, exp):
    if(exp == 0):
        return 1
    return base * pot(base, exp - 1)

print(pot(2,10))