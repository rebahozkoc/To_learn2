import sys


def diamond_comprehension(x):
    for i in range(1, x+1):
        temp_list = [" " for m in range(x-i)] + ["*" for n in range(2*i-1)]
        print("".join(temp_list))
    for k in range(x-1, 0, -1):
        temp_list = [" " for p in range(x-k)] + ["*" for o in range(2*k-1)]
        print("".join(temp_list))


diamond_comprehension(int(sys.argv[1]))
