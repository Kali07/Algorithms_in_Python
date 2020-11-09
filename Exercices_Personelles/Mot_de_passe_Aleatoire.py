#programme Generer Mot de Passe Aléatoire
#choice permet de tirer au sort les element d'une liste
#end = " " pour espacer a la fin de chaque instrucion 
from random import choice,randint

Mot_de_passe = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
                'q','r','s','t','u','v','w','x','y','z',1,2,3,4,5,6,7,8,9,10]
for i in range(8) :
    print(choice(Mot_de_passe),end=" ")
    
