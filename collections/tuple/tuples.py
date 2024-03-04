## Tuples are used to store multiple items in a single variable
# Tuples are ordered
# Tuples are unchangeable
# Tuples allows duplicated items, since tuples are indexed
# Tuples can be of any data type
person = ('Matheus', 18, False)

print(person)
print(type(person)) # tuple

# Tuples are indexed
print(person[0])

fruits = ('Banana', 'Pineapple', 'Banana')
print(fruits)

# Tuple length
print(len(fruits))

# Tuple with one item
cars = ('Arizzo') # not a tuple
cars = ('Arizzo',) # yes, this is a tuple

# Tuple constructor
something = tuple(('Jony', 12, False)) # note the double round-brackets
