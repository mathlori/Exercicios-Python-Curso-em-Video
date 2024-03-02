"""Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
 Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso."""

print('\033[35m=-=\033[m'*10)
print('\033[32mNúmeros por Extenso\033[m')
print('\033[35m=-=\033[m'*10)

extenso = ("zero","um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

while True:
    n = int(input("Digite um número: "))
    if n < 0 and n > 20:
        n = int(input("Valor menor ou maior que o intervalo mencionado. Digite novamente: "))
    if n == -1:
        print("Programa encerrado.")
        break
    for i in range(0, 21):
        if n == i:
            print(f"Você digitou o número {extenso[i]}")
    
