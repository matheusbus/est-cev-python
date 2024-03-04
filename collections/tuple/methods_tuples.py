'''
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
'''

my_tuple = ('Matheus', 18, 'Eng. Software')
print(my_tuple.count(18))
print(my_tuple.index('Matheus'))
print(my_tuple.index('Something which is not in the list'))


