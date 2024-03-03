"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""

nome = "Matheus"
print(nome, " - Classe: ", type(nome))

idade = 10
print('Idade: ', idade, ' - Classe: ', type(idade))

faculdade = True
print('Faculdade:', faculdade, ' - Classe: ', type(faculdade))

renda = 3786.93
print('Renda: R$', renda, ' - Classe ', type(renda))

## Métodos de teste de tipo podem ser acessado com "variavel.is..."
print(nome.isnumeric())
print(nome.isalpha())

## Casting
x = str(3)
y = int('10')
z = float(4)

## O python é case sensitive
a = 'Algo'
A = 'Outro algo'

## Atribuição multipla
b, c, d = 'Amarelo', 'Verde', 'Azul'

## Visibilidade
def myFunc():
    global variavel_global
    variavel_global = 'Essa é uma variável global, pode ser acessada fora da função.'
    print(variavel_global)

myFunc()
print(variavel_global)

