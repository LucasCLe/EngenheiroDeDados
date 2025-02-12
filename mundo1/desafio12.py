'''
Faça um algoritmo que leia o preço do produto e mostre seu novo preço, com 5% de desconto.
'''
precoProduto = float(input('Digite o preço do produto: R$ '))

desconto = precoProduto - (precoProduto * 0.05)

print(f'O preço do produto é R${precoProduto:.2f} e com desconto de 5% fica R${desconto:.2f}.')