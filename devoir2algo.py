
#programme suite_de_syracus


N = int(input("Entrez votre N __ "))
u = N 
i=0

while(u != 1 and i < 20 ) :
    print(u) #Pour afficher a partir du premier
    
    if u%2 == 0 :
        u = u/2
    else :
        u = 3*u+1
    i+=1

print("voici la suite de syracus pour le nombre : ",N)



"""
u = 12

i = 0

while i < 5 :
    print(u,"pour i = ",i)

    if u%2==0 :
        u = u/2
    i+=1

print("fin")
"""
