#Programme Aire d'un cercle
#import math
#pour se passe de import

from math import pi
#pi = 3.14 (ancienne methode)
r = float(input("Saisir le rayon__"))
#math.pi*r*r (avec l'appel de la bibliotheque math
surface = pi * r * r

print("La surface est de = ", surface)
