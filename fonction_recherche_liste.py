#programme rechercher dans une liste

L = ['lyon','paris','la rochelle','perpignan','montpelier','beijing']       
def rechercheP(element,L) :
    
    print("debut de recherche \n")
    for i in range(len(L)) :
        if L[i] == element :
            return i
    return -1

t = "perpignan";

print(rechercheP(t,L))
print("\n")
















"""
def rechercheL(element,L) :
    k = 0
    b = str(element)
    print("debut de recherche \n")
    for i in range(len(L)) :
        if L[i] == b :
            k = 1
            print("l'element qu'on cherche se trouve a la place",i+1)
    if k == 0 :
        return -1
        """
