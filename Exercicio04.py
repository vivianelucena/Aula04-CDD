'''Escreva um algoritmo para ler 10 números e no final calcular a soma desses números'''

soma = 0
for a in range(0, 11, 1):
    valor = int(input('Digite um valor para somar: '))
    soma += valor
print(soma)