import random
baraja = {'Ace': 1, 'Dos': 2, 'Tres': 3, 'Cuatro': 4, 'Cinco': 5, 'Seis': 6, 'Siete': 7, 'Ocho': 8, 'Nueve': 9, 'Diez': 10, 'Jota': 10, 'Queena': 10, 'Kaiser': 10}

def repartir_cartas():
    Baraja = []
    for x in range(2):
        carta = random.choice(list(baraja.keys()))
        Baraja.append(carta)
    return Baraja

def pedir_carta():
    carta = random.choice(list(baraja.keys()))
    return carta

def jugar_computadora():
    Baraja_computadora = repartir_cartas()
    while sumar_cartas(Baraja_computadora) < 17:
        Baraja_computadora.append(pedir_carta())
    return Baraja_computadora

def sumar_cartas(Baraja):
    total = 0
    for carta in Baraja:
        total += baraja[carta]
    return total

def determinar_ganador(Baraja_jugador, Baraja_computadora):
    total_jugador = sumar_cartas(Baraja_jugador)
    total_computadora = sumar_cartas(Baraja_computadora)
    if total_jugador > 21:
        return 'La Maquina te ganó. perdiste.'
    elif total_computadora > 21:
        return 'Felicidades, ganaste.'
    elif total_jugador > total_computadora:
        return 'Felicidades, ganaste.'
    elif total_computadora > total_jugador:
        return 'La computadora te ganó, perdiste'
    else:
        return 'Empate.'
        
print('Bienvenido al 21')
Baraja_jugador = repartir_cartas()
Baraja_computadora = jugar_computadora()
print('Tu baraja:', Baraja_jugador)
while True:
    opcion = input('¿Quieres sacar una carta? (s/n): ')
    if opcion == 's':
        Baraja_jugador.append(pedir_carta())
        print('Tu baraja:', Baraja_jugador)
        if sumar_cartas(Baraja_jugador) > 21:
            print('Perdiste')
            break
    else:
        break
    print('La baraja de la maquina:', Baraja_computadora)
print(determinar_ganador(Baraja_jugador, Baraja_computadora))