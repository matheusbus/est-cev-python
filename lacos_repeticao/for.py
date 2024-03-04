fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# Loop through the letters in the word "banana":
for x in "banana":
  print(x)

# Exit the loop when x is "banana":
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

# Don't print banana
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

for x in range(6): # will print 0 to 5
  print(x)

# Using the start parameter
for x in range(2, 6):
  print(x)

# Increment the sequence with 3 (default is 1)
for x in range(2, 30, 3):
  print(x)

# Else in for looping
for x in range(6):
  print(x)
else:
  print("Finally finished!")

# break will exit looping without pass through else statement
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

# Nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

# for loops cannot be empty, but if you for some reason have a for loop with no content,
# put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
  pass