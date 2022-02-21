"""
@author: ozan.geckin
"""

def exponentiationBruce_Force(base,exponent):
   
    res = 1
    
    for i in range(exponent):
     
        res *= base
    
    return res

def exponentiationDivide_And_Conquer(base,exponent):
    
    if exponent == 0:
        return 1
    
    
    if int(exponent % 2) == 0:
       
        return exponentiationDivide_And_Conquer(base*base,int(exponent/2))
  
    else:
      
        return base*exponentiationDivide_And_Conquer(base*base,int(exponent/2))    
    
if __name__=='__main__':
    print("Base : 5 , Exponentiation : 2  ==>",exponentiationBruce_Force(5,2))
    print("Base : 2 , Exponentiation : 5 ==>",exponentiationDivide_And_Conquer(2,5))