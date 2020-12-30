# CTFlearn 
# Hard challenge 231 (Symbolic Decimals)
"""
Map each symbol to an integer.
Convert the decimal value to ASCII characters.
"""

def convertDeci2Ascii(output_string): # Converting from decimal to ascii
    output_list = output_string.split(" ")
    output_list.pop()
    ascii_text = ""
    for x in output_list:
        ascii_text = ascii_text + chr(int(x))
    return ascii_text


symbols = [')', '!', '@', '#', '$', '%', '^', '&', '*', '(']
input_string = "^&,*$,&),!@#,*#,!!^,(&,!!$,(%,$^,(%,*&,(&,!!$,!!%,(%,$^,(%,&),!!!,!!$,(%,$^,(%,&^,!)%,!)@,!)!"
input_list = input_string.split(",")
output_string = ""
for x in input_list:
    for y in x:
        for symIndex in range(len(symbols)):
            if (y == symbols[symIndex]):
                output_string = output_string + str(symIndex) # Mapping the symbol to the number
                break
    output_string = output_string + " "
print("Flag: ", convertDeci2Ascii(output_string))