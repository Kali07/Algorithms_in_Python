#pierre feuille ciseau version graphique
#joueur VS Ordinateur

from random import randint
from tkinter import *  #biblioteque qui permet de faire des graphiques





def augmenter_scores(mon_coup,ton_coup):
    global mon_score, ton_score
    
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
    if mon_coup==1:
        lab3.configure(image=pierre)
    elif mon_coup==2:
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
