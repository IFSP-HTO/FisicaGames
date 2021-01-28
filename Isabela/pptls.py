import simplegui
import random

Opcoes = ("Pedra", "Papel", "Tesoura", "Spock", "Lagarto")

m = "Regras:"
me = "Papel cobre Pedra"
mes = "Papel refuta Spock"
mess = "Pedra esmaga Lagarto"
messa = "Pedra quebra Tesoura"
messag = "Lagarto envenena Spock"
message = "Lagarto come Papel"
messagem = "Spock esmaga Tesoura"
messagem1 = "Spock vaporiza Pedra"
messagem2 = "Tesoura corta papel"
messagem3 = "Tesoura decapita Lagarto"
    

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(m, (10, 20), (15), "White")
    canvas.draw_text(me, (10, 40), (15), "White")
    canvas.draw_text(mes, (10, 60), (15), "White")
    canvas.draw_text(mess, (10, 80), (15), "White")
    canvas.draw_text(messa, (10, 100), (15), "White")
    canvas.draw_text(messag, (10, 120), (15), "White")
    canvas.draw_text(message, (10, 140), (15), "White")
    canvas.draw_text(messagem, (10, 160), (15), "White")
    canvas.draw_text(messagem1, (10, 180), (15), "White")
    canvas.draw_text(messagem2, (10, 200), (15), "White")
    canvas.draw_text(messagem3, (10, 220), (15), "White")

def button_pedra():
    comp_name = random.choice(Opcoes)
    Jogador = "Pedra"
    if Jogador == "Pedra" and comp_name == "Lagarto":
        print 'Voce escolheu Pedra'
        print 'O computador escolheu ' + str (comp_name)
        print "Jogador ganhou!"
    elif Jogador == "Pedra" and comp_name == "Tesoura":
        print 'Voce escolheu Pedra'
        print 'O computador escolheu ' + str (comp_name)
        print "Jogador ganhou!"
    elif Jogador == "Pedra" and comp_name == "Pedra":
        print 'Voce escolheu Pedra'
        print 'O computador escolheu ' + str (comp_name)
        print "Empate!"
    elif Jogador == "Pedra" and comp_name == "Papel":
        print 'Voce escolheu Pedra'
        print 'O computador escolheu ' + str (comp_name)
        print "Computador ganhou!"
    elif Jogador == "Pedra" and comp_name == "Spock":
        print 'Voce escolheu Pedra'
        print 'O computador escolheu ' + str (comp_name)
        print "Computador Ganhou!"
    print ("-"*50)
    
def button_papel():
    comp_name = random.choice(Opcoes)
    Jogador = "Papel"
    if Jogador == "Papel" and comp_name == "Pedra":
        print 'Voce escolheu Papel'
        print 'O computador escolheu ' + str (comp_name)
        print "Jogador ganhou!"
    elif Jogador == "Papel" and comp_name == "Spock":
        print 'Voce escolheu Papel'
        print 'O computador escolheu ' + str (comp_name)
        print "Jogador ganhou!"
    elif Jogador == "Papel" and comp_name == "Papel":
        print 'Voce escolheu Papel'
        print 'O computador escolheu ' + str (comp_name)
        print "Empate!"
    elif Jogador == "Papel" and comp_name == "Lagarto":
        print 'Voce escolheu Papel'
        print 'O computador escolheu ' + str (comp_name)
        print "Computador ganhou!"
    elif Jogador == "Papel" and comp_name == "Tesoura":
        print 'Voce escolheu Papel'
        print 'O computador escolheu ' + str (comp_name)
        print "Computador Ganhou!"
    print ("-"*50)
    
def button_tesoura():
    comp_name = random.choice(Opcoes)
    Jogador = "Tesoura"
    if Jogador == "Tesoura" and comp_name == "Papel":
        print 'Voce escolheu Tesoura'
        print 'O computador escolheu ' + str (comp_name)
        print "Jogador ganhou!"
    elif Jogador == "Tesoura" and comp_name == "Lagarto":
        print 'Voce escolheu Tesoura'
        print 'O computador escolheu ' + str (comp_name)
        print "Jogador ganhou!"
    elif Jogador == "Tesoura" and comp_name == "Tesoura":
        print 'Voce escolheu Tesoura'
        print 'O computador escolheu ' + str (comp_name)
        print "Empate!"
    elif Jogador == "Tesoura" and comp_name == "Spock":
        print 'Voce escolheu Tesoura'
        print 'O computador escolheu ' + str (comp_name)
        print "Computador ganhou!"
    elif Jogador == "Tesoura" and comp_name == "Pedra":
        print 'Voce escolheu Tesoura'
        print 'O computador escolheu ' + str (comp_name)
        print "Computador Ganhou!"
    print ("-"*50)
    
def button_spock():
    comp_name = random.choice(Opcoes)
    Jogador = "Spock"
    if Jogador == "Spock" and comp_name == "Tesoura":
        print 'Voce escolheu Spock'
        print 'O computador escolheu ' + str (comp_name)
        print "Jogador ganhou!"
    elif Jogador == "Spock" and comp_name == "Pedra":
        print 'Voce escolheu Spock'
        print 'O computador escolheu ' + str (comp_name)
        print "Jogador ganhou!"
    elif Jogador == "Spock" and comp_name == "Spock":
        print 'Voce escolheu Spock'
        print 'O computador escolheu ' + str (comp_name)
        print "Empate!"
    elif Jogador == "Spock" and comp_name == "Lagarto":
        print 'Voce escolheu Spock'
        print 'O computador escolheu ' + str (comp_name)
        print "Computador ganhou!"
    elif Jogador == "Spock" and comp_name == "Papel":
        print 'Voce escolheu Spock'
        print 'O computador escolheu ' + str (comp_name)
        print "Computador Ganhou!"
    print ("-"*50)
            
def button_lagarto():
    comp_name = random.choice(Opcoes)
    Jogador = "Lagarto"
    if Jogador == "Lagarto" and comp_name == "Spock":
        print 'Voce escolheu Lagarto'
        print 'O computador escolheu ' + str (comp_name)
        print "Jogador ganhou!"
    elif Jogador == "Lagarto" and comp_name == "Papel":
        print 'Voce escolheu Lagarto'
        print 'O computador escolheu ' + str (comp_name)
        print "Jogador ganhou!"
    elif Jogador == "Lagarto" and comp_name == "Lagarto":
        print 'Voce escolheu Lagarto'
        print 'O computador escolheu ' + str (comp_name)
        print "Empate!"
    elif Jogador == "Lagarto" and comp_name == "Pedra":
        print 'Voce escolheu Lagarto'
        print 'O computador escolheu ' + str (comp_name)
        print "Computador ganhou!"
    elif Jogador == "Lagarto" and comp_name == "Tesoura":
        print 'Voce escolheu Lagarto'
        print 'O computador escolheu ' + str (comp_name)
        print "Computador Ganhou!"
    print ("-"*50)
    
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 230)
frame.add_button("Pedra", button_pedra,90)
frame.add_button("Papel", button_papel,90)
frame.add_button("Tesoura", button_tesoura,90)
frame.add_button("Spock", button_spock,90)
frame.add_button("Lagarto", button_lagarto,90)
frame.set_canvas_background('Purple')
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
