modelos = ["j2-J200", "j2-prime", "j5-prime", "J5-J500", "k10-2017", "G5s",
          "G5s-plus", "moto-g1", "moto-g2", "moto-g3"]


#modelos = {5:"j2-J200", 6:"j2-prime"}
print(modelos)

class Amodelo:
    def __init__(self, nome):
        self.nome = nome


for i in modelos:
    print(i)
    i = Amodelo(i)
    print(type(i))



