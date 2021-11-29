# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 15:52:41 2021

"""
class Item:
    def __init__(self, v, w):
        self.value = v
        self.weight = w

usObjects = [Item(10, 4), Item(2, 15), Item(5, 7), Item(4, 9), Item(2, 1), Item(6, 12)]
wmax = 35
mode = 1 # 1 = can only use each value once. 0 = can use any number of each value

def isSorted(l):
    for i in range(len(l) - 1):
        if l[i].weight > l[i + 1].weight:
            return False
    return True

def sort(l): # bubble sort
    if isSorted(l):
        return l
    for i in range(len(l) - 1):
        if l[i].weight > l[i + 1].weight:
            temp = l[i]
            l[i] = l[i + 1]
            l[i + 1] = temp
    return sort(l)

def checkMax(l, w):
    if len(l) == 0:
        return -1
    if not l[-1].weight > w:
        return len(l) - 1
    return checkMax(l[:-1], w)

def solve():
    objects = sort(usObjects)
    usedObjects = []
    totalValue = 0
    objectValues = []
    wcurrent = wmax
    
    while True:
        loc = checkMax(objects, wcurrent)
        if loc == -1:
            break
        
        usedObjects.append(objects[loc].weight)
        totalValue += objects[loc].value
        objectValues.append(objects[loc].value)
        wcurrent -= objects[loc].weight
        if mode == 1:
            objects.pop(loc)
    
    print("Finished")
    print("Used Weights:", usedObjects)
    print("Free weight:", wcurrent)
    print("Total value:", totalValue)
    print("Used Values:", objectValues)
solve()
