from console_gfx import ConsoleGfx

def display_menu(): # prints the display menu
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
    menu_option = int(input("Enter your Menu Option: "))

def to_hex_string(data):
    hex_string_list = []
    for i in data:
        if 0 <= i <= 9:
            hex_string_list.append(str(i))
        elif 10 <= i <= 15:
            hex_string_list.append(chr(i + 55).lower())
    return "".join(hex_string_list)

def count_runs(flat_data):
    count_runs_list = []
    for i in flat_data:
        if i not in count_runs_list:
            count_runs_list.append(i)
    return len(count_runs_list)

def encode_rle(flat_data):
    flat_data_compressed = []
    for i in range(16,1,-1):
        if i in flat_data:
            flat_data_compressed.append(flat_data.count(i))
            flat_data_compressed.append(i)
    return flat_data_compressed

def get_decoded_length(rle_data):
    sum = 0
    for i in range (0, len(rle_data),2):
        sum += int(rle_data[i])
    return sum

def decode_rle(rle_data):
    rle_data_decompressed = []
    for i in range (0, len(rle_data),2):
        for j in range (0,rle_data[i]):
            rle_data_decompressed.append(rle_data[i+1])
    return rle_data_decompressed

def string_to_data(data_string):
    data_string_list = []
    for i in range (0, len(data_string),2):
        data_string_list.append(int(data_string[i]))
        if data_string[i+1] in ['0','1','2','3','4','5','6','7','8','9']:
            data_string_list.append(int(data_string[i+1]))
        elif data_string[i+1].upper() in ['A','B','C','D','E','F']:
            data_string_list.append(ord(data_string[i+1].upper()) - 55)
    return data_string_list

def to_rle_string(rle_data):
    rle_string_list = []
    for i in range(0,len(rle_data),2):
        P1 = str(rle_data[i])
        if rle_data[i] == rle_data[i+1]:
            P2 = chr(rle_data[i+1]+87)
        else:
            P2 = str(rle_data[i+1])
        rle_string_list.append(P1 + P2)
    return ":".join(rle_string_list)

def string_to_rle(rle_string):
    string_list = []
    rle_string = rle_string.split(":")
    print(rle_string)
    print(rle_string[0][0])
    for i in range(rle_string):
        if len(rle_string[i]) == 2

if __name__ == "__main__":
    print("Welcome to the RLE image encoder!\n")
    print("Displaying Spectrum Image:")
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow)
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
            True
        elif menu_option == 4:
            True
        elif menu_option == 5:
            True
        elif menu_option == 6:
            print("Displaying image...")
            ConsoleGfx.display_image(loaded_image)
        elif menu_option == 7:
            True
        elif menu_option == 8:
            True
        elif menu_option == 9:
            True
string_to_rle("15f:64")