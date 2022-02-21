# Author: 1801042103
#         Ozan GECKIN
def polynomial(x,arr):
    res=0
    for i in range(len(arr)):
        res = res + (x ** i)* arr[i]
    return res

print(polynomial(5,[2,6]))