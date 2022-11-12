"""
Tipo String

Em Python, um dado é considerado do tipo string sempre que:

- Estiver entre àspas simples -> 'uma string', '1234', 'a'.
- Estiver entre àspas duplas -> "uma string", "1234", "a".

"""    

nome = "Pedro Oliveira"

print(nome.split()[0])

nome = "Pedro_Oliveira"

print(nome.split("_")[1])

nome = "João Pedro de Oliveira Neto"

print(nome.split()[0])