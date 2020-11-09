#Jeux Pile ou Face Truqué

#on jette 100 pieces et on s'assure quil montre face sur 57% des cas


from random import random

for i in range(100):
    #piece = random()
    if random() < 0.5783 :
        print("Face",end = " ")
    else :
        print("Pile",end = " ")

print("Fin du programme")



