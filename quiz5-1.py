import sys


def diamond(aim, star, edge):
    if star == 0 and edge:
        return None
    if aim == star:
        line = '{:^' + str(2*aim-1) + '}'
        print(line.format((2*star-1)*"*"))
        return diamond(aim, star-1, True)
    elif not edge:
        line = '{:^' + str(2*aim-1) + '}'
        print(line.format((2*star-1)*"*"))
        return diamond(aim, star+1,False)
    else:
        line = '{:^' + str(2*aim-1) + '}'
        print(line.format((2*star-1)*"*"))
        return diamond(aim, star-1, True)


diamond(int(sys.argv[1]), 1, False)
