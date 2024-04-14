#difference -
#difference update

set1 = {'jenny', 'ram', 'new', 'love'}
set2 = {'new', 'raj', 'king', 6, 8}

# Calculate the difference between set1 and set2 and store it in set3
set3 = set1 - set2

# Update set1 with the difference of set1 and set2
set1.difference_update(set2)

print("After difference update:", set1)

# Adding a new element 'new' to set1
set1.add('new')

print("After adding 'new':", set1)


print(set1.symmetric_difference(set2))
print(set1^set2)