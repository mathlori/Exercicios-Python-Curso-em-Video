"""Crie um código que verifique se o site pudim.com.br está acessível"""

print('\033[35m=-=\033[m'*10)
print(f'\033[32mPudim\033[m')
print('\033[35m=-=\033[m'*10)

import urllib
import urllib.request

try:
    site = urllib.request.urlopen("https://www.pudim.com.br")

except urllib.error.URLError:
    print("O site Pudim não está funcionando.")
else:
    print("O site Pudim está funcionando normalmente")