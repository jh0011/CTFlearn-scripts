# CTFLearn 
# Easy challenge 970 (The Credit Card Fraudster)
"""
To find the credit card number 54321******1234 that is a multiple of 123457 and 
fulfils the Luhn Algorithm check.
"""

def luhn_checksum(num_str):
    s = int(num_str[-1])
    for n, c in enumerate(num_str[:-1]):
        c = int(c)
        if (n % 2) == 0:
            c *= 2
        if c > 9:
            c -= 9
        s += c
    return (s % 10) == 0

def check_last_4_digits(credNumber):
    if (str(credNumber)[-4:] == '1234'):
        return True
    else:
        return False

minCredNumber = 5432100000001234
maxCredNumber = 5432109999991234

for x in range(minCredNumber, maxCredNumber + 1, 1):
    if (x % 123457 == 0):
        if (luhn_checksum(str(x)) and (check_last_4_digits(x))): 
            print('Credit number: ', x)
print('EXITING THE PROGRAM')




