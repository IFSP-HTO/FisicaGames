# Fun��o que retorna o n�mero formatado em minutos e segundos
# criada por Yasmin Deodato
# Dispon�vel em: http://www.codeskulptor.org/#user46_AIzow1OQQd_4.py
####################################################################
import random

# Fun��o de formata��o do tempo
def format_time(number):
    return "%s minutos e %s segundos"%(number/60, number)

def random_number():
    return random.randrange(0, 3600)

###################################################
# Testes

print format_time(23)
print format_time(1237)
print format_time(0)
print format_time(1860)

###################################################
# Sa�da no console
#0 minutos e 23 segundos
#20 minutos e 37 segundos
#0 minutos e 0 segundos
#31 minutos e 0 segundos
