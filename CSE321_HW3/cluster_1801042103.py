# Author: 1801042103
#         Ozan GECKIN
import sys

#Return maxProfit returns the first index and last index of the substring. 
#I wrote down the values in the table in the assignment.
#Starting index 2, end index 5 when we look at the output table, we see that it is (C-D-E-F).
#5.1
def findCluster(intArr):
    startIndex = 0
    lastIndex = 0
    maxProfit = 0
    res = -sys.maxsize

    for i in range(len(intArr)):
        maxProfit = intArr[i]
        for j in range(i+1,len(intArr)):
            maxProfit += (intArr[j])
            if res < maxProfit:
                res = maxProfit
                startIndex = i
                lastIndex = j
                
    return res,startIndex,lastIndex


res,startIndex,lastIndex=findCluster([3,-5,2,11,-8,9,-5])

print("Maximum Profit :",res)
print("Start Index : ",startIndex)
print("Last Index : ",lastIndex)

#5.2
# Return maximum of following three possible cases
def maximumProfit(arr, start, last):
	
	if (start == last): # Base case only one element
		return arr[start]

	middle = (start + last) // 2 # Find middle point

	return max(maximumProfit(arr, start, middle),maximumProfit(arr, middle+1, last),maxCrossingSum(arr, start, middle, last))

# Return sum of elements on left and right of mid
def maxCrossingSum(arr, start, middle, last):
	
	temp = 0
	left_sum = -10000

	for i in range(middle, start-1, -1):# Include elements on left of mid.
		temp = temp + arr[i]

		if (temp > left_sum):
			left_sum = temp

	temp = 0
	right_sum = -1000
	for i in range(middle + 1, last + 1):# Include elements on right of mid
		temp = temp + arr[i]

		if (temp > right_sum):
			right_sum = temp

	return max(left_sum + right_sum, left_sum, right_sum)


arr = [3,-5,2,11,-8,9,-5]
size = len(arr)

maxPorfit = maximumProfit(arr, 0, size-1)
print("Maximum Porfit: " , maxPorfit)


