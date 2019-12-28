def f():
    input_string = "17:3:15:-6|25:42:18:36|45:3:9:8"
    delimeter = "|"
    input_list = input_string.split(delimeter)
    list_number = 1
    total_sum = 0
    for i in input_list:
        colon = ":"
        line_list = i.split(colon)
        line_sum = 0
        for j in line_list:
            if int(j)%3 == 0:
                line_sum += int(j)
        total_sum += line_sum
        print(str(list_number) + ". line:  " + str(line_sum))
        list_number += 1
    print("Sums     ",total_sum)


f()
