'''
    Escreva um programa que pergunte a quantidade de km percorridos por carro alugado e a quanditdade de dias pelos quais
    ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.
'''

diasAlugado = int(input('Quantos dias o carro ficou alugado? '))
kmPercorrido = float(input('Quantos km foi percorrido? '))


diariaCarro = 60 * diasAlugado
kmRodado = 0.15 * kmPercorrido

totalPagar = diariaCarro + kmRodado


print('\n')
print(f'Você rodou com o carro por {diasAlugado} dias e andou um total de {kmPercorrido}km')
print(f'Então sabendo que a diária é R$60,00 e o km rodado é R$0,15.\nO aluguel do carro ficará R${totalPagar}.')

