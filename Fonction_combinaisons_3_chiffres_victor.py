#programme imprime par ordre croissants etc..
"""
from math import sqrt

def estpremier(nombre) :
    k = int(sqrt(nombre))
    for i in range(2,k+2) :  
        if(nombre%i == 0):
            return False
    
        return True


#appel de la fonction
        
print(estpremier(17))
"""
for i in range (0,8):
    for j in range (i+1,9):
        for k in range (j+1,10):
            print(i,j,k,',')
            
