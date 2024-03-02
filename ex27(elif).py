#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
# atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER
print('\033[35m=-=\033[m'*10)
print('\033[32mClassificação de atletas\033[m')
print('\033[35m=-=\033[m'*10)
ano = int(input('\nEm que ano você nasceu?:'))
if ano >= 2014:
    print(f'Você tem \033[4;36m{2023-ano}\033[m anos, portanto, é classificado como \033[31mMIRIM\033[m.')
elif ano >= 2009:
    print(f'Você tem \033[4;36m{2023 - ano}\033[m anos, portanto, é classificado como \033[31mINFANTIL\033[m.')
elif ano >= 2003:
    print(f'Você tem \033[4;36m{2023 - ano}\033[m anos, portanto, é classificado como \033[31mJÚNIOR\033[m.')
elif ano >= 1998:
    print(f'Você tem \033[4;36m{2023-ano}\033[m anos, portanto, é classificado como \033[31mSÊNIOR\033[m.')
else:
    print(f'Você tem \033[4;36m{2023-ano}\033[m anos, portanto, é classificado como \033[31mMASTER\033[m')