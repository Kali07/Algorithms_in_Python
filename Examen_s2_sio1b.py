#examens algo S2 sio 1

Dist = []
Totale = 0
l = 7
h = 35 
for i in range(0,180) : 
    Dist.append(i)
    Totale = Totale + l
    
    
print(Dist)
print("\n")
print("Distance totale",Totale)






"""
Liste = [1,21,24,17,20,21]
Liste2 = [1,21,24,17,20]
def verifdoublons(liste) :
    nouvelleL = [] 
    for i in Liste : 
        if i not in nouvelleL : 
            nouvelleL.append(i)
    if nouvelleL != liste :
        print("il ya un ou plusieurs doublons")
    else :
        print("il n'ya pas de doublons")



print(verifdoublons(Liste))
print(verifdoublons(Liste2))



nouvelleL = [] 
for i in Liste : 
    if i not in nouvelleL : 
        nouvelleL.append(i)
if nouvelleL != Liste :
    print("il ya un ou plusieurs doublons")
else :
    print("il n'ya pas de doublons")


    
def VerifierParite(nombre) :
        if(nombre%2 == 0):
            #print("Le nombre",nombre," est pair!");
            return True 
            
        else :
            #print("Le nombre",nombre," est impair!");
            return False 
        
for i in range(1,21):
    if VerifierParite(i) == False :
        print("nombre impair",i)


def eliminer(Liste) :
    for i in range(len(Liste)) :
        if Liste[i] in Liste :
            print("Il y'a un ou plusieurs doublons")
            return 0
        else :
            print("Il y'a pas de doublons")
            return 0
    


print(eliminer(Liste))


    
        

"""





    


