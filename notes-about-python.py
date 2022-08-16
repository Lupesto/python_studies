import random
#Mágica com loop
# mostrar primeiro o código e tentar enteder o que ele faz
"""
Acessando valores em listas aninhadas
"""
Dieta = [['abacaxi', 'maçã', 'uva', 'amora'], ['ovo', 'peixe', 'frango', 'queijo']]

print(Dieta[1][0])
print()

"""
Qual será resultado deste código?
"""

sopa = ["cenoura", "cebola", "batata"]
for ingredientes in sopa:
    print(ingredientes)




"""
Listas multidimensionais
São listas dentro de listas. A seguir usaremos listas bidimensionais (2D) e tridimensionais (3D). As aprendidas até agora pdeomos chama-las de unidimensionais, pois cada posição da lista possui um elemento.
"""


#Strings
#------------------------------------------------------



"""
postToChat()
Função para enviar mensagens dentro do jogo
"""


#Boleanos
#------------------------------------------------------
"""
função getBlock()
coleta o bloco ID
"""

"""
ordem dos operadores lógicos.
[pesquisar] not, and e or

"""
        

"""
Para que serve o if?
Condiciona o código, podendo o conteúdo aninhado ser executado ou não.
"""

"""
if e while aninhados
Exemplo com o uso do if e while junto.
"""

"""
Interrompendo loop while
break -> faz com que o código saia imediatamente do while.
"""




"""
O que é uma iteração?
Quando o loop repete um bloco

Para que serve ctrl+c?
para parar o código.

Para que serve o while?
Loops ou laços de repetição. Ao invés de copiar o código diversas vezes são usados para repetir blocos de código.

"""


print()
"""
operadores boleanos e loop while
While com o uso do and, or e not.
"""
cont = 0
while cont < 10 or cont == 7: #ARRUMAR. PAREI AQUI
    cont += 1
    print(cont)



#Funções


"""
docstring
Comentário. O python ignora a linha de comentário. O objetivo do comentário é explicar sobre o funcionamento do código para si próprio como para outras que irão ter contato com o código desenvolvido. 
Docstring são comentários de multiplas linhas que começam e terminam com "."" aspas.

"""
""" Exemplo:
    de docstring.
"""



"""
Motivos para usarmos as funções:
reusabilidade, identificação de problema, aumento de processos em um programa.


O que uma função de retorno nos permite?
Funções que retornam valores podem servir de argumento ou em variáveis, as funções que não retornam nada, não.


Para que servem as funções?
Blocos de comando reutilizáveis. Ao invés de ficar reescrevendo código utilizamos função.


Quebra de linha em argumentos
Podemos quebrar a linha quando os argumentos são muito longos
    - ver pg cento e noventa e seis

    
Valores de retorno da função
O retorno permite que a função trabalhe os dados e retorne um valor.
"""

#Array

print()
"""
Usando listas
"""
objetos = ['cadeira', 'mesa', 'caneta', 'copo']



"""
Índice é o nome dado para cada posição na lista.



Para que servem arrays?
Usados para armazenar dados em sequência. Listas podem armazenar strings, númeross, boleanos e outras listas.


pollBlockHits()
retorna lista de dados já acertados.


Qual o primeiro indice de uma lista?
O primeiro indice é 0. Se tentar acessar um índice que não existe na lista o código dará erro.
"""






"""
Alterando métodos e atributos
É possível redefinir métodos e atributos com o mesmo nome na superclass para a subclass. Faz com que se comporte de maneira diferente.

VER código página trzentos e duzentos e um% [Classe gato]

Entendendo a herança
Quando classes compartilham os mesmos métodos, atributos e outras classes.

Exemplo: Patos e penguins são aves. Ave é uma superclass.
Patos e penguins são subclass

Todos compartilham dos mesmos métodos base e atributos.
Superclass é a classe que outras herdam.


Herdando uma classe
Adicionar método e atributos extras sem afetar o original

class nomeDeClasse(herança)
-> não necessita de inicializador

Para o autor a programação era um hobby, mas por sorte se transformou em sua principal profissão.
[imagem do autor e nome]


Para que serve orientação a objetos?
Agrupa funções e variáveis para criar classes. Cada classe pode ser usada par criar objetos que compartilham das mesmas variáveis.
Quando uma função faz parte de uma classe a chamamos de método e, quando uma variável faz parte de uma classe, a chamamos de atributo.


Por que aprender orientação a objetos?
torna a programação mais fácil,


Qual a vantagem de programar voltado a orientação a objetos?
Reusabilidade


Retornando valores com métodos
Basta adicionar return como função
"""


