# CTFlearn 
# Medium challenge 290 (Weird Android Calculator)
"""
Perform an XOR for each element in the list.
Convert from decimal to ASCII values.
"""

def printAscii(listOfInt):
    for x in range(len(listOfInt)):
        print(chr(listOfInt[x]), end = "")

listOfInt = [1407, 1397, 1400, 1406, 1346, 1400, 1385, 1394, 1382, 1293, 1367, 1368, 1365, 1344, 1354, 1288, 1354, 1382, 1288, 1354, 1382, 1355, 1293, 1357, 1361, 1290, 1355, 1382, 1290, 1368, 1354, 1344, 1382, 1288, 1354, 1367, 1357, 1382, 1288, 1357, 1348]

for x in range (len(listOfInt)):
    listOfInt[x] = listOfInt[x] ^ 1337 #Performing the XOR operation
print(printAscii(listOfInt))