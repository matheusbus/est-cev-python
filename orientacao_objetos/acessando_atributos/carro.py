class Carro:

    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano

    def get_modelo(self):
        return self.modelo

    def get_ano(self):
        return self.ano

    def set_modelo(self, novo_modelo):
        self.modelo = novo_modelo

    def set_ano(self, novo_ano):
        self.ano = novo_ano


corolla = Carro('Corolla XLI', 2014)
print(corolla.get_modelo())
print(corolla.get_ano())
corolla.set_ano(2018)
print(corolla.get_ano())