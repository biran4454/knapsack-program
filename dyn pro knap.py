# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 17:31:37 2021
"""

#Knapsack Problem
#coded with help from https://www.youtube.com/watch?v=cJ21moQpofY

CAPACITY = 7

class Item:
    def __init__(self, value, cost):
        self.v = value
        self.c = cost

item0 = Item(0,0)
item1 = Item(2, 3)
item2 = Item(2, 1)
item3 = Item(4, 3)
item4 = Item(5, 4)
item5 = Item(3, 2)

allItems = [item0, item1, item2, item3, item4, item5]

table = []
for row in range(0, len(allItems)):
    newRow = []
    for column in range(0, CAPACITY+1):
        if (row == 0) or (column == 0):
            newRow.append(0)
        else:
            newRow.append(None)
    table.append(newRow)

for itemNo in range(1, len(allItems)):
    for stateNo in range(0, CAPACITY+1):
        if (allItems[itemNo].c <= stateNo):
            matchingBestState = stateNo - allItems[itemNo].c
            potentialBestValue = allItems[itemNo].v + table[itemNo-1][matchingBestState]
            table[itemNo][stateNo] = max(potentialBestValue, table[itemNo-1][stateNo])
        else:
            table[itemNo][stateNo] = table[itemNo-1][stateNo]

def printTable():
    for row in range(0, len(table)):
        for column in range(len(table[row])):
            print(table[row][column], end=' ' )
        print()

printTable()
