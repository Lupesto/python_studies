PROGRAMAÇÃO ORIENTADA PYTHON

MATERIAL EXCLUSIVO APÓS ENTENDER A BASE DE ORIENTAÇAO a OBJETOS
https://medium.com/@nicolasbontempo/programando-python-orientado-a-objetos-d0069b2f1eb5



funções dentro de uma classe são chamados de métodos.

[o que é instância?]
[Pesquise por pyCharm]

------------------------------------------------------------

https://www.alura.com.br/conteudo/python-3-avancando-orientacao-objetos

o.o - orientação a objetos
Analogia com filmes.


um filme possui: 
Nome, ano e duração

uma série possui:
Nome, ano e temporadas

Aquele código maluco gerado quando damos print significa onde está alocado na memória.

class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome
        self.ano = ano
        self.duracao = duracao

vingadores = Filme()
print(vingadores.nome)

- este código dá erro pois não passamos os argumentos para o código.
-> nome, ano e duração são os atributos da classe.
_init_ sempre deve receber self.

PARTE CLASS SERIE



