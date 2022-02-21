# Author: 1801042103
#         Ozan GECKIN
import math
import sys

#Return distance between two points
def Distance(p1, p2):
    res = 0
    for i in range(len(p1)):
        res = res + (p1[i]**2 - p2[i]**2)
    if res < 0:
        res = res * -1
    return math.sqrt(res)

#Return Closest with Brute Force algorithm
def BruteClosestDistance(pArr):
    min_value = sys.maxsize
    for i in range(len(pArr)):
        for j in range(i+1,len(pArr)):
            if(Distance(pArr[i],pArr[j])< min_value):
                min_value=Distance(pArr[i],pArr[j])
    return min_value


print(BruteClosestDistance([(1,0,0,0),(1,1,0,1),(2,1,2,2),(3,2,3,3),(4,4,3,4)]))