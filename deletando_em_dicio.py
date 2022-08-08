notas = {'joão':9, 'ana':2, 'augusto':10}

print(notas)
#notas['João'] = notas.pop('joão')
notas['João'] = notas['joão']
del notas['joão']

print(notas)
notas['ana'] = notas.pop('ana')
notas['augusto'] = notas.pop('augusto')
print(notas)
