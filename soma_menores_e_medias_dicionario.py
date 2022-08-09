"""

a = {'a':1, 'b': 5, 'c': 2}
b = {'d': 3, 'e':9, 'f':2}

MenorA = min(a.items(), key=lambda x: x[1])
MenorB = min(b.items(), key=lambda x: x[1])

print(type(MenorA))
print(MenorA, MenorB)
print(MenorA[1], MenorB[1])
print(MenorA[1] + MenorB[1])

print(sum(a.values()))
print(len(a))

#Média
z = sum(a.values())/len(a)
print(round(z,2))

#Criar um for, simular dicio real


-------------------------------------------------------------
"""
print()
print()

dicionarios = {'a': {'z':10, 'b': 50, 'c': 20}, 'b': {'d': 30, 'e':92, 'f':32}}
novoDicionario = {}

#SOMAR MENORES/ SOMAR MÉDIAS

menores = []
medias = []
for name in dicionarios:
    print(name)
    for i in dicionarios[name]:
        a = 0
        
        precoSite = dicionarios[name][i]
        if precoSite < 90:
            a = 5    
        dicionarios[name][i] = precoSite - ((precoSite*0.15)+a)
        
        
    menor = min(dicionarios[name].items(), key=lambda x: x[1])
    print(menor)
    novoDicionario[name] = {menor[0]:menor[1]}
    
    menores.append(menor[1])
    media = round(sum(dicionarios[name].values())/len(dicionarios[name]),2)
    medias.append(media)
    


#retornar um dicionário
# {'componente': {'NomeItem': 45}, 'componente2': {'NomeItem': 12}

print('dicionário dos menores', novoDicionario)
print(menores)
print(medias)
print('Soma menores:', sum(menores))
print('Soma médias:', sum(medias))
