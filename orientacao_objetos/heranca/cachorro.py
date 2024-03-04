from animal import Animal

class Cachorro(Animal):

    def __init__(self, nome, cor):
        super().__init__(self, nome, cor)

    def latir(self):
        print(f"O {self.nome} diz: au, au!")