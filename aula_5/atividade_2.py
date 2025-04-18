# Exercício 1 - Contagem Simples

for num in range(10):
    print(num + 1)

# Exercício 2 - Mensagem repetida

text = 'Estudando Python!'

for i in range(5):
    print(text)

# Exercício 4 - Coleta de dados

name = input('Informe o nome: ')

for p in range(3):
    print(name)

# Exercício 5 - Soma de valores

sum = 0.0
mean = 0.0

for v in range(5):
    value = float(input('Informe um valor para a soma e para média: '))
    sum = float(sum + value)
    mean = sum/int(v+1)
    print(f'soma: {sum}')
    print(f'média: {mean}')
