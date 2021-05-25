import random
import math
import sys
import numpy as np

people = {  
    "tom" : 1, "ted": 1, "tim": 1, "toni": 1, "tex": 1, 
    "sue": 0, "sara": 0, "shelly":0, "sienna" : 0, "selina":0}

members = {  
    1:"bob", 2:"ted", 3:"tim", 4:"toni", 5:"tex", 
    6:"alice", 7:"sara", 8:"shelly", 9:"sienna", 10:"selina"}

def compute_sum(k, choices):
    sum_total = 0
    for _ in range(k):
        while True:
            ind = math.ceil(random.random() * 10)
            if ind in choices:
                val = choices.pop(ind)
                sum_total += val
                break
    return sum_total
        

def alice_bob(k, members):
    people = set()
    for _ in range(k):
        while True:
            ind = math.ceil(random.random() * 10)
            if ind in members:
                person = members.pop(ind)
                people.add(person)
                break
    return set(['alice', 'bob']).issubset(people)

def countdown(num):
    while num > 0:
        amount = compute_sum(k, {1:1,2:1,3:1,4:1,5:1,6:0,7:0,8:0,9:0,10:0})
        yield amount
        num -= 1

def alice_bob_countdown(num):
    while num > 0:
        new_members = members.copy()
        boo = alice_bob(k, new_members)
        yield boo
        num -= 1


if __name__ == '__main__':

    #choices = {1:1,2:1,3:1,4:1,5:1,6:0,7:0,8:0,9:0,10:0}
    n = int(sys.argv[1])
    k = int(sys.argv[2])

    tot_sum = 0
    l = []
    l = list(countdown(n))

    #print(tot_arr)
    #matches = np.where(tot_arr == 2).size
    #print(type(np.where(tot_arr == 2)))
    #print(np.where(tot_arr == 2))
    #print(type(g))

    
    # tot_size = len(l) 
    # s_l = len(list(filter(lambda a: a ==2,l)))
    # print(s_l / tot_size)

    ## more women than men 
    # tot_size = len(l) 
    # s_l = len(list(filter(lambda a: a in [1,0],l)))
    # print(s_l / tot_size)

    #at least one man
    # tot_size = len(l) 
    # s_l = len(list(filter(lambda a: a >= 1,l)))
    # print(s_l / tot_size)

    #alice and bob
    l = list(alice_bob_countdown(n))
    tot_size = len(l) 
    s_l = len(list(filter(lambda a: a,l)))
    print(s_l / tot_size)