import random

def jogo_adivinhacao():
    print("Bem-vindo ao Jogo da Adivinhação!")
    print("Escolha um nível de dificuldade:")
    print("1 - Fácil (1 a 10, 3 tentativas)")
    print("2 - Médio (1 a 30, 5 tentativas)")
    print("3 - Difícil (1 a 100, 7 tentativas)")
    
    escolha = input("Digite o número da dificuldade: ")
    
    if escolha == "1":
        limite = 10
        tentativas = 4
    elif escolha == "2":
        limite = 30
        tentativas = 6
    elif escolha == "3":
        limite = 100
        tentativas = 7
    else:
        print("Opção inválida. Escolhendo dificuldade Fácil por padrão.")
        limite = 10
        tentativas = 3
    
    numero_secreto = random.randint(1, limite)
    
    print(f"Tente adivinhar o número entre 1 e {limite}. Você tem {tentativas} tentativas!")
    
    for tentativa in range(1, tentativas + 1):
        palpite = int(input(f"Tentativa {tentativa}/{tentativas}: "))
        
        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou o número {numero_secreto}!")
            return
        elif palpite < numero_secreto:
            print("Tente um número maior!")
        else:
            print("Tente um número menor!")
    
    print(f"Suas tentativas acabaram! O número secreto era {numero_secreto}.")

# Executando o jogo
jogo_adivinhacao()
    
	
