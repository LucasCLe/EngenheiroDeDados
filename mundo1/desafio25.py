'''
    Crie um programa que leia o nome de uma pessoa e diga
    se ela tem "Silva" no nome.

'''

nome = str(input('Digite seu nome completo: '))

if "Silva" in nome:
    print('Sim, o nome tem "Silva".')

if "silva" in nome:
    print('Sim, o nome tem "Silva".')