#programme palindrome

from math import sqrt

def estpremier(nombre) :
    k = int(sqrt(nombre))
    for i in range(2,k+2) :  
        if(nombre%i == 0):
            return False
        return True

def somchiffre(nombre) :
    r = 1
    p = 0
    beta = nombre
    while beta >= 1 :
        r = int(beta % 10)
        beta = beta/10
        p = p + r
    return p

def change(nombre) : 
    nb = str(n)
    ch = ""
    for k in range(0,len(nb)) :
        ch = nb[k] + ch
    res = int(ch)
    return res

n = 10000
while (change(n) != n or somchiffre(n)!= 19 or estpremier(n) == False):
#while not (change(n) == n and somchiffre(n)== 19 and estpremier(n)):
    n=n+1
    

print("le plus petit nombre premier palindrome est ", n)

