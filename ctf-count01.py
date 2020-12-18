# CTFLearn 
# Easy challenge 174 (Simple Programming)
"""
To count the number of lines where the count of 0 is a multiple of 3
or the count of 1 is a multiple of 2.
"""

dataFile = open('C:\\Users\\dell\\Downloads\\data.dat', 'r')
fileLines = dataFile.readlines()
count = 0
for line in fileLines:
    count0 = 0
    count1 = 0
    for character in line:
        if character == '0':
            count0 = count0 + 1
        if character == '1':
            count1 = count1 + 1
    if (count0 % 3 == 0 or count1 % 2 == 0):
        count = count + 1
print("Count is: ", count)