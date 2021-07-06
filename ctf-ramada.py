# CTFlearn 
# Easy challenge 1009 (Ramada)
"""
Convert the hexadecimal values into decimal values.
Cube root the decimal values.
Convert the cube rooted decimal values to ASCII characters.
"""

import numpy as np

# From InitData() function
list_of_hex_data = ["13693", "6b2c0", "11a9f9", "157000", "1cb91", "1bb528", "1bb528", "ded21", "144f38", "fb89d", "169b48", 
"d151f", "8b98b", "17d140", "ded21", "1338c0", "1338c0", "11a9f9", "1b000", "144f38", "1734eb"]

# Initialise an empyt list
list_of_int_converted = [0]*21

# Convert the hex to decimal
index=0
for element in list_of_hex_data:
    list_of_int_converted[index] = int(element, 16)
    index += 1

# Cube root the decimal values
list_of_int_cuberoot = np.cbrt(list_of_int_converted) 

# Convert from decimal to ASCII
flag = ""
for element in list_of_int_cuberoot:
    flag += chr(int(element))
print("Flag: CTFlearn{"+flag+"}")