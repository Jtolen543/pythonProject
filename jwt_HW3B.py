def to_hex_string(data):
    hex_string_list = []
    for i in data:
        if 0 <= i <= 9:
            hex_string_list.append(str(i))
        elif 10 <= i <= 15:
            hex_string_list.append(chr(i + 55).lower())
    return "".join(hex_string_list)

def count_runs(flat_data):
    count = 0
    for i in range(len(flat_data)-1):
        if flat_data[i] == flat_data[i+1]:
            count += 1
            if count == 4:
                consecutive = True
                break
        else:
            count = 0
        consecutive = False
    total_runs = 0
    if consecutive == True:
        for i in range(0,16):
            runs = flat_data.count(i)
            if i in flat_data:
                if runs % 15 == 0:
                    total_runs += runs // 15
                else:
                    total_runs += runs // 15 + 1
    elif consecutive == False:
        for i in flat_data:
            total_runs += 1
    return total_runs

def encode_rle(flat_data):
    count = 0
    repeat_list = []
    compressed_list = []
    for i in range(len(flat_data)-1):
        if flat_data[i] == flat_data[i+1]:
            count += 1
            if count == 4:
                consecutive = True
                break
        else:
            count = 0
        consecutive = False
    if consecutive == True:
        for i in flat_data:
            if i not in repeat_list:
                repeat_list.append(i)
                x = flat_data.count(i)
                if x < 15:
                    compressed_list.extend([flat_data.count(i),i])
                elif x > 15:
                    while x > 15:
                        compressed_list.extend([15,i])
                        x -= 15
                    compressed_list.extend([x,i])
    elif consecutive == False:
        for i in flat_data:
            compressed_list.append(1)
            compressed_list.append(i)
    return compressed_list

def get_decoded_length(rle_data):
    sum = 0
    for i in range (0, len(rle_data),2):
        sum += int(rle_data[i])
    return sum

def decode_rle(rle_data):
    decode_list = []
    for i in range(0,len(rle_data),2):
        for j in range(0,rle_data[i]):
            decode_list.append(rle_data[i+1])
    return decode_list

def string_to_data(data_string):
    data_string_list = []
    for i in data_string:
        if i in [str(j) for j in range(10)]:
            data_string_list.append(int(i))
        elif i in ['a','b','c','d','e','f']:
            data_string_list.append(ord(i)-87)
    return data_string_list