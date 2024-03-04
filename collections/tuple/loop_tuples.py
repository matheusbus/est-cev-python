my_tuple = ('Matheus', 18, 'Eng. Software')

for value in my_tuple:
    print(value)

for i in range(len(my_tuple)):
    print(f"{i+1}° value: {my_tuple[i]}")

i = 0
while i < len(my_tuple):
    print(my_tuple[i])
    i += 1

