#programme Pierre, Feuille, Ciseaux

from random import randint

#fonction Ecrire
def ecrire(nombre):
    if nombre == 1 :
        print("PIERRE\n",end=" ")
    elif nombre == 2 :
        print("FEUILLE\n",end=" ")
    else :
        print("CISEAUX\n",end=" ")

def augmenter_score(mon_tour, ton_tour) :
    global mon_score, ton_score
    if mon_tour == 1 and ton_tour == 2 :
        ton_score +=1
    elif mon_tour == 2 and ton_tour == 1 :
        mon_score +=1
    elif mon_tour == 1 and ton_tour == 3 :
        mon_score +=1
    elif mon_tour == 3 and ton_tour == 1 :
        ton_score +=1
    elif mon_tour == 3 and ton_tour == 2 :
        mon_score += 1
    elif mon_tour == 2 and ton_tour == 3 :
        ton_score += 1

ton_score = 0
mon_score = 0
joueur1 = input("Entrez votre nom : ")
joueur2 = input("Entrez votre nom : ")

limite = 5
print()
print("Pierre - Feuille - Ciseaux : Le premier a",limite,"a gagné \n!")

while mon_score < limite and ton_score < limite  :
    ton_tour = int(input("1: Pierre  2 : Feuille 3 : Ciseaux ?\n"))
    while ton_tour < 1 or ton_tour > 3 :
        ton_tour = int(input("1: Pierre  2 : Feuille 3 : Ciseaux ?\n"))
    ecrire(ton_tour)
    print(joueur1,"ton tour ")
    
    
    mon_tour =int(input("1: Pierre  2 : Feuille 3 : Ciseaux ?\n")) 
    ecrire(mon_tour)
    print(joueur2,"ton tour")
    
    augmenter_score(ton_tour,mon_tour)
    print(ton_score,"points pour",joueur2,"et ",mon_score,"points pour",joueur1)
    
    

    
