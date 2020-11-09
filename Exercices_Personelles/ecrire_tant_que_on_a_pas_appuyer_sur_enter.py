#Programme ecrire au clavier tant que on a pas appuyer sur la touche Enter

#enter corespond tout simplement au retour a la ligne ou juste le vide

entrer = "mot"
n = 0
while entrer !="":
    entrer = input("tapez un mot ou enter pour quitter :  ")
    n+=1
    if entrer != "":
        print(n,entrer)
print("Au revoir !")

