## Lists are ordered, changeable and allows duplicate values.
"""
append() - Adds an element at the end of the list
clear() - Removes all the elements from the list
copy() - Returns a copy of the list
count() - Returns the number of elements with the specified value
extend() - Add the elements of a list (or any iterable), to the end of the current list
index() - Returns the index of the first element with the specified value
insert() - Adds an element at the specified position
pop() - Removes the element at the specified position
remove() - Removes the item with the specified value
reverse() - Reverses the order of the list
sort() - Sorts the list
"""

## Creating lists
fruits = ['Abacate', 'Banana', 'Uva']
print(fruits)

for fruit in fruits:
    print(fruit)

fruits.append('Maçã')
print(fruits)

## Access items
print(fruits[1])
print(fruits[-1]) ## refere-se ao último item da lista. -2 é o penúltimo e assim por diante

more_fruits = ['Abacate', 'Abacaxi', 'Banana', 'Pêssego', 'Maçã', 'Uva', 'Kiwi', 'Manga']
print(more_fruits[2:5]) ## the search start at index 2 (included) and end at index 5 (not included)

print(more_fruits[:2])
print(more_fruits[5:])

fruits.remove('Banana')
if 'Banana' in fruits:
    print('Yes, \'Banana\' is in the fruits list.')
elif 'Abacate' in fruits:
    print('Yes, \'Abacate\' is in the fruits list.')

## Change list items
print('Before: ', more_fruits[2])
more_fruits[2] = 'Laranja'
print('After:', more_fruits[2])

print('Before: ', more_fruits)
more_fruits[1:3] = ["Tangerina", "Melancia"]
print('After: ', more_fruits)

# Insert method insert an item to a specified position
more_fruits.insert(3, 'Jabuticaba')
print(more_fruits)

# Append method insert an item to the end of the list
more_fruits.append('Limão')
print(more_fruits)

fruits.extend(more_fruits) ## Like a join between 2 lists
print(fruits)

# Add any iterable
tropical = ['Morango', 'Laranja']
tuple = ('Abacaxi', 'Limão')
tropical.extend(tuple)
print(tropical)

## Remove list items

# Specified item - removes the first occurance
tropical.remove('Morango')
# Index
fruits.pop(1)
# Remove last item
fruits.pop()
# Delete first item
del fruits[0]
# Delete list completely
del fruits
# Not work, because the list was deleted above
#fruits.clear()
more_fruits.clear()

# Loop lists
for fruit in tropical:
    print(fruit)

for i in range(len(tropical)):
    print(tropical[i])

i = 0
while i < len(tropical):
    print(tropical[i])
    i += 1

# Short hand
[print(x) for x in tropical]

## Lists compreenshion

# Syntax
# newlist = [expression for item in iterable if condition == True]
newlist = [x for x in tropical if "a" in x]
print(newlist)

newlist = [x for x in tropical if x != "Abacaxi"] # Only accept items that are not 'Abacaxi'
print(newlist)

## Sorting lists

tropical.sort()
print(tropical)

numeric_list = [121,51,21,43,66,26,52]
numeric_list.sort()
print(numeric_list)

numeric_list.sort(reverse=True)
print(numeric_list)

tropical.sort(reverse=True)
print(tropical)

def mySort(n):
    return abs(n - 50)

numeric_list.sort(key=mySort)
print(numeric_list)

# Case sensitive sorting can give an unexpected result
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# Perform a case-insensitive sort of the list:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

thislist.reverse()
print(thislist)

## Copy lists
copy_list = list(thislist)
print(copy_list)
copy_list2 = thislist.copy()
print(copy_list2)

## Joinin lists
list1 = [1, 2, 3]
list2 = ['A', 'B', 'C']

list3 = list1 + list2
print(list3)

for x in list2:
    list1.append(x)

print(list1)

list1.extend(list2)
print(list2)