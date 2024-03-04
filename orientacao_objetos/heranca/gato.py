from animal import Animal

class Gato(Animal):
    tipo_animal = 'Felino'

    def __init__(self, nome, raca, cor, peso):
        super().__init__(nome, raca, cor)
        self._peso = peso

    def miar(self):
        print(f"{self.nome} diz: miauuu")

    # método utilitário (só pode ser acessado internamente)
    def _dieta_gato(self):
        self.msg = 'Tudo ok!'
        if(self._peso < 3.5):
            self.msg = 'Aumente a ração do gato.'
        if(self._peso >= 5.0):
            self.msg = 'Diminua a ração do gato.'
        return self.msg

    def dados_gato(self):
        print(f"Animal: {self.tipo_animal}")
        print(f"O gato {self.nome} está com {self._peso} Kg.")
        print(self._dieta_gato())

# essa mudança afeta todas as próximas instâncias de Gato
Gato.tipo_animal = 'Pet'

nome_gato = 'Thomas'
gato = Gato(nome_gato, 'Siamês', 'Bege', 3.3)

gato.dados_gato()

# acessando método da classe pai
gato.comer()

gato.tipo_animal = 'Felino'
gato.dados_gato()