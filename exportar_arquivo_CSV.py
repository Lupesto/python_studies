import csv

nomeCompleto = 'teste.csv'
with open(nomeCompleto, 'a', newline = '') as file:
	writer = csv.writer(file)
	writer.writerow(['modelo', 'componente', 'quantidade'])
	writer.writerow(['j2', 'camera frontal', 5])

