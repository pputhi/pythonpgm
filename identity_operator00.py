'''a=2
b=4
print(a is b)
print(a is not b)
'''
# Using the 'in' operator
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  # Output: True
print(6 in my_list)  # Output: False

my_string = "Hello, World!"
print('o' in my_string)  # Output: True
print('z' in my_string)  # Output: False

my_dict = {'a': 1, 'b': 2, 'c': 3}
print('a' in my_dict)  # Output: True
print(1 in my_dict)    # Output: False (membership operators test keys in dictionaries, not values)

# Using the 'not in' operator
print(6 not in my_list)  # Output: True
print('z' not in my_string)  # Output: True
print('a' not in my_dict)  # Output: False
