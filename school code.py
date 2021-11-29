# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 17:49:53 2021

"""

###Here is the data abstraction model





#Give me some items to pack please



#An item as a tuple
#waterBottle = ("waterBottle", 6, 4)



#An item as a list: name, value weight
waterBottle = ["waterBottle", 6, 4]
snackBar = ["ruler",3,7]
torch = [ "torch", 8,3 ]
hat = ["hat", 10, 1]
roleMat =["rolemat",6,9]
tripMap = ["map", 3, 1]
headTorch = ["headTorch", 5, 2]
Stove = ["Stove", 8, 7]
watch = ["watch", 7, 5]
jacket = ["jacket", 5, 2]
clock = ["clock", 6, 1]
#The Knapsack as a list
allItems = []



allItems.append(waterBottle)
allItems.append(snackBar)
allItems.append(torch)
allItems.append(hat)
allItems.append(roleMat)
allItems.append(tripMap)
allItems.append(headTorch)
allItems.append(Stove)
allItems.append(watch)
allItems.append(jacket)
allItems.append(clock)





#How to pack????



itemsByRatio = []
for item in allItems:
    ratio = item[1]/item[2]
    itemsByRatio.append([item[0], ratio])
