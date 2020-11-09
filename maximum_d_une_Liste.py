#maximum liste

Liste = [18,24,15,45,75,119,15]

def maximumL(Liste) :
    maxi = Liste[0]
    for i in range(len(Liste)) :
        if Liste[i] > maxi :
            maxi = Liste[i]
    return maxi

print("Le plus grand element de la liste est : ",maximumL(Liste))
    
