
def somchiffre(nombre) :
    
    r = 1
    p = 0
    beta = nombre
    while beta >= 1 :
        r = int(beta % 10)
        beta = beta/10
        p = p + r
    
    return p


somme = somchiffre(2469)
print(somme)
                   
    
