import random
from datetime import date

def valores():
    compV = [random.randint(30, 90), random.randint(30, 90), random.randint(30, 90)]
    compZ = [random.randint(30, 90), random.randint(30, 90), random.randint(30, 90)]
    compX = [random.randint(30, 90), random.randint(30, 90), random.randint(30, 90)]
    

    return compV, compZ, compX

def menor_media(modelo):
    print(modelo)


    menores = []
    for i in modelo:
        menores.append(min(i))

    print('soma menores: ', sum(menores))
        

    media = []
    for i in modelo:
        media.append(round(sum(i)/len(i), 2))

    print('soma média: ',round(sum(media), 2))
    

menor_media(valores())



