from console_gfx import ConsoleGfx

def display_menu():  # prints the display menu
    print("\n"*2 + "RLE Menu" + "\n--------")
    print("0. Exit")
    print("1. Load File")
    print("2. Load Test Image")
    print("3. Read RLE String")
    print("4. Read RLE Hex String")
    print("5. Read Data Hex String")
    print("6. Display Image")
    print("7. Display RLE String")
    print("8. Display Hex RLE Data")
    print("9. Display Hex Flat Data\n")
    global menu_option
    menu_option = int(input("Select a Menu Option: "))


def to_hex_string(data):
    hex_string = []
    for i in data:
        if 0 <= i <= 9:
            hex_string.append(str(i))
        elif 10 <= i <= 15:
            hex_string.append(chr(i + 55).lower())
    return "".join(hex_string)


def count_runs(flat_data):
    total_runs, count = 0
    for i in range(1, len(flat_data)):
        if flat_data[i-1] == flat_data[i]:  # checks if the first number is equal to the next number in list
            count += 1  # adds one to the count
            if count == 15:  # if the count reaches 15 it adds to the total runs and restarts the count
                total_runs += 1
                count = 0
        elif flat_data[i-1] != flat_data[i]:  # if not equal to next number in list, restarts the count and adds to runs
            count = 0
            total_runs += 1
    if flat_data[-1] == flat_data[-2]:  # essentially here for clarity, but after it reaches the last number in the list
        total_runs += 1  # we can just add one since it'll conclude the total runs for any condition
    elif flat_data[-1] != flat_data[-2]:
        total_runs += 1
    return total_runs


def encode_rle(flat_data):
    rle_data = []
    total_runs = 0
    for i in range(1, len(flat_data)):
        if flat_data[i-1] == flat_data[i]:  # checks if current number is equal to next number in sequence
            total_runs += 1  # if so, total runs is updated by 1
            if total_runs == 15:  # if total runs reaches 15, it appends 15 and the number to the list and restarts runs
                rle_data.extend([total_runs, flat_data[i-1]])
                total_runs = 0
        if flat_data[i-1] != flat_data[i]:  # if not equal, appends current number of runs +1 and number to the list
            total_runs += 1
            rle_data.extend([total_runs, flat_data[i-1]])
            total_runs = 0
    if flat_data[-1] == flat_data[-2]:  # checks for the last number, if equal to second to last, the total runs is
        total_runs += 1  # already stored and able to be added by 1, gets appended to list with respective number
        rle_data.extend([total_runs, flat_data[-1]])
    if flat_data[-1] != flat_data[-2]:  # if not equal to second to last number, the number is appended to list by [1,x]
        rle_data.extend([1, flat_data[-1]])
    return rle_data


def get_decoded_length(rle_data):
    summation = 0
    for i in range(0, len(rle_data), 2):
        summation += int(rle_data[i])
    return summation


def decode_rle(rle_data):
    flat_data = []
    for i in range(0, len(rle_data), 2):
        for j in range(0, rle_data[i]):
            flat_data.append(rle_data[i + 1])
    return flat_data


def string_to_data(data_string):
    flat_data = []
    for i in data_string:
        if i in [str(j) for j in range(10)]:
            flat_data.append(int(i))
        elif i in ['a', 'b', 'c', 'd', 'e', 'f']:
            flat_data.append(ord(i) - 87)
    return flat_data


def to_rle_string(rle_data):
    rle_string = []
    rle_data = [str(i) for i in rle_data]
    for i in range(0, len(rle_data), 2):  # skips every other number in the list
        if rle_data[i] == rle_data[i+1]:  # if the nth number is equal to the next number in the list
            rle_data[i+1] = (chr(int(rle_data[i+1]) + 87))  # change that number into its character code counterpart
    rle_data = ["".join(x) for x in zip(rle_data[0::2], rle_data[1::2])]
    for i in rle_data:
        if len(i) == 2:
            rle_string.append(i)
        elif len(i) == 3:
            if i[2] in ['a', 'b', 'c', 'd', 'e', 'f']:  # appends to list if already formatted
                rle_string.append(i)
            elif i[1:3] in [str(x) for x in range(10, 16)]:  # if first number begins with 2-9, assumes next two is
                i = i.replace(i[1:3], f"{chr(int(i[1:3]) + 87)}")  # double digits and converts last two to character
                rle_string.append(i)  # counterpart
            elif i[0:2] in [str(x) for x in range(10, 16)]:
                rle_string.append(i)
        elif len(i) == 4:
            i = i.replace(i[2:4], f"{chr(int(i[2:4]) + 87)}")
            rle_string.append(i)
    rle_string = ":".join(rle_string)
    return rle_string


def string_to_rle(rle_string):
    new_rle_data = []
    rle_string = rle_string.split(":")
    for i in rle_string:
        if len(i) == 2:
            new_rle_data.append(int(i[0]))
            if i[1] in [str(x) for x in range(0, 10)]:
                new_rle_data.append(int(i[1]))
            elif i[1] in ['a', 'b', 'c', 'd', 'e', 'f']:
                new_rle_data.append(ord(i[1]) - 87)
        elif len(i) == 3:
            new_rle_data.append(int(i[0:2]))
            if i[2] in [str(x) for x in range(0,10)]:
                new_rle_data.append(int(i[2]))
            elif i[2] in ['a', 'b', 'c', 'd', 'e', 'f']:
                new_rle_data.append(ord(i[2]) - 87)
    return new_rle_data


if __name__ == "__main__":
    print("Welcome to the RLE image encoder!\n")
    print("Displaying Spectrum Image:")
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow)
    loaded_image = "empty"
    while True:
        display_menu()
        if menu_option == 0:
            break
        elif menu_option == 1:
            file_name = input("Enter name of file to load: ")
            loaded_image = ConsoleGfx.load_file(file_name)
        elif menu_option == 2:
            loaded_image = ConsoleGfx.test_image
            print("Test image data loaded.")
        elif menu_option == 3:
            rle_data = string_to_rle(input("Enter an RLE string to be decoded: "))
            loaded_image = decode_rle(rle_data)
        elif menu_option == 4:
            rle_data = string_to_data(input("Enter the hex string holding RLE data: "))
            loaded_image = decode_rle(rle_data)
        elif menu_option == 5:
            loaded_image = string_to_data(input("Enter the hex string holding flat data: "))
        elif menu_option == 6:
            print("Displaying image...")
            if loaded_image == "empty":
                print("(no data)")
            else:
                ConsoleGfx.display_image(loaded_image)
        elif menu_option == 7:
            if loaded_image == "empty":
                print("RLE representation: (no data)")
            else:
                print(f"RLE representation: {to_rle_string(encode_rle(loaded_image))}")
        elif menu_option == 8:
            if loaded_image == "empty":
                print("RLE hex values: (no data)")
            else:
                print(f"RLE hex values: {to_hex_string(encode_rle(loaded_image))}")
        elif menu_option == 9:
            if loaded_image == "empty":
                print("Flat hex values: (no data)")
            else:
                print(f"Flat hex values: {to_hex_string(loaded_image)}")
        else:
            print("Error! Invalid input.")
