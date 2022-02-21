"""
@author: ozan.geckin

 """   
def choseCheese(pi, wi, W):

    index = [0]*len(pi)
    
    ratio = [v/w for v, w in zip(pi, wi)]

    index.sort(key=lambda i: ratio[i], reverse=True)
 
    maxPrice = 0
    cheese = [0]*len(pi)
    for i in index:
        if wi[i] <= W:
            cheese[i] = 1
            maxPrice += pi[i]
            W -= wi[i]
        else:
            cheese[i] = W/wi[i]
            maxPrice += pi[i]*W/wi[i]
            break
 
    return maxPrice, cheese
 

if __name__=='__main__':
    weight = [3,4,5,1,6,9,2]
    price = [2,23,44,21,86,100,10]
    capacity = 10
    p = choseCheese(price,weight,10)
    print(p)
