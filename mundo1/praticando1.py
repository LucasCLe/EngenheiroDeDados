'''
tempo = int(input('Quanto tempo voce tem seu carro? '))

if tempo <= 3:
    print('Seu carro é novinho!')

else:
    print('Seu carro já está velho!')
  
print('==FIM!==')
'''

print('=================')
'''
nome = str(input('Qual é seu nome? '))
if nome == 'Gustavo':
    print('Que nome bacana você tem.')
else:
    print('Seu nome é tão normal.')
print(f'Bom dia, {nome}!')
'''
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
m = (n1 + n2) / 2
print(f'A sua média foi {m:.1f}')

if m >= 6.0:
    print('Sua média foi boa! Parabéns!')
else:
    print('Sua média foi ruim! Estude Mais!')