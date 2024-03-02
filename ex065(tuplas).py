"""Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar,
 para cada palavra, quais são as suas vogais."""

print('\033[35m=-=\033[m'*10)
print('\033[32mContando vogais\033[m')
print('\033[35m=-=\033[m'*10)

palavras = ("Abacate", "Arroz", "Feijão", "Alho", "Palmeiras", "Bombom", "Richard")

for palavra in palavras:
    print(f"Vogais da palavra {palavra}: ", end = " ")
    for letras in palavra:
        if letras in "AEIOUaeiou":
            print(letras, end = " ")
    print("\n")   
    