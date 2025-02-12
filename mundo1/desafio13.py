'''
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
'''

salarioAtual = float(input('Qual seu sálario atual? '))

aumentoSalario = (salarioAtual * 0.15)

salarioComAumento = salarioAtual + aumentoSalario

print(f'Seu salário atual é de R${salarioAtual} e com o aumento de 15% é R${salarioComAumento}')