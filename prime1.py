
start_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
left_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
startpoints = []
endpoints = []
fulllist = []

def isprime(x):
    if x < 2:
        return False
    else:
        for n in range (2, x):
            if x % n == 0:
                return False
            return True

def initialize(lst):
    while True:
        if len(lst) > 0:
            tested_num = lst.pop(0)
            if isprime(tested_num):
                startpoints.append(tested_num)
                fulllist.append(tested_num)
        else:
            break

def add_left(lst):
    for i in lst:
        for left in left_list:
            new_num = int(str(left) + str(i))
            if isprime(new_num):
                pass



initialize(start_list)
add_left(startpoints)

print("startlist:   ", start_list)
print("startpoints: ", startpoints)
print("endpoints:   ", endpoints)
print("fulllist:    ", fulllist)

