modelo = 'j5'

celulares = ['j5-metal', 'j2-prime', 'g5s-plus', 'g6-play',
             'g6', 'g7', 'g7-play', 'g8', 'g8-play', 's10']
celularesA = []

#Considerar as diversas variações na busca.

for celular in celulares:
    novaString = []
    for i in celular:
        if not i == '-':
            novaString.append(i)
        else:
            novaString.append(' ')

    celularesA.append("".join(novaString))

print(celularesA)

"""    
novaString = []
for i in modelo:
    print(i)
    if not i == '-':
        novaString.append(i)
    else:
        novaString.append(' ')

print(novaString)
strA = "".join(novaString)
print(strA)
"""
