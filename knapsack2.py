# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 17:23:58 2021

"""
import random
class Item:
    def __init__(self, value, weight, maxUses=1):
        self.value = value
        self.weight = weight
        self.benefit = 0
        self.uses = 0
        self.maxUses = maxUses
    def use(self):
        self.uses += 1
    def setUses(self, amount):
        self.uses = amount

def isSorted(ls):
    for i in range(len(ls) - 1):
        if ls[i].benefit < ls[i + 1].benefit:
            return False
    return True

def sort(ls):
    if isSorted(ls):
        return ls
    for i in range(len(ls) - 1):
        if ls[i].benefit < ls[i + 1].benefit:
            temp = ls[i]
            ls[i] = ls[i + 1]
            ls[i + 1] = temp
    return sort(ls)

def popLs(n):
    ls = []
    for i in range(n):
        ls.append(Item(random.randint(1, 20), random.randint(1, 10), 1))
    return ls

def calcBenefit(ls):
    for a in ls:
        a.benefit = a.value / a.weight
    return ls

def resetUses(ls):
    for a in ls:
        a.setUses(0)

def debug(item):
    print("Uses:", item.uses)
    print("Value:", item.value)
    print("Weight:", item.weight)
    print("Benefit:", item.benefit)
    input()
def solve(ls, wm):
    wfree = wm
    pack = []
    ok = True
    while ok:
        if wfree == 0 or len(ls) == 0:
            return pack
        for a in ls:
            #debug(a)
            if a.uses == a.maxUses:
                if ls.index(a) == len(ls) - 1:
                    ok = False
                    break
                continue
            elif a.weight > wfree:
                if ls.index(a) == len(ls) - 1:
                    ok = False
                    break
                continue
            else:
                wfree -= a.weight
                pack.append(a)
                a.use()
                break
    return pack

def totalValue(ls):
    val = 0
    for a in ls:
        val += a.value
    return val

def totalWeight(ls):
    wgt = 0
    for a in ls:
        wgt += a.weight
    return wgt

def lowestWeight(ls):
    lw = 0xffffff # a very big number
    for a in ls:
        if a.weight < lw and not a.uses == a.maxUses:
            lw = a.weight
    return lw

def solveRandom(ls, wm):
    wfree = wm
    pack = []
    ok = True
    lw = ls[0].weight
    while ok:
        lw = lowestWeight(ls)
        if lw == 0xffffff:
            break
        if wfree == 0 or len(ls) == 0:
            return pack
        a = ls[random.randint(0, len(ls) - 1)] # not very efficient but who cares
        if a.uses == a.maxUses:
            continue
        elif a.weight > wfree:
            if a.weight == lw:
                ok = False
                break
            continue
        else:
            wfree -= a.weight
            pack.append(a)
            a.use()
    return pack

def normal():
    WMAX = 30
    objects = sort(calcBenefit(popLs(10)))
    print("Total value:", totalValue(objects))
    print("Total weight:", totalWeight(objects))
    solved = solve(objects, WMAX)
    print("> Calculated value:", totalValue(solved), "<")
    print("> Calulated weight:", totalWeight(solved), "<")
    total = 0
    maxValue = 0
    maxValueItems = []
    times = 0
    combinations = 1
    for j in range(1000):
        resetUses(objects)
        solvedRandom = solveRandom(objects, WMAX)
        c = totalValue(solvedRandom)
        if c > maxValue:
            maxValueItems = [solvedRandom]
            maxValue = c
            combinations = 1
            times = 1
        elif c == maxValue:
            times += 1
            try:
                maxValueItems.index(solvedRandom)
            except ValueError:
                combinations += 1
                maxValueItems.append(solvedRandom)
        total += c
    mean = total / 1000
    print("Average random value:", mean)
    print("> Max random value:", maxValue, "<")
    print("Number of times max value achieved:", times)
    print("Combinations for max value:", combinations)
    if maxValue > totalValue(solved):
        print("Random value is greater than calculated value.")
def sci():
    WMAX = 30
    examineSolved = []
    examineRandom = []
    for k in range(2, 70, 2):
        print("Iteration", int(k / 2))
        objects = sort(calcBenefit(popLs(k)))
        solved = solve(objects, WMAX)
        maxValue = 0
        for j in range(10000):
            resetUses(objects)
            solvedRandom = solveRandom(objects, WMAX)
            c = totalValue(solvedRandom)
            if c > maxValue:
                maxValue = c
        examineSolved.append(totalValue(solved))
        examineRandom.append(maxValue)
    breakpoint()
normal()
