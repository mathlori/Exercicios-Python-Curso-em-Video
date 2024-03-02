"""Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a 
expressão passada está com os parênteses abertos e fechados na ordem correta."""

print('\033[35m=-=\033[m'*10)
print('\033[32mValidando expressões matemáticas\033[m')
print('\033[35m=-=\033[m'*10)

simb = []
expressao = str(input("Digite uma expressão: "))

for char in expressao:
    if char == "(":
        simb.append(char)
    elif char == ")":
        simb.append(char)

if len(simb) % 2 == 0:
    print("Os parênteses dessa expressão estão corretos")
else:
    print("Os parênteses dessa expressão não estão colocados corretamente.")