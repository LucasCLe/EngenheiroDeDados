'''
    Faça um programa que faça programa que leia um número
    de 0 a 9999 e mostre na tela cada um dos digitos 
    separados.

    ex: 
    Digite um número: 1834

    unidade: 4
    dezena: 3
    centena: 8
    milhar: 1
'''

numero = input('Digite um número de 0 a 9999: ')



print(f'Unidade : {numero[3]}')
print(f'Dezena : {numero[2]}')
print(f'Centena : {numero[1]}')
print(f'Milhar : {numero[0]}')