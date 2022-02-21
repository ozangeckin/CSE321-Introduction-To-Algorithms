# Author: 1801042103
#         Ozan GECKIN
def counterSubstring(txt,start,end):
    counter = 0
    
    for i in range(len(txt)):
        if(txt[i] == start):
            for j in range(i + 1,len(txt)):
                if(txt[j] == end):
                    counter += 1
    return counter

print(counterSubstring("TXZXXJZWX",'X','Z'))