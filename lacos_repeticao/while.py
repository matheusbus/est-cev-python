i = 1
while i < 6:
    print(i)
    i += 1

i = 1
while i < 5:
    print(i)
    if(i == 3):
        break
    i += 1

i = 1
while i < 5:
    i += 1
    if(i == 3):
        print("I = 3")
        continue # stop the current iteration and continue in the next
    print(i)

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
