#programme jeux du hasard 
#shuffle(liste) melanger les element d'une liste(comme des cartes)
#sample(liste,k) tire au sort k element d'une liste
#end = " " pour espacer a la fin de chaque instrucion 
from random import shuffle,sample

listecarte = ['a','b','c','d','e','f','g','h']
numero = list(range(1,51))
etoile = [1,2,3,4,5,6,7,8,9,10,11]

shuffle(listecarte)
print(listecarte,"\n")

#tirer des element au sort
print("tirage au sort \n")
print(sample(listecarte,3),"\n")

#Extrait EuroMilion

print("Euro Million\n")

print(sample(numero,5))
print(sample(etoile,3))



