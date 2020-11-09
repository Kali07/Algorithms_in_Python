#programme qui calcule le factorielle Richard Mulamba

nombre = int(input("Entrez le nombre a calculer __ "))
i=nombre
facto = 1
while i >= 1 :  
    facto = facto*i 
    i=i-1
print("le factorielle de",nombre,"est",facto)
    
#with boucle For

"""
nombre = int(input("entrez le nombre"))
facto = 1
for i in range(1,nombre+1) :
    facto = facto * i
print("Le factorielle de ",nombre,"est",facto)
"""
