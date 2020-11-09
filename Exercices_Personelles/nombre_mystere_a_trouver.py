#Programme nombre Mystere ++ 
from random import randint

nom_joueur = input("veuillez entrer votre nom : ")
nb_max_essai = 10
nombremax = 30
nb_jeux = 0
rejouer = "o"

while rejouer != 'n' :
    nb_tentative = 1
    nb_mystere = randint(1,nombremax)
    nb_a_trouver = 0
    print("J'ai choisi un nombre entre 1 et ",nombremax)
    print("A vous",nom_joueur,"de le deviner en ",nb_max_essai," tentatives maximum!")
    print()
    while nb_mystere != nb_a_trouver and nb_tentative <= nb_max_essai:
        print("essai numero ", nb_tentative)
        #eviter les erreurs generer quand l'user rentre autre chose qu'un entier
        while True :
            try :
                nb_a_trouver  = int(input("Entrez le nombre  : "))
                break
            except ValueError :
                print("T'es bete ou quoi ? faut rentrer un entier")
                print()
    
        if nb_a_trouver > nb_mystere :
            print("Ton nombre est  Grand ")
        elif nb_mystere > nb_a_trouver :
            print("Ton nombre est Petit ")
        else :
            print("Bravo",nom_joueur,"Vous avez trouver ",nb_mystere, "en",nb_tentative,"essais")
            
        nb_tentative+=1
        print()
    if nb_tentative > nb_max_essai and nb_mystere != nb_a_trouver :
        print("Desole, vous avez epuisé vos ",nb_max_essai," tentatives en vain")
        print("Le nombre etait : ",nb_mystere)
    nb_jeux +=1
    rejouer=input("Voulez vous rejouer ? o/n : ")
print()

print("Merci et a bientot !")
    
    
    

