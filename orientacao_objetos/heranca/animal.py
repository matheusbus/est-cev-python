class Animal:

    def __init__(self, nome, raca, cor):
        self.nome = nome
        self.raca = raca
        self.cor = cor
        self.fome = False

    def comer(self):
        if(not self.fome):
            self.fome = True
            print(f"O {self.nome} está comendo.")