binary = 0
digit = 0

def print_menu():
    print("Decoding Menu" + "\n-------------")
    print("1. Decode hexadecimal")
    print("2. Decode binary")
    print("3. Convert binary to hexadecimal")
    print("4. Quit\n")

def hex_char_decode(digit):
    digit = hex
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
    hex = str(numeric_string)
    global sum
    list = []
    for i in hex.lower():
        if i == "x":
            continue
        elif i == "a":
            i = 10
            list.append(int(i))
        elif i == "b":
            i = 11
            list.append(int(i))
        elif i == "c":
            i = 12
            list.append(int(i))
        elif i == "d":
            i = 13
            list.append(int(i))
        elif i == "e":
            i = 14
            list.append(int(i))
        elif i == "f":
            i = 15
            list.append(i)
        else:
            list.append(int(i))
    list.reverse()
    for i in range(0,len(list)):
        sum += list[i] * 16**i
    print(f"Result: {sum}\n")

def binary_string_decode(binary):
    binary = str(numeric_string)
    global sum
    list = [i for i in binary]
    if list[0] == '0' and list[1] == 'b':
        del list[0:2]
    list = [int(i) for i in list]
    list.reverse()
    for i in range(0,len(list)):
        sum += list[i] * 2**i
    print(f"Result: {sum}\n")

def binary_to_hex(binary):
    binary = str(numeric_string)
    list = [int(i) for i in binary]
    new_list = []
    last_list = []
    if len(list) % 4 != 0:
        for i in range(len(list) % 4,4 ):
            list.insert(0,0)
    list.reverse()
    new_list = [list[i:i+4] for i in range(0, len(list), 4)]
    for i in range(0, len(new_list)):
        sum = 0
        for j in range(0,4):
            sum += new_list[i][j] * 2**j
        last_list.append(sum)
    last_list.reverse()
    new_list.clear()
    for i in last_list:
        if 0 <= i <= 9:
            new_list.append(str(i))
        if i == 10:
            new_list.append("A")
        if i == 11:
            new_list.append("B")
        if i == 12:
            new_list.append("C")
        if i == 13:
            new_list.append("D")
        if i == 14:
            new_list.append("E")
        if i == 15:
            new_list.append("F")
    # new_list.insert(0,"0x") commented this code since program does not like it
    print("Result: "+"".join(new_list) + "\n")

while True:
    sum = 0
    print_menu()
    user_input = int(input("Please enter an option: "))
    if user_input == 1:
        numeric_string = input("Please enter the numeric string to convert: ")
        hex_string_decode(hex)
    elif user_input == 2:
        numeric_string = input("Please enter the numeric string to convert: ")
        binary_string_decode(binary)
    elif user_input == 3:
        numeric_string = input("Please enter the numeric string to convert: ")
        binary_to_hex(binary)
    elif user_input == 4:
        print("Goodbye!")
        break
