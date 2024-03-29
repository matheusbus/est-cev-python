# Extract the values back into variables is called "unpacking"
fruits = ('Banana', 'Apple', 'Cherry')

(yellow, green, red) = fruits
print(yellow)
print(green)
print(red)

# Assign the rest of the values as a list called "red"
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits
print(red)

# If the asterisk is added to another variable name than the last, Python will
# assign values to the variable until the number of values left matches the number of variables left.
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

