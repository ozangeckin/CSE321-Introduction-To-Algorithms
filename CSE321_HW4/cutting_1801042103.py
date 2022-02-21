"""
@author: ozan.geckin
"""

def cutting(length,cutCount):
    if length > 1:
        cutCount+=1
        return cutting (length/2,cutCount)
    else:
        return cutCount

if __name__ == '__main__':

    lengt = 12
    print("Minimum number of cuts for",lengt,"length", ":", cutting(lengt, 0))
