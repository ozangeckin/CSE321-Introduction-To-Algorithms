"""
@author: ozan.geckin
"""

def find_rop(arr, n):
    tempArr = [0]*n
    return mergeSort(arr, tempArr, 0, n-1)


def mergeSort(arr, tempArr, left, right):

    count = 0

    if left < right:

        mid = (left + right)//2

        count += mergeSort(arr, tempArr, left, mid)

        count += mergeSort(arr, tempArr, mid + 1, right)
 
        count += merge(arr, tempArr, left, mid, right)
    
    return count


def merge(arr, tempArr, left, mid, right):
    i = left     
    j = mid + 1  
    k = left     
    count = 0

    while i <= mid and j <= right:

        if arr[i] <= arr[j]:
            tempArr[k] = arr[i]
            k += 1
            i += 1
        else:
            tempArr[k] = arr[j]
            count += (mid-i + 1)
            k += 1
            j += 1

    while i <= mid:
        tempArr[k] = arr[i]
        k += 1
        i += 1

    while j <= right:
        tempArr[k] = arr[j]
        k += 1
        j += 1

    for z in range(left, right + 1):
        arr[z] = tempArr[z]

    return count

if __name__ == '__main__':

    arr = [1, 7, 2, 4, 6]
    inversionsNumber = find_rop(arr,len(arr))
    print("Counter of inversions : ", inversionsNumber)

