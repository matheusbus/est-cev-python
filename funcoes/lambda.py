# Syntax - lambda arguments : expression

plus_ten = lambda a : a + 10
print(plus_ten(2))

sum = lambda a, b: a + b
print(sum(2,4))

# The power of lambda is better shown when you use them as an anonymous function inside another function.
def my_func(n):
    return lambda a : a * n

my_doubler = my_func(2)
print(my_doubler(5))

my_tripler = my_func(3)
print(my_tripler(5))

