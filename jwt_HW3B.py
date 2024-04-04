def to_hex_string(data):
    hex_string_list = []
    for i in data:
        if 0 <= i <= 9:
            hex_string_list.append(str(i))
        elif 10 <= i <= 15:
            hex_string_list.append(chr(i + 55).lower())
    return "".join(hex_string_list)


def count_runs(flat_data):
    total_runs = 0
    count = 0
    for i in range(1, len(flat_data)):
        if flat_data[i-1] == flat_data[i]:  # checks if the first number is equal to the next number in list
            count += 1  # adds one to the count
            if count == 15:  # if the count reaches 15 it adds to the total runs and restarts the count
                total_runs += 1
                count = 0
        elif flat_data[i-1] != flat_data[i]:  # if not equal to next number in list, restarts the count and adds to runs
            count = 0
            total_runs += 1
    if flat_data[-1] == flat_data[-2]:  # essentially here for clarify, but after it reaches the last number in the list
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
    sum = 0
    for i in range(0, len(rle_data), 2):
        sum += int(rle_data[i])
    return sum


def decode_rle(rle_data):
    decode_list = []
    for i in range(0, len(rle_data), 2):
        for j in range(0, rle_data[i]):
            decode_list.append(rle_data[i + 1])
    return decode_list


def string_to_data(data_string):
    data_string_list = []
    for i in data_string:
        if i in [str(j) for j in range(10)]:
            data_string_list.append(int(i))
        elif i in ['a', 'b', 'c', 'd', 'e', 'f']:
            data_string_list.append(ord(i) - 87)
    return data_string_list


