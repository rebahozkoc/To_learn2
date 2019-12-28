def up_to_n_calculator(n):
    sum_of_odds = 0
    sum_of_evens = 0
    element_count = 0
    for i in range(1,n+1, 2):
        sum_of_odds += i
    for j in range(2, n+1, 2):
        sum_of_evens += j
        element_count += 1
    average = sum_of_evens/element_count
    print("Sum of odd numbers up to", n, "is", sum_of_odds)
    print("Average of even numbers up to", n, "is", average)

up_to_n_calculator(10)


def checker(x):
    if '@' and '.' not in x:
        return False
    else:
        return True


import random
def guessgame():
    aim = random.randint(0, 10)
    try_counter = 0
    x =-1
    while x != aim :
        x = int(input('guess the number'))
        try_counter += 1
        if x > aim:
            print('decrease your number')
        else:
            print('increase your number')
    print('you found it! in ', try_counter, 'guess')

guessgame()



