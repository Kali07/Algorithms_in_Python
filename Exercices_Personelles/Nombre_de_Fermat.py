#programme Nombre_de_Fermat

n = int(input("Entre "))

R = 0
if B == 0 :
    print("Le pgcd est",A)
else :
    while B != 0 : #peut etre rajouter une condition pour a>b strictement
        R = A%B
        A = B
        B = R
        #print(B)        
print("Le pgcd est : ",A)
    





