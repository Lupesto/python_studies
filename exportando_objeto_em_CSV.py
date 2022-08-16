import csv


class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome
        self.ano = ano
        self.duracao = duracao

    def soma(self):
        somar = self.ano+5
        return somar

vingadores = Filme('vingadores Ultimato', 2015, 60+60)
papaiNoel = Filme('vingadores - guerra infinita', 2018, 60)

print(vingadores.soma())
print(papaiNoel.soma())


with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Nome do filme', "ano", "duracao"])
    writer.writerow([vingadores.nome, vingadores.ano, vingadores.duracao])
