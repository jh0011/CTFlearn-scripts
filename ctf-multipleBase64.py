# CTFlearn 
# Hard challenge 121 (So many 64s)
"""
Decode the base64 encoded string in a while loop till the curly brace { is found.
"""

import base64

dataFile = open('C:\\Users\\dell\\Downloads\\flag.txt', 'r')
output_string = dataFile.read()
substring = "{"
while (substring not in output_string):
    output_string = base64.b64decode(output_string).decode('utf-8')
print(output_string)
