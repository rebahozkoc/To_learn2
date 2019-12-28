def input_caller(K):
    list_of_lists = []
    for i in range(K):
        i = input().split()
        for j in i:
            i[i.index(j)] = int(j)
        for k in range(2):
            if not (1 <= i[k] <= 10**7):
                return None
            if not (i[2] == 0 or i[2] == 1):
                return None
        list_of_lists.append(i)
    return list_of_lists

def elimination(a, t, e, N_list):
    person = N_list[0]
    for i in range(t):
        if len(N_list) < 1:
            return -1
        if (a + person) > len(N_list):
            person = (a+person)%len(N_list)
        else:
            person = person + a
    if person%2 != e:
        N_list.remove(person)
    return N_list


def yusyuvarlak():
    list = input().split()
    N = int(list[0])
    K = int(list[1])
    list = input_caller(K)
    N_list = []
    for j in range(1,N+1):
        N_list.append(j)
    for i in range (K):
        N_list = elimination((list[i])[0],(list[i])[1], (list[i])[2], N_list)
        if len(N_list) < 1:
            return -1
    return N_list

def printer(x):
    output = x
    for i in range(len(output)):
        print(output[i]," ", end ='')

printer(yusyuvarlak())
