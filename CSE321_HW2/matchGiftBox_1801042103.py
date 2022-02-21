#Author: 1801042103
#        Ozan GECKIN

def matchs(gifts, boxs, low, high):
    if (low < high):
        pivot = partition(gifts, low, high, boxs[high])
        partition(boxs, low, high, gifts[pivot])
        matchs(gifts, boxs, low, pivot - 1)
        matchs(gifts, boxs, pivot + 1, high)


def partition(arr, low, high, pivot):
    i = low
    j = low
    while j < high:
        if (arr[j] < pivot):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        elif (arr[j] == pivot):
            arr[j], arr[high] = arr[high], arr[j]
            j -= 1
        j += 1
    arr[i], arr[high] = arr[high], arr[i]
 
    return i
 
def display(arr,arr2,size):
    print("Gifts(Size)  Boks(Size)")
    for i in range(size):
        print(arr[i],"          ",arr2[i])
    print()
 
if __name__ == "__main__":
 
    gifts_size = [5,7,4,3,9]
    boxs_size = [3,4,9,5,7]
    print("UNPAIRED STATE\n")
    display(gifts_size,boxs_size,5)
    matchs(gifts_size, boxs_size, 0, 4)
    print("PAIRED STATE\n")
    display(gifts_size,boxs_size,5)
 
