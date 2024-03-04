'''
Sets are used to store multiple items in a single variable
A set is a collection which is unordered, unchangeable and unindexed

* Note: Set items are unchangeable, but you can remove items and add new items.
'''

people = {'John', 'Mary', 'Eva'}
print(people)
print(type(people))

# Duplicates Not Allowed
people = {'John', 'Mary', 'Eva', 'John'}
print(people)

## Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:
print({'Jhon', 18, True, 1, 2})
## Note: The values False and 0 are considered the same value in sets, and are treated as duplicates:
print({'Jhon', 18, False, 0, 2})

print(len(people))

# Sets can be of any data type
set1 = {"Matheus", 34, True, 40, "male"}
print(set1)

# Set constructor
set2 = set(("Matheus", 34, True, 40, "male"))
print(set2)

