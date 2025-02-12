'''
O mesmo professor do desafio anterior que quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome 
dos quatros alunos e mostre a ordem sorteada
'''

import random
n1 = 'Marcos'
n2 = 'Cleber'
n3 = 'Cris'
n4 = 'Nath'

lista = [n1,n2,n3,n4]
escolhido = random.shuffle(lista)

print(f'O sorteio da lista ficou {lista}')