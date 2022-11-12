"""
Estruturas Lógicas

AND(e)
OR(ou)
NOT(não)
IS(é)

Operadores Unários:
    - not, is

Operadores Binários:
    - and, or

"""

ativo = True
logado = True

if ativo and logado:
    print('Bem-vindo!!!')
else:
    print('Ative sua conta!!!')


if ativo or logado:
    print('Bem-vindo!!!')

if not ativo:
    print('Ative sua conta!!!')