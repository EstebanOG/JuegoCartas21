from random import *

def genera_mazo():
    return [(numero,tipo) for numero in ['A','K','Q','J']+[x for x in range(2,11)] for tipo in ('corazones','picas','treboles','diamantes')]

def genera_carta(mazo):
    return choice(mazo)

def limpia_mazo(carta,mazo):
    mazo.remove(carta)
    return carta

def llena_jugador1(mazo):
    return [x for x in range(0,2) for x in limpia_mazo(genera_carta(mazo), mazo)]

def equivalencia(cartas):
    aux=0
    for x in cartas:
        if x=='K' or x=='Q' or x=='J':
            cartas[aux]=10
        elif x=='A':
            cartas[aux]=11
        aux+=1
    return cartas

print("Las dos cartas son: ",llena_jugador1(genera_mazo()))
