def cluster(station,n):
    
    nextMax =station[0]
    currMax = station[0]
    
    for i in range(1,n):
        currMax = max(station[i], currMax + station[i])
        nextMax = max(nextMax,currMax)
        
    return nextMax

if __name__ == '__main__':
    station = [3, -5, 2, 11, -8, 9, -5]
    print("Maximum  profit :" , cluster(station,len(station)))
