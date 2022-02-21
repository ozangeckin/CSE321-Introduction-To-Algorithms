"""
@author: ozan.geckin
"""
import sys

def findWorstBest(arr, left, right, min, max):
   
    if left == right:               
        
        if min > arr[right]:          
            min = arr[right]
 
        if max < arr[left]:           
            max = arr[left]
 
        return min, max
 
 
    if right - left == 1:           
 
        if arr[left] < arr[right]:      
            if min > arr[left]:       
                min = arr[left]
 
            if max < arr[right]:      
                max = arr[right]
 
        else:
            if min > arr[right]:      
                min = arr[right]
 
            if max < arr[left]:       
                max = arr[left]
 
        return min, max
 
    mid = (left + right) // 2
    min, max = findWorstBest(arr, left, mid, min, max)
    min, max = findWorstBest(arr, mid + 1, right, min, max)
 
    return min, max

if __name__ == '__main__':
    
    successRates = [8,3,5,3,2,24,7,1,6,9]
    
    min=sys.maxsize
    max=-sys.maxsize
    minSuccessRates ,maxSuccessRates = findWorstBest(successRates,0,len(successRates)-1,min,max)
    print("Minimum success rates: ", minSuccessRates)
    print("Maximum success rates: ", maxSuccessRates)