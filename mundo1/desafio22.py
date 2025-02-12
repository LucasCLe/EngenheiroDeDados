'''
    Crie um programa que leia o nome completo de uma pessoa e mostre:
    1. O nome com todas as letra maiúsculas.
    2. O nome com todas as letras minúsculas.
    3. Quantas letras ao todo sem considerar espaços.
    4. Quantas letras tem o primeiro nome.
'''

nome = str(input('Digite seu nome: '))

print(f'Seu nome com letras maiúsculas fica {nome.upper()}.')
print(f'Seu nome somente com letras minúsculas fica {nome.lower()}.')
print(f'Seu nome sem os espaços entre os nomes fica {nome.replace(" ", "")}.')

nome1 = nome.split()
print(nome.replace("A","-"))
print(f'O primeiro nome que é "{nome1[0]}" tem {len(nome1[0])} letras.')
