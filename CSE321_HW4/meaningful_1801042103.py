"""
@author: ozan.geckin
"""
def partition(arr, left, right):

    x = arr[right]
    i = left
    for j in range(left, right):
        if (arr[j] <= x):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i

def meaningful(arr, left, right, k):

    if (k > 0 and k <= right - left + 1):
    
        index = partition(arr, left, right)
        if (index - left == k - 1):
            return arr[index]
        if (index - left > k - 1):
            return meaningful(arr, left, index - 1, k)

        return meaningful(arr, index + 1, right, k - index + left - 1)

if __name__ == "__main__":
    
    successRates = [8,3,5,3,2,24,7,1,6,9]
    k = 3;
    print("K'th success rates : ",meaningful(successRates, 0, len(successRates) - 1, k))

