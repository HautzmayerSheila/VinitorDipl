
def find_max(number_list):
    biggest_num = 0
    for num in number_list:
        if num > biggest_num:
            biggest_num = num
    return biggest_num