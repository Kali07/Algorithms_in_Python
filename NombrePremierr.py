#programme qui determinne si un nombre est premier ou pas

from math import sqrt

nombre = float(input("Entrez le nombre voulu __ "))
k = int(sqrt(nombre))
premier = 1
for i in range(2,k+2) :  
    if(nombre%i == 0):
        premier = 0
if(premier == 1):
    print("est un nombre premier")
else:
    print("pas un nombre premier")

    
