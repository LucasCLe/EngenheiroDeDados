'''
    Crie um programa que leia um programa Real qualquer
    pelo teclado e mostre na tela a sua porção inteira.
    exemplo:
    Digite um número: 6.127.
    O número 6.127 tem a parte inteira 6.
'''
import math
numero = float(input('Digite um número real: '))
print(f'O número real é {math.floor(numero)}.')