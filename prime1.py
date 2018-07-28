import math


start_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
left_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
startpoints = []
endpoints = []
fulllist = []

def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range (2, x):
            print("test: ", x % n)
            if x % n == 0:
                return False
            return True

def initialize(lst):
    while True:
        if len(lst) > 0:
            tested_num = lst.pop(0)
            if is_prime(tested_num):
                startpoints.append(tested_num)
                fulllist.append(tested_num)
        else:
            break

def add_left(lst):
    for i in lst:
        for left in left_list:
            new_num = int(str(left) + str(i))
            if is_prime(new_num):
                print(new_num, " is prime?  ", is_prime(new_num))



initialize(start_list)
add_left(startpoints)

print("startlist:   ", start_list)
print("startpoints: ", startpoints)
print("endpoints:   ", endpoints)
print("fulllist:    ", fulllist)

