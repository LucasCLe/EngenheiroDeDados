'''
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
sobre ele
'''

digito = input('Digite alguma coisa: ')

print(f'Ele é um número? {digito.isdigit()}')
print(f'Ele é uma letra? {digito.isalpha()}')
print(f'Ele está em letra minúscula? {digito.islower()}')
print(f'Ele está em letra maiúscula? {digito.isupper()}')
print(f'Ele é alfanúmerico? {digito.isupper()}')