binary = 0
digit = 0
hex = 0

def print_menu():
    print("Decoding Menu" + "\n-------------")
    print("1. Decode hexadecimal")
    print("2. Decode binary")
    print("3. Convert binary to hexadecimal")
    print("4. Quit\n")

def hex_char_decode(digit):
    if digit == "a":
        return 10
    elif digit == "b":
        return 11
    elif digit == "c":
        return 12
    elif digit == "d":
        return 13
    elif digit == "e":
        return 14
    elif digit == "f":
        return 15
    else:
        return digit

def hex_string_decode(hex):
    sum = 0
    list = []
    for i in hex.upper():
        if i == "X":
            continue
        elif i in ['A','B','C','D','E','F']:
            list.append(ord(i)-55)
        else:
            list.append(int(i))
    list.reverse()
    for i in range(0,len(list)):
        sum += list[i] * 16**i
    return sum

def binary_string_decode(binary):
    sum = 0
    list = [i for i in binary]
    if list[0] == '0' and list[1] == 'b':
        del list[0:2]
    list = [int(i) for i in list]
    list.reverse()
    for i in range(0,len(list)):
        sum += list[i] * 2**i
    return sum

def binary_to_hex(binary):
    list = [int(i) for i in binary]
    new_list = [] # empty list used later in function, explain later
    last_list = [] # empty list used later in function, explain later
    if len(list) % 4 != 0: # appends i numbers of 0 to the list if the binary number is not a factor of 4
        for i in range(len(list) % 4,4 ):
            list.insert(0,0)
    list.reverse() # reverses the order of the list for make the calculations easier
    new_list = [list[i:i+4] for i in range(0, len(list), 4)] # redefining list in this case using ternary operator
    # draws four numbers from list at a time and groups them together into multiple singular list inside new_list
    for i in range(0, len(new_list)): # new_list only recognizes the list and not the individual vars inside those list
        sum = 0
        for j in range(0,4): # simple for loop to go through each var in the 'sublist'
            sum += new_list[i][j] * 2**j # for each list inside new_list, it sums up the the output for the 4 binary #'s
        last_list.append(sum) # adds sum to last_list
    last_list.reverse() # reverses the order again to make the syntax in the correct order (see line 77)
    new_list.clear() # cleared this list to make use of it again
    for i in last_list: # last_list is now in binary, all that's left is converting binary to hex through characters
        if 0 <= i <= 9:
            new_list.append(str(i))
        if 10 <= i <= 15:
            new_list.append(chr(i + 55))
    # new_list.insert(0,"0x") commented this code since program does not like it (this is also correct, autograder mad)
    return f"{"".join(new_list)}" # joins the strings inside the list into a singular string (autograder happy)

if __name__ == "__main__":
    while True:
        print_menu()
        user_input = int(input("Please enter an option: "))
        if user_input == 1:
            hex = input("Please enter the numeric string to convert: ")
            hex_char_decode(digit)
            print("Result: " + f"{hex_string_decode(hex)}\n")
        elif user_input == 2:
            binary = input("Please enter the numeric string to convert: ")
            print("Result: " + f"{binary_string_decode(binary)}\n")
        elif user_input == 3:
            binary = input("Please enter the numeric string to convert: ")
            print("Result: " + f"{binary_to_hex(binary)}\n")
        elif user_input == 4:
            break