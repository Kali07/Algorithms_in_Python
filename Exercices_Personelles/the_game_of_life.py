#Jeux de la vie
from random import *

def afficher(tab) :
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=' ')
        print()

def voisin (tab,i,j):
    return (tab[i-1,j-1] + tab[i-1,j]+
            tab[i-1,j+1] + tab[i,j-1]+
            tab[i,j+1] + tab[i+1,j-1]+
            tab[i+1,j] + tab[i+1,j+1])

def operation (tab) :
    cp = tab
    for i in range (len(tab[0])):
        for j in range(len(tab[1])):
            #c = voisin(cp, i,j)
            if((tab[i][j] == 1 and c == 2) or c == 3):
                tab[i][j] = 1
            else :
                tab[i][j] = 0

#N = int(input("entrez la taille du tableau ... "))
N = 4
copie = []
a = [[randint(0,1) for x in range(N)],
     [randint(0,1) for x in range(N)]]
copie = a

"""for i in range(len(a)):
    for j in range(len(a[i])):
        #print("[",i,"]","[",j,"]=",a[i][j], end=' ')
        voisin(a,i,j)
    print()"""


afficher(a)
print()
operation(a)
print()
afficher(a)
print()
afficher(copie)

#print([[random.randint(0, 1) for x in range(10)] for y in range(10)])
