entrada = {'sopa de cebola estragada': 15, 'sopa de alho': 13, 'pastel de carne': 6,
         'carne moida': 8, 'Carne moida estragada': 3,
         'estragada carne moida': 3}

#quero = 'carne' and 'moida'
quero =  ['modelo', 'componente']
evitar = ['estragada']



condizentes = {}

"""
dicio = {}
for k, v in entrada.items():
    dicio[k.lower()] = v

print(dicio)
print()
"""



for a in entrada:
    if 'carne' in a or 'sopa' in a: #terá que chamar listar e index
    #if 'carne' in a and 'moida' in a: <- uso do and
        condizentes[a] = entrada[a]
    else:
        print('não',a)

print('condizentes 1:', condizentes)


deletar = []
for i in evitar:
    for a in condizentes:
        if i in a:
            print('não pode', a)
            deletar.append(a)


for a in deletar:
    del condizentes[a]

print(condizentes)
            
