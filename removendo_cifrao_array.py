valores = ["R$13", 'R$ 17', 'R$ 42,99', 'R$ 5,45', 'R$ 1.299,90'] #Entender como o ML trabalha com os milhares

novoValores =[]
for i in valores:
    listaTemporaria = []
    for a in i:
        if a != "R" and a != '$' and a != ' ' and a != '.':
            if a == ',':
                listaTemporaria.append('.')
            elif a == '.':
                listaTemporaria.append(',')
            else:
                listaTemporaria.append(a)
    novoValores.append(listaTemporaria)
    
    print(listaTemporaria)


novaLista = []
for i in novoValores:
    indice = novoValores.index(i)
    vazia = ''
    for a in i:
        vazia = vazia + a
        
    else:
        novaLista.append(float(vazia))
        
print(novaLista)




