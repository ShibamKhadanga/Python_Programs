'''Using Dict Function'''
# Original array
array = [1, 2, 2, 3, 4, 4, 5]

# Removing duplicates while preserving order
unique_array = list(dict.fromkeys(array))

print(unique_array)




"""Using Set Function"""
# Original array
array = [1, 2, 2, 3, 4, 4, 5]

# Removing duplicates using set
unique_array = list(set(array))

print(unique_array)
