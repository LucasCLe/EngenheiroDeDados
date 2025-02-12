'''
    Faça um programa que leia um ângulo qualquer e mostre na tela o 
    valor do seno cosseno e tangente desse ângulo.
'''
import math




angulo = float(input("Digite um ângulo em graus: "))


angulo_rad = math.radians(angulo)


seno = math.sin(angulo_rad)
cosseno = math.cos(angulo_rad)
tangente = math.tan(angulo_rad)


print(f"O valor do seno de {angulo}° é: {seno:.2f}")
print(f"O valor do cosseno de {angulo}° é: {cosseno:.2f}")
print(f"O valor da tangente de {angulo}° é: {tangente:.2f}")