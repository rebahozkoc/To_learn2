# DİKKAT DİKKAT!!!!

# 500 liralık kod!!!!


test = [3,7,4,5]

def solution(A):
    firstlist =A[:]
    solution1 = 0
    # A>b
    for i in range(0, len(firstlist)-1, 2):
        try:
            if firstlist[i] < firstlist[i+1]:
                firstlist[i+1] = 0
                solution1 += 1
            if firstlist[i+1] > firstlist[i+2]:
                firstlist[i+1] = 0
                solution1 += 1
        except IndexError:
            solution1 -=1
    print("sol1", solution1)

    solution2 = 0
    # A< b
    for i in range(0, len(A)-1, 2):
        try:
            if A[i] > A[i+1]:
                print("sol2 if1", i, A[i], A[i+1])
                A[i+1] = 0
                solution2 += 1
            if A[i+1] < A[i+2]:
                print("sol2 if2", i+1, A[1+1], A[i+2])
                print(A)
                A[i+2] = 0
                solution2 += 1
        except IndexError:
            continue
    print("sol2", solution2)
    return min(solution1, solution2)

print(solution(test))

