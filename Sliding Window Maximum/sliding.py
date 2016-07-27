#!/bin/bash
#https://leetcode.com/problems/sliding-window-maximum/
#The time complexity would be O(n * k), in best case O(n) (k = 1), and worst O(n^2) (k = n)
def sliding(array, k):
    maxarray = [None] * (len(array) - k + 1)
    i = 0
    while i < len(array):
        minpos = max(0, i - k + 1)
        maxpos = i
        j = minpos
        while j <= maxpos and j < len(maxarray):
            if maxarray[j] < array[i]:
                maxarray[j] = array[i]
            j += 1
        i += 1
    print 'output', maxarray

array=[1,3,-1,-3,5,3,6,7]
k = 3
print 'input', array, k
sliding(array, k)
