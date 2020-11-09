#programme qui ecrit les heures minutes et secondes d'une journee

heure = 0

while heure < 24 :
    minute = 0
    while minute < 60 :
        seconde = 0
        while seconde < 60 :
            print(heure,"heure",minute,"minutes",seconde,"secondes")
            seconde += 1
        minute += 1
    heure += 1

