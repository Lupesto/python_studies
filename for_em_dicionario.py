
dicio = {'sopa de cebola': 15, 'sopa de alho': 13, 'pastel de carne': 6, 'carne moida': 8, 'carne moida estragada': 3, 'estragada carne moida': 3}

quero = ['carne', 'pastel']
evitar = ['estragada']


media = []
for i in dicio:
    if i != 'banana':
        print(i)
        print(dicio[i])
        media.append(dicio[i])


media = round(sum(media)/len(media),2)
print(media)



"""
dicio = {'banana': 4, 'maçã':3, 'uva': 7}



media = []
for i in dicio:
    if i != 'banana':
        print(i)
        print(dicio[i])
        media.append(dicio[i])


media = round(sum(media)/len(media),2)
print(media)


"""


"""
#produtos = {'moto g3 carcaça': 'R$18', 'moto g3 carcaça quebrada': 'R$21', 'moto g4 carcaça': 'R$ 40,99', 'carcaça moto g3': 'R$ 32'}
produtos = ['moto g3 carcaça', 'moto g3 carcaça quebrada', 'moto g4 carcaça', 'carcaça moto g3']


buscar = ['moto g3']
evitar = ['quebrada']

condizentes = []
for i in produtos:
    for a in buscar:
        if a in i:
            condizentes.append(i)
print(condizentes)

for i in evitar:
    for a in condizentes:
        if i in a:
            del(condizentes[condizentes.index(a)])

print(condizentes)
"""

