'''
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
considere
US$1,00 = R$3,27
'''
dinheiroCarteira = float(input('Quantos dinheiro há na carteira? R$ '))
valorDolar = 3.27
possivelCompra = dinheiroCarteira / valorDolar

print(f'Você possui R${dinheiroCarteira:.2f} e pode comprar US${possivelCompra:.2f}.')
