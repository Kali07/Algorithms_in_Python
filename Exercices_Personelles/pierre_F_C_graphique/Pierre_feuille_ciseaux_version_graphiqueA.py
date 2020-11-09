#from fonctions_pfc_gpq import *

#pierre feuille ciseau version graphique
#joueur VS Ordinateur

from random import randint
from tkinter import *  #biblioteque qui permet de faire des graphiques





def augmenter_scores(mon_coup,ton_coup):
    global mon_score, ton_score
#ton_coup : moi
    #mon_coup : ordinateur
    
    if mon_coup == 1 and ton_coup == 2:
        ton_score += 1
    elif mon_coup == 2 and ton_coup == 1:
        mon_score += 1
    elif mon_coup == 1 and ton_coup == 3:
        mon_score += 1
    elif mon_coup == 3 and ton_coup == 1:
        ton_score += 1
    elif mon_coup == 3 and ton_coup == 2:
        mon_score += 1
    elif mon_coup == 2 and ton_coup == 3:
        ton_score += 1
        
def jouer(ton_coup):
    
    global mon_score, ton_score, score1, score2
    mon_coup = randint(1,3) 
    if mon_coup==1: #mon_coup
        lab3.configure(image=pierre)
    elif mon_coup==2: #mon_coup
        lab3.configure(image=feuille)
    else:
        lab3.configure(image=ciseaux)
        augmenter_scores(mon_coup,ton_coup)
        score1.configure(text=str(ton_score))
        score2.configure(text=str(mon_score))


def jouer_pierre() :
    jouer(1)
    lab1.configure(image = pierre)


def jouer_feuille() :
    jouer(2)
    lab1.configure(image=feuille)


def jouer_ciseaux() :
    jouer(3)
    lab1.configure(image=ciseaux)


def reinit () :
    global mon_score, ton_score, score1, score2, lab1, lab3
    ton_score = 0
    mon_score = 0
    score1.configure(text=str(ton_score))
    score2.configure(text=str(mon_score))
    lab1.configure(image=vide)
    lab3.configure(image = vide)


ton_score = 0
mon_score = 0

#fenetre graphique
fenetre = Tk()
fenetre.title("Pierre, feuille, ciseaux")

#images dans fenetre

vide = PhotoImage(file = 'vide.gif')
versus = PhotoImage(file = 'versus.gif') 
pierre = PhotoImage(file = 'pierre.gif')
feuille = PhotoImage(file = 'feuille.gif')
ciseaux = PhotoImage(file = 'ciseaux.gif')

#labels (textes visibles) peut etre du text ou des img

texte1 = Label(fenetre, text = "Joueur :", font=("helvetica",16))
texte1.grid(row=0, column = 0)

texte2 = Label(fenetre, text = "Ordinateur :", font=("helvetica",16))
texte2.grid(row=0, column = 2)

texte3 = Label(fenetre, text = "Pour jouer, cliquer sur un choix ci dessous :")
texte3.grid(row=1, columnspan= 3, pady = 5)

score1 = Label(fenetre, text = "0", font=("helvetica",16))
score1.grid(row=2, column = 0)

score2 = Label(fenetre, text = "0", font=("helvetica",16))
score2.grid(row=2, column = 2)

#les coup qu'on joue

lab1 = Label(fenetre, image = vide)
lab1.grid(row = 3, column=0)

lab2 = Label(fenetre, image = versus)
lab2.grid(row = 3, column=1)

lab3 = Label(fenetre, image = vide)
lab3.grid(row = 3, column=2)

#les boutons

bouton1 = Button(fenetre, command = jouer_pierre)
bouton1.configure(image = pierre)
bouton1.grid(row = 4,column = 0)

bouton2 = Button(fenetre, command=jouer_feuille)
bouton2.configure(image=feuille)
bouton2.grid(row=4,column=1)

bouton3 = Button(fenetre, command=jouer_ciseaux)
bouton3.configure(image=ciseaux)
bouton3.grid(row=4,column=2)

#ligne 5

bouton4 = Button(fenetre, text = 'Rejouer', command = reinit)
bouton4.grid(row = 5, column = 0, pady = 10, sticky = E)

bouton5 = Button(fenetre, text = 'Quitter', command = reinit)
bouton5.grid(row = 5, column = 2, pady = 10, sticky = W)


fenetre.mainloop()


