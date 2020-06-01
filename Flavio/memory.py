# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global cartas, state, vistas, descobertas, numeros
    cartas = range(9)
    vistas = [-1,-1]
    descobertas = []
    numeros = range(5) + range(5)
    random.shuffle(numeros)
    print numeros
    state = 0
    
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global cartas, state, vistas, descobertas, numeros
    

    if state == 0:
        state = 1
        for ind in range(10):
            if pos[0] > ind*80 and pos[0] < ind*80 + 80:
                vistas[0] = ind
                
    elif state == 1:
        for ind in range(10):
            if pos[0] > ind*80 and pos[0] < ind*80 + 80:
                if vistas[0] != ind:
                    vistas[1] = ind
                    state = 2
                    
                    if numeros[vistas[0]] == numeros[vistas[1]]:
                        descobertas.append(vistas[0])
                        descobertas.append(vistas[1])

                
        
                                
    else:
        state = 1
        vistas = [-1,-1]
        for ind in cartas:
            if pos[0] > ind*80 and pos[0] < ind*80 + 80 and ind not in vistas:
                vistas[0] = ind

    
# cards are logically 50x100 pixels in size    
def draw(canvas):
    
    global cartas, vistas
    for larg in range(10):
        canvas.draw_polygon([[larg*80, 0], [larg*80, 100], [larg*80+80, 100], [larg*80+80, 0]], 12, 'Red', 'Green')
    for larg in vistas:
        canvas.draw_polygon([[larg*80, 0], [larg*80, 100], [larg*80+80, 100], [larg*80+80, 0]], 12, 'Red', 'Black')
        canvas.draw_text(str(numeros[larg]), [larg*80+30, 60] ,36, 'White')
    for larg in descobertas:
        canvas.draw_polygon([[larg*80, 0], [larg*80, 100], [larg*80+80, 100], [larg*80+80, 0]], 12, 'Red', 'Black')
        canvas.draw_text(str(numeros[larg]), [larg*80+30, 60] ,36, 'White')

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
