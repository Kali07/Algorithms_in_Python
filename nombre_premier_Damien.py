#On cherche à savoir si un nombre est premier

from math import sqrt

def is_int(v):
    c=int(v)==v
    return c

liste=[2,3,5,7,11,13,17,19,23,29]
x=0

nombre=float(input("saisissez un nombre pour savoir si il est premier:"))
i=sqrt(nombre)
t=is_int(i)
if t==True:
    print(nombre,"est divisible par ",i," qui est un nombre entier donc ",nombre," n'est pas un nombre premier.")
elif i<29:
   f=False
   while i>liste[x] and f==False:
       y=nombre/liste[x]
       f=is_int(y)
       x=x+1
if f==False:
    print("le nombre donné est premier car il n'est divisible par aucun nombre premier inférieur à sa racine ",i)
else:
    print("Le nombre donné n'est pas premier car il est divisible par",liste[x-1])
