#nombre de chiffre deja

#nombre = int(input("entrez le nombre  : "))

#Programme ARM 
r = 1
for nombre in range (1, 15000) :
    long = 0
    p = 0
    beta = nombre
    while beta >= 1 :
        r = int(beta % 10)
        beta = beta/10
        p = p + r**3
        long +=1        
    if long == 3 and p == nombre :
        print("ARM : ",nombre)






        #print("p = bien ",p,"et long",long)
    #print("beta",beta)
    #print("nombre",nombre)
#print("longueur est",long)










"""
fonction ARM
def arm (nombre):
    r = 1
    p = 0
    long = 0
    while nombre >= 1 :
        r = int(nombre % 10)
        nombre = nombre/10
        p = p + r**3
        long +=1
        print(r)
        print("p = bien ",p)
    
    print("longueur est",long)

arm(153)


#Programme Jeux de Roulette

    
pari = input("entrez le pari i ou p ")
print()
nombre = int(input("entrez le nombre : "))

if nombre % 2 == 0 and pari == 'p' :
    print("Gagné ")
elif nombre % 2 != 0 and pari == 'i' :
    print("Gagné")
else :
    print("Perdu")






#programmes EP Algo

a = "az"
b = "er"
c = a+b+"ty"
#print(c)

#Programme qui demande a un utilisateur d'ecrire un pseudo avec au moins de 4 lettres

pseudo = input("entrez le pseudo")
while len(pseudo) < 4 :
    print("pseudo incorrect",end =" ")
    pseudo = input("veuillez saisir de nouveau : ")

print("Bonjour",pseudo)

#saisir un nombre puis affiche s'il est nul, neg ou pos

nombre = float(input("Entrez votre nombre : "))

if nombre * -1 > 0 :
    print(nombre,"est négatif")
elif nombre * -1 < 0 :
    print(nombre,"est positif")
else :
    print(nombre,"est null")
"""
