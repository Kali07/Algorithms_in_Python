#programme qui calcule la somme de tous les nombres avant n

nombre = int(input("Entrez le nombre a calculer __ "))
somme = 0
for i in range(1,nombre+1) :
    somme = somme + i
print("Le resultat est =",somme)
