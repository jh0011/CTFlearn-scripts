# CTFlearn 
# Easy challenge 1080 (Raspberry)
"""
Reverse engineer the instructions in Ghidra.
Concatenate the flag.
"""

def from_hex_dec(hex_num):
    return int(hex_num, 16)

flag = ""

flag += "CTFlearn{+Fru"

# if ((ulong)(byte)in_stack_00000010[0xd] * 0x15 == 0x89d)
flag += chr(int(int("89d", 16) / from_hex_dec("15")))

# if (((ulong)bVar1 / 0x15 == 5) && ((ulong)bVar1 % 0x15 == 0xb))
for element in range(32, 126):
    if (int(element / from_hex_dec("15")) == 5 and int(element % from_hex_dec("15")) == 11):
        flag += chr(element)
        break

flag += "123}"

print(flag)