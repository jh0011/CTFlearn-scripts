# CTFlearn 
# Easy challenge 995 (Recklinghausen)
"""
XOR the hex values and store them as decimal values.
Convert the decimal values into ASCII characters.
"""

# From msg5 variable
list_of_hex_data = ["21", "7e", "3d", "2a", "38", "12", "1b", "1f", "0c", "10", "05", 
"2c", "0b", "16", "0c", "18", "1b", "0d", "0a", "0d", "0e", "17", "1b", "12", "1b", "21", "38", 
"1b", "0d", "0a", "17", "08", "1f", "12", "03"]

# Initialise an empty list
list_of_decimal = [0]*35

index_for_string1 = 1 # always remains the same
index_for_string2 = 2 # increments by 1

# Algorithm seen from the CheckMsg() function
# XOR 0x7e with the rest of the elements in list_of_hex_data starting with index 2
# The values from the XOR will be stored as decimal values
for index in range(33):
    list_of_decimal[index] = int(list_of_hex_data[index_for_string1], 16) ^ int(list_of_hex_data[index_for_string2 + index], 16)
print(list_of_decimal)

# Convert from decimal to ASCII
flag=""
for element in list_of_decimal:
    flag += chr(element)
print("Flag: " + flag)