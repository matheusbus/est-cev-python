'''
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
'''

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
    print('a is greather than b')

# Short hand if
if a > b: print('a is greather tahn b')

# Short hand if..else
print("A") if a > b else print("B")

# One line if else statement, with 3 conditions:
print("A") if a > b else print("=") if a == b else print("B")

# We can use AND, OR, NOT operatores in if statements

# The pass statement:
# if statements cannot be empty, but if you for some reason have an if
# statement with no content, put in the pass statement to avoid getting an error.
if b > a:
    pass

