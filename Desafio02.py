'''Receba um número do usuário e mostre todos os números ímpares do intervalo de 1 até o número digitado'''

valor = int(input(f'Digite um valor e mostrarei os números ímpares até o valor digitado: '))

for a in range(1, valor + 1):       # Adiciona 1 para incluir o valor digitado
    if a % 2 != 0:                  # Verifica se o número é ímpar
        print(a)                    # Exibe o número ímpar