# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

# Convert the tuple into a list to be able to change it:
fruits = ('Banana', 'Pineapple', 'Apple', 'Orange')
tropical = list(fruits)
tropical[1] = 'Kiwi'
fruits = tuple(tropical)

print(fruits)

# Add items - since tuple are immutable, they do not hava a built-in append() method

# 1- Convert into a list and then use the append() method
brands = ('Ford', 'Chevrolet', 'Toyota')
print(brands)
brand_list = list(brands)
brand_list.append('Maseratti')
brands = tuple(brand_list)
print(brands)

# 2- Add tuple to a tuple
new_brands = ('Fiat',)
brands += new_brands
print(brands)

# Remove items - tuples are unchangeable, so you cannot remove items from it.
brands = ('Ford', 'Chevrolet', 'Toyota')
print(brands)
brand_list = list(brands)
brand_list.remove('Ford')
brands = tuple(brand_list)
print(brands)

del brands
# print(brands) # doesn't work, becaus brands tuple was deleted above.