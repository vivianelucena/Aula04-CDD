'''Ler uma variável de número inteiro e mostrar a tabuada de multiplicação desse número (1-10)
Formato de saída:
1 x 5 = 5
2 x 5 = 10'''

multiplicacao = 0
valor = int(input('Digite um valor: '))

for a in range(1, 11):
    #valor = int(input('Digite um valor: '))
    multiplicacao = a * valor
    print(f'{a} x {valor} = {multiplicacao}')