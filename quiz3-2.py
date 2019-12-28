import sys
def lucky_numbers(string):
    number_list_str = string.split(",")
    # Remove numbers less than or equal to zero.
    number_list = [int(i) for i in number_list_str if int(i) > 0]
    # Remove duplicates.
    number_list = list(set(number_list))
    # Sort in ascending order.
    number_list.sort()
    # Remove every second element.
    number_list = list(filter(lambda x: number_list.index(x) % 2 == 0, number_list))
    lucky_number = number_list[1]
    lucky_index = 1
    # Remove every lucky number'th element.
    while lucky_number <= len(number_list):
        number_list = list(filter(lambda x: (number_list.index(x)+1) % lucky_number != 0 or x == 1, number_list))
        lucky_index += 1
        lucky_number = number_list[lucky_index]
    # Print output.
    print(*number_list)


lucky_numbers(sys.argv[1])
