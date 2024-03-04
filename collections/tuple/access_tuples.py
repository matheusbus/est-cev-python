# You can access tuple items by referring to the index number, inside square brackets:
my_tuple = ('Matheus', 18, 'Eng. Software')
print(my_tuple[1])

# Negative index
print(my_tuple[-1])

# Range of indexes
print(my_tuple[0:])
print(my_tuple[0:-1])
print(my_tuple[1:-1])

# Chek if item exists
if 'Matheus' in my_tuple:
    print('Yeah, Matheus is in your tuple.')

if 'matheus' in my_tuple:
    print('Yeah, matheus is in your tuple.')

