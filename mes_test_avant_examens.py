#Mes_test_avant_bts

#exo 1 : fonction carree et l'affiche 10fois

def carree(nombre) :
    caree = nombre * nombre
    return caree
for i in range(1,11):
    print("le carre de" ,i, "est :", carree(i))

#exo 2 : volume du parallélépipède
    
print("\n")
def Vparallelepipede(L,l,h) :
    volume = L*l*h
    return volume
print("le volume est",Vparallelepipede(7,4,8))

#exercice 3 : plus grande valeur

def plusgrandevaleur(nombre):
    
    nombre = float(input("saisir le nombre__"))
    maxi = nombre
    while nombre > 0 :
        nombre = float(input("saisir le nombre__"))
        if nombre > maxi :
            maxi = nombre
    return maxi
print(plusgrandevaleur(5))
        
    
    
