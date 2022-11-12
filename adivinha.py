from ast import If


print("|**********************************|")
print("| Bem vindo no jogo de adivinhação |")
print("|**********************************|")

numero_secreto = 1010

chute = input("Digite o seu numero: ")

print("Você digitou", chute)

if(chute == numero_secreto):
    print("Parabéns, você acertou!")
else:
    print("Tente novamente")
