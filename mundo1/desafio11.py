'''
Faça um programa que leia a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la
sabendo que cada litro de tinta pinta uma área de 2m².
'''

alturaParede = float(input(f'Qual a altura da parede? '))
larguraParede = float(input(f'Qual a largura da parede? '))
calculoArea = (alturaParede * larguraParede)

tintaNecessaria = calculoArea / 2



print(f'A sua parede tem a dimensão de {alturaParede}x{larguraParede} e sua área é de {calculoArea}m² \n e serão necessários {tintaNecessaria} litros de tinta para pintá-lá.')