<<<<<<< HEAD
from random import shuffle


def baraja():
    return [(n,p) for n in ['A','J','Q','K']+[str(x) for x in range(2,11)] for p in ['Picas', 'Corazones', 'Trevoles', 'Diamantes']]

def mezclar(baraja):
    shuffle(baraja)
    return baraja

def sacar_carta(mazo):
    if mazo ==[]:
        pass
    else:
        print(mazo[0])
        sacar_carta(mazo[1:])

def valor_carta(carta):
    if carta[0] in ['J', 'Q', 'K']:
        return 10
    elif carta[0] == 'A':
        return 1
    else:
        return int(carta[0])

def valor_mano(mano):
    if mano == []:
        return 0
    return valor_carta(mano[0]) + valor_mano(mano[1:])

def valor_mano_recargado(mano):
    if mano == 0:
        return 0
    elif valor_mano(mano) <= 11 and 1 in [valor_carta(x) for x in mano]:
        return valor_mano(mano) + 10
    else:
        return valor_mano(mano)


def jugar(mazo, jugador, repartidor):
    print (jugador, repartidor)
    if len(mazo) > 48:
        jugar(mazo[2:], jugador+[mazo[0]], repartidor+[mazo[1]])
    else: 
        if len(mazo) > 2 and valor_mano_recargado(jugador) < 21:
            if input("Pedir carta(s/n): ").capitalize() == "S":
                jugar(mazo[2:], jugador+[mazo[0]], repartidor)
            else:
                print("Evaluar quién gana")
        else:
            print("Game over :v")

#print(mezclar(baraja()))
#sacar_carta(mezclar(baraja()))
#print(valor_mano_recargado(mezclar(baraja())[:2]))
jugar(mezclar(baraja()), [], [])
=======
from random import *

while True:
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

    def suma(cartas):
        equivalencia(cartas)
        return sum([x for x in cartas if cartas.index(x)%2==0]), cartas

    def juega():
        return llena_jugador1(genera_mazo())

    print(suma(juega().copy()))

    if input("¿Pedir carta? y/n \n").capitalize()=="Y":
        print("Pidiendo nueva carta")
        break
    else:
        break

>>>>>>> 510c3a53e98c4ad66b745c17595786cf5cf4d3b5
