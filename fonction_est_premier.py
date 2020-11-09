#programme qui determinne si un nombre est premier ou pas

from math import sqrt

def estpremier(nombre) :
    k = int(sqrt(nombre))
    for i in range(2,k+2) :  
        if(nombre%i == 0):
            return False
    
        return True


#appel de la fonction
        
print(estpremier(17))
    
