#Desafio 5: rpsls_input.py
#Proposta: game rpsls com entrada do usuário validada a partir da interface.
#Disponível em: http://www.codeskulptor.org/#user46_HET62s8d7F_5.py
# Rock-paper-scissors-lizard-Spock template

# A ideia chave desse programa é igualar as  strings
# "rock", "paper", "scissors", "lizard", "Spock" aos números
# como segue:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
import random
import simplegui

options = {
    0: "pedra",
    1: "Spock",
    2: "papel",
    3: "lagarto",
    4: "tesoura"
}

def name_to_number(name):
    number = -1;
    for i in range(5):
        if options[i] == name:
            number = i;

    return number;


def number_to_name(number):
    name = "";
    for i in range(5):
        if i == number:
            name = options[i];

    return name;


def rpsls(player_choice):
    # imprima uma linha em branco para separar jogos consecutivos
    print("\n")

    # imprima a mensagem com a escolha do jogador
    print("Jogador escolhe " + player_choice)
    text = "Jogador escolhe " + player_choice

    # convera a escolha para número usando a função name_to_number()
    player_number = name_to_number(player_choice)

    # compute um palpite aleatório comp_number usando random.randrange()
    comp_number = random.randrange(5)

    # converta comp_number para comp_choice usando a função number_to_name()
    comp_choice = number_to_name(comp_number)

    # imprima a escolha do computador
    print("Computador escolhe " + comp_choice)
    text += "\n Computador escolhe " + comp_choice

    # compute a diferença de comp_number e player_number módulo 5
    subtraction = comp_number - player_number

    # use if/elif/else para determinar o ganhador, imprima o vencedor
    if subtraction == 0:
        result = "Empate!"
        text += "          Empate!"
    elif subtraction == 1 or subtraction == 2 or subtraction == -3 or subtraction == -4:
        result = "Computador vence!";
        text += "\n Computador vence!"
    else:
        result = "Jogador vence!";
        text += "\n Jogador vence!"

    print(result)
    label.set_text(text)


def input_handler(input):
    input = input.lower()
    if input == "pedra" or input == "papel" or input == "tesoura" or input == "lagarto" or input == "spock":
        # input is valid
        rpsls(input)
    else:
        # input is not valid
        print("Jogada Invalida! Tente Novamente!")


# Create a frame and assign callbacks to event handlers
# Crie um frame e assinale os callbacks para os event handlers
frame = simplegui.create_frame("RPSLS", 300, 200)
frame.add_input("Sua Jogada: ", input_handler, 100)
label = frame.add_label('', 200)

# Inicie a animação
frame.start()

# teste seu código - ESTAS CHAMADAS DEVEM ESTAR PRESENTES NO CÓDIGO QUE
# VOCÊS VÃO ME RETORNAR
"""/rpsls("pedra")
rpsls("Spock")
rpsls("papel")
rpsls("lagarto")
rpsls("tesoura")"""
