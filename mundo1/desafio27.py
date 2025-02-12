'''
    Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
    e o ultimo nome separadamente.

    ex: Ana Maria de Souza
    primeito = Ana
    útimo = Souza
'''

nome = str(input('Digite o seu nome: '))
nomeFatiado = nome.split()
print(f'Seu primeiro nome é {nomeFatiado[0]}.')
print(f'Seu último nome é {nomeFatiado[-1]}')