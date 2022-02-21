"""
@author: ozan.geckin
"""

def candy(maxLength, length, price, n):
    K = [[0 for x in range(maxLength + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for j in range(maxLength + 1):
            if i == 0 or j == 0:
                K[i][j] = 0
            elif length[i-1] <= j:
                K[i][j] = max(price[i-1]
                          + K[i-1][j-length[i-1]],  
                              K[i-1][j])
            else:
                K[i][j] = K[i-1][j]

    return K[n][maxLength]

if __name__=='__main__':
    length = [1,2,3,4,5,6,7,8]
    price = [1,5,8,9,10,17,17,20]
    maxLength = 8
    n = len(length)
    print("Max profit :",candy(maxLength, length,price, n))

