#programme suite_de_syracus
                                                        
#ceci n'est pas un commentaire mais une instruction pas pris en compte
"""
une suite de syracuse est une suite des entiers definier de maniere suivante :
pour tout n>0 : si nest par alors n/2 sinon alors 3*n+1
"""

N = float(input("Entrez votre N __ "))
i=0
while(N != 1 and i < 20 ) :
    print(N) #Pour afficher a partir du premier
    
    if N%2 == 0 :
        N = N/2
        #print(N)
    else :
        N = 3*N+1
        #print(N)
    i+=1

print("voici la suite de syracus pour le nombre choisi",i)
