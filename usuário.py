
"""
Recebendo dados do usuário
"""

# Entrada de dados
# print("Informe seu nome!")
# nome = input()

# print(nome, "Informe sua Idade")
# idade = input()

# Processamento

# Saída de dados

#  print(nome, idade,"Anos, Correto ?")
# resposta = input()

# Simplificando

nome = input("Qual seu nome?")
idade = int(input("Data de nascimento"))

print(nome, 2022 - idade, "Anos!")

pergunta = input("Sua idade está correta?")

if(pergunta == "SIM"):
    print("Dados válidados")