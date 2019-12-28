import sys


def string_adder(x, y):
    # Calculate x^y
    power = int(x)**int(y)
    print(x+'^'+y+" = "+str(power), end="")
    strings_list = []
    number_list = []
    while len(str(power)) > 1:
        # Calculate sum of digits.
        digit_list = [int(i) for i in str(power)]
        power = sum(digit_list)
        strings_list.append(digit_list)
        number_list.append(power)
    # Print output except first part.
    for i in range(len(strings_list)):
        print(str(" = " + str(strings_list[i][0])), end="")
        for j in range(1, len(strings_list[i])):
            print(" + " + str(strings_list[i][j]), end="")
        print(" = " + str(number_list[i]), end="")
    print()


string_adder(sys.argv[1], sys.argv[2])
