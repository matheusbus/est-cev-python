# Use "def" keyword to implement a function
def my_function():
  print("Hello from a function")

# Calling a function
my_function()

# Arguments
def hello_word(fname):
  print(f"Hello, {fname}")

hello_word("Matheus")

# Two Arguments
def hello_word(fname, lname):
  print(fname + " " + lname)

hello_word("Emil", "Refsnes")

# Arbitrary arguments
# If you do not know how many arguments that will be passed into your function,
# add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:
def youngest_child(*kids):
  print("The youngest child is " + kids[2])

youngest_child("Emil", "Tobias", "Linus")

# Keyword arguments
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Arbitrary Keyword Arguments, **kwargs
def last_name(**kid):
  print("His last name is " + kid["lname"])

last_name(fname = "Tobias", lname = "Refsnes")

# Default Parameter Value
def print_country(country = "Brazil"):
  print("I am from ", country)

print_country("Norway")
print_country()
print_country("Germany")

# Passing a List as an Argument
def list_fruits(fruits):
  for fruit in fruits:
    print(fruit)

fruits = ["apple", "banana", "cherry"]

list_fruits(fruits)

# Return Values
def sum(a=0, b=0):
  return a + b

print(sum(2,2))

# The pass statement
# function definitions cannot be empty, but if you for some reason have a
# function definition with no content, put in the pass statement to avoid getting an error
def func_with_no_body():
  pass

func_with_no_body()

# Positional-Only Arguments
# you can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
# to specify that a function can have only positional arguments, add , / after the arguments:
def positional_only_arguments_function(x, y, /):
  return x + y

# positional_only_arguments_function(x=1, y=2) # i can't pass keyword arguments
positional_only_arguments_function(1, 2)


# Keyword-Only Arguments
# To specify that a function can have only keyword arguments, add *, before the arguments:
def keyword_only_arguments_function(*, x, y):
  return x - y

# keyword_only_arguments_function(5, 2) # i can't pass positional arguments, i have to specify keyword
keyword_only_arguments_function(x=10, y=20)
keyword_only_arguments_function(y=10, x=20)

# Combine Positional-Only and Keyword-Only
def combined_function(a, b, /, *, x, y):
  print(a + b + x + y)

combined_function(10, 5, x=8, y=9)

# Recursion
def try_recursion(k):
  if(k > 0):
    result = k * try_recursion(k - 1)
  else:
    result = 1
  return result

print(try_recursion(5))

# Returning multiple values (with tuple assignments)
def swap(x, y):
    return y, x  # Return multiple values as a tuple without the parenthesis.
                 # (Note: parenthesis have been excluded but can be included)

x = 1
y = 2
x, y = swap(x, y)
print(x, y)

def create_avg():
  total = 0
  count = 0

  def avg(n):
    nonlocal total, count
    total += n
    count += 1
    return total / count

  return avg

avg = create_avg()
avg(3)  # => 3.0
avg(5)  # (3+5)/2 => 4.0
avg(7)  # (8+7)/3 => 5.0