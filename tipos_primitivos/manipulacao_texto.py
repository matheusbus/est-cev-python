frase = "Python é uma linguagem muito utilizada nos contextos de Inteligência Artificial e manipulação de dados."

print(frase)
print('Tamanho da frase:', len(frase))
print('Quantas letras "u": ', frase.count('u'))
print('Quantas letras "u" até o 15 byte: ', frase.count('u', 1, 15))
print('Posição do texto procurado: ', frase.find('Artificial'))
print('Python' in frase)
print(frase.replace('muito', 'pouco'))
print(frase.upper())
print(frase.lower())
print(frase.title())

frase_leiga = '   Removendo espaços do início e do final'
print(frase_leiga.strip())
print(frase_leiga.lstrip())
print(frase_leiga.rstrip())

palavras_da_frase = 'Python é top.'.split()
for palava in palavras_da_frase:
    print(palava)

print('-'.join(palavras_da_frase))

for letra in 'Banana':
    print(letra)

name = 'Matheus'
txt = 'My name is {}.'
print(txt.format(name))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

## Escape text
txt = 'We are started to \'learn\' Python'
print(txt)