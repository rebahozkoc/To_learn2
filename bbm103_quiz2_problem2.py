import sys


def problem2(x):
    input_list_str = x.split(",")
    input_list = []
    print("inliststr:", input_list_str)
    e = []
    sum_of_even_numbers = 0
    sum_of_all_numbers = 0
    for i in input_list_str:
        if int(i) > 0:
            input_list += [int(i)]
            print("inputlist:",input_list)
            sum_of_all_numbers += int(i)
            sum_of_all_numbers = sum_of_all_numbers + int(i)
        if int(i) % 2 == 0 and int(i) > 0:
            e = e + [int(i)]
            print("e",e)
            sum_of_even_numbers += int(i)
    even_number_rate = sum_of_even_numbers/ sum_of_all_numbers
    even_string = "\"" + str(e[0])
    print(even_string)
    for i in range(len(e)-1):
        even_string = even_string + ", " + str(e[i+1])
        print("evenstring:",even_string)
    even_string = even_string + "\""
    print("Even Numbers:", even_string)
    print("Sum of Numbers:", sum_of_even_numbers)
    print("Even Number Rate:", round(even_number_rate, 3))


problem2(sys.argv[1])