#arquivos e modulos
"""
Abrindo um arquivo no python
open() -> recebe dois argumentos, local e permissão.
open("ArquivoSecreto.txt","w")

w-> especifica que o programa está autorizado.



Aplicando o módulo
Caso o nome do módulo seja muito longo, podemos renoma-lo
- também  para facilitar a escrita ou em caso de conflito
- Adicione a palavra [as] após o import

    import pickle as p


Argumentos para permissão
w -> somente escrita. Pode substituir conteúdo existente, mas não pode lê-lo.
r -> Somente leitura
r+ -> leitura e escrita
a -> adição. Insere conteúdo somente novo no final do arquivo.


Arquivo o que é?
Escrever algo no bloco de notas e salvar no computador é um arquivo. Texo, imagens e vídeo são arquivos.


As funções acompanham notação
arquivo = open ("segredo.txt", "")
arquivo.função()
arquivo.close



Funções
write -> escreve dados em um arquivo aberto
close -> para salvar e fechar o arquivo
read -> lê todo o arquivo
readline -> lê apenas uma linha


getBlockWithData
retorna além do ID a posição do bloco e seu estado


Importando todas as funções com [%]
Para que não precise utilizar a notação de ponto toda vez que precisar de uma função, basta:
    from pickle import asterisco%
    
Porém se outro módulo utilizado compartilhar do mesmo nome para uma função, você terá erro, pois o python ficará confuso, então utilize notação caso o código seja muito extenso.


Importando uma função com a cláusula from
Quando usamos o import importamos todas as funções de um módulo, com o from podemos especificar. 
Nos permite chamar apenas a função, sem necessidade de notação com o módulo.

se precisar de mais de uma função  basta separa-las por virgula
    from picle import dump, load




Instalando novos módulos com pip
O pip facilita a instalação dos módulos. pip é um programa que possui recursos e que facilita a instalação, atualização e desinstalação de módulos.
Dependendo do sistema operacional  a forma do pip muda.

no windows: abra o prompt de comando, digite pip e em seguida    
    pip install flask



O que são módulos?
São coleções de funções que podemos importar para o python. Há uma grande variedade de módulos disponíveis, estes permitem criar jogos, calculadoras...

from mcpi por exemplo é um módulo que permite conectar o python ao minecraft. Algumas das funções já vistas fazem parte da biblioteca padrão do python.


Para que servem os arquivos?
Arquivos permitem o armazenamento de dados para uso futuro, em programas.
Até agora nossos programas armazenavam dados em variáveis [Inseridos diretamente no código ou atráves de input de usuário].


Para que servem os módulos?
Módulos aumentam as possibilidades com diversas funções prontas. Por que perder tempo se já existe a solução?

"""






"""
[Testar na IDLE]
Operadores
Em matemática os operadores são usados para alterar ou combinar os números. Exemplo, o operador de adição [+] nos permite somar enquanto o operador de subtração [-] nos permite subtrair.

O python utiliza todos os operadores básicos [+, -, %, /] e também avançados como exponenciação.
ex: flowers = 2+2 ou 2-2
Ordem das operações -[Imagem pemdas]


Pegar a posição do jogador
position = mc.player.getTilePos()
x = position.x
y = position.y
z = position.z


Expresões e declarações
2+2 -> Expressão
zumbi = 2+2 -> declaração


Fora do python Shell você precisará fazer declarações pois os editores não fazem nada sem declaração.
-No editor precisamos atribuir a alguma variável-
exemplificar 2+2 no Shell e no Editor


função setBlock()
para criar e posicionar um bloco no mine. SetBlock(x,y,z,BlockType)


função setBlocks (x,y,z,x,y,z, BlockType)
Uso de dois conjuntos de coordenadas. Extremidades como ponto.


função setPos ()
[PARA QUE SERVE]

blockType
Cada tipo de bloco tem um valor. Melão, grama areia e água por exemplo.
"""


pesquisar = 'arroz'
alimentos = ['maçã', 'banana','arroz','feijão']
outros = ['canivete', 'notebook', 'papel']

if pesquisar not in alimentos:
    print(alimentos)

if pesquisar not in outros:
    print(outros)

if pesquisar not in alimentos and outros:
    print(alimentos, outros)

if pesquisar not in alimentos or outros:
    print(alimentos, outros)

