#programme jeux du hasard 
#randint(a,b) renvoi un nombre aleatoire compris entre a et b
#end = " " pour espacer a la fin de chaque instrucion 
from random import choice,randint

listeDe = [1,2,3,4,5,6]
for i in range(100) :
    print(choice(listeDe),end=" ")
    
"""
sommeDe = 0
print("Lancement des de")
for i in range(3):
    jet = randint(1,6)
    print(jet,end=" ")
    sommeDe = sommeDe + jet
print("la somme est de",sommeDe)

"""
