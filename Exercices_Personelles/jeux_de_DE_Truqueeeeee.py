#programme jeux de DE truqué
#end = " " pour espacer a la fin de chaque instrucion
from random import random

rnd = random()
if rnd < 0.1252 :  #equivalent a 12.52 % 
    print(1)
elif rnd < 0.2561 :
    print(2)
elif rnd < 0.4718 :
    print(3)
elif rnd < 0.6705 :
    print(4)
elif rnd < 0.7828 :
    print(5)
else :
    print(6)

    
"""
on oblige le jet de dé a respecter les probabilites qu'on va lui imposer


"""
