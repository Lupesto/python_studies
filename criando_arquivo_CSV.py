import csv
# Criando arquivo em csv
#with open('data.csv', 'w', newline='') as file:

# adicionando linhas em csv.
with open ('data.csv', 'a') as file:
    writer = csv.writer(file)
    """
    writer.writerow(['Data', "modelo", "menor Preço", "preço médio"])
    writer.writerow(['15/5', "moto g5 play", 55, 66])
    writer.writerow(['25/5', "moto g6", 55, 66])
    writer.writerow(['35/5', "Samsung j5 metal", 66, 55])
    """

    writer.writerow(['Modelo', "Placa mãe", 'Bateria', 'Display', 'Camera interna', 'Camera traseira', 'Carcaça', 'Tampa', "Preço menor", "preço médio"])
    writer.writerow(['G3', 230.9, 55.3, 130, 15, 12, 20, 13, 476.2, 606.2])
    writer.writerow(['J4', 120.4, 33.3, 50, 12, 6, 10, 33, 256.2, 357.2])
#modelo objeto, menor dicionráio de cada componente, soma preços menores, soma média
