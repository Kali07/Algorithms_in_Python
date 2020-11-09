#Nombre mystere du Coté de  l'ordinateur

from random import randint

debut = 1
fin = 30
essai_max = 5
tentative = 1
aide = 3 #pour nous permettre de lui repondre
print()
print("Choisissez un nombre entre ",debut,"et",fin)
print("et moi je vais essayer de le deviner en ",essai_max,"tentatives")
print()
input("tapez 'entrer' pour commencer")

while aide > 0 and tentative <= essai_max :
    print("essai n° ",tentative)
    if tentative == 1 :
        mon_nombre = randint(debut,fin)
        print("je propose",mon_nombre)
    else :
        mon_nombre = (debut+fin)//2
        print("je propose",mon_nombre)
    while True :
        try:
            aide = int(input("Trouve(0), trop grand(1) ou trop petit (2) ?"))
            break
        except ValueError :
            print("Reponse non valide, reessayez")
    if aide == 1 :
        fin = mon_nombre - 1
    elif aide == 2 :
        debut = mon_nombre + 1
    else :
        print("C'est le bon")
        tentative -=1
    tentative +=1
    
if tentative > essai_max and aide > 0 :
    print("Zut, j'ai gaspillé toutes mes",essaie_max,"tentatives")


    
