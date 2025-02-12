'''
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milimetros.
'''

metros = float(input('Digite os metros que deseja para saber a altura convertida em centímetros e milimetros: '))
cm = metros * 100
mm = metros * 1000

print(f'Você tem {metros}, convertido em centímetros fica {cm}cm e milimetros fica {mm}mm.')