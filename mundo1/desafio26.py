'''
    Faça um programa que leia uma frase pelo teclado e mostre:
    1. Quantas vezes aparece a letra "E"
    2. Em que posição ela aparece a primeira vez.
    3. Em que posição ela aparece a última vez.
'''
frase = 'Tudo posso naquele que me guarde e me protege.'

print(f'Tem {frase.upper().count('E')} palavras "E".')
print(f'A primeira vez que aparece a letra "E" é na casa {frase.find("e")}.')
print(f'A última vez que aparece a letra "E" é na casa {frase.rfind("e")}.')