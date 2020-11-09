#Jeux de cartes Hearthstone

from random import randint

ok = False  # sera True si on tire autre chose qu'une commune
for x in range(5):
    if randint(1,100)==1:
        print("L",end=" ")
        ok = True
    elif randint(1,100)<=5:
        print("E",end=" ")
        ok = True
    elif randint(1,100)<=28:
        print("R",end=" ")
        ok = True
    else:
        print("C",end=" ")
        
if not ok :
    print("Paquet non valide : que des communes")
   

