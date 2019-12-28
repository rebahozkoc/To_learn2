# First exercise

def greatest(liste):
    if len(liste) == 1:
        return liste[0]
    elif float(liste[0]) > float(liste[-1]):
        return greatest(liste[:-1])
    else:
        return greatest(liste[1:])


print(greatest(["34", "11", "42", "3", "16", "7"]))


# Second exercise
def counter(liste, depth, depth_list):
    for i in liste:
        if type(i) == list:
            depth += 1
            depth_list.append(counter(i, depth, depth_list))
    return depth


def main(liste):
    depth_list_result = []
    counter(liste, 0, depth_list_result)
    return max(depth_list_result)


print(main([["1","4", "7"], "a", ["b",["t",["9","1", ["u","1"], "9"],"3"]],"r"]))
