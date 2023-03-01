from random import choice

gestures = ['piedra','papel','tijeras','lagarto','Spock']
n_rondas = int(input("Elija el numero de rondas a jugar (numero impar):"))
rondas_p_ganar = int((n_rondas // 2) + 1)
cpu_score = 0
player_score = 0
n_partida = 0

def seleccion_cpu():
    for i in range(1):
        cpu_option = (choice(gestures))
        
    return cpu_option


def seleccion_jugador():
    player_option = input("Seleccione una opcion, piedra, papel, tijeras, lagarto, Spock: ")

    while player_option not in gestures:
        print("Su seleccion no es valida, intente de nuevo.")
        print("Valide que su opción este bien escita.")
        player_option = input("Seleccione una opcion, piedra, papel, tijeras, lagarto, Spock: ")
    
    return player_option


#piedra, papel o tijeras, lagarto,Spock
#1 gana la computadora
#2 gana el jugador

def reglas_de_juego(player_option, cpu_option):
    
    resultado_partida = 0
    #Empate
    if player_option == cpu_option:
        resultado_partida = 0
    #Piedra
    elif player_option == "piedra":
        if cpu_option == "papel":
            resultado_partida = 1
        elif cpu_option== "lagarto":
            resultado_partida = 2
        elif cpu_option == "Spock":
            resultado_partida = 1
        else:
            resultado_partida = 2
    #Papel
    elif player_option == "papel":
        if cpu_option == "tijeras":
            resultado_partida = 1
        elif cpu_option == "lagarto":
            resultado_partida = 1
        elif cpu_option == "Spock":
            resultado_partida = 2
        else:
            resultado_partida = 2    
    #Tijeras
    elif player_option == "tijeras":
        if cpu_option == "piedra":
            resultado_partida = 1
        elif cpu_option == "Spock":
            resultado_partida = 1
        elif cpu_option == "lagarto":
            resultado_partida = 2
        else:
            resultado_partida = 2    
    #Lagarto
    elif player_option == "lagarto":
        if cpu_option == "piedra":
            resultado_partida = 1
        elif cpu_option == "tijeras":
            resultado_partida = 1
        elif cpu_option == "Spock":
            resultado_partida = 2
        else:
            resultado_partida = 2    
    #Spock
    elif player_option == "Spock":
        if cpu_option == "lagarto":
            resultado_partida = 1
        elif cpu_option == "papel":
            resultado_partida = 1
        elif cpu_option == "piedra":
            resultado_partida = 2
        else:
            resultado_partida = 2    
    
    return resultado_partida


def variables_juego(resultado_partida):
    
    global cpu_score
    global player_score
    global n_partida
    
    if resultado_partida == 0:
        n_partida +=1
        estatus_partida = "Empate"
    elif resultado_partida == 1:
        cpu_score +=1
        n_partida +=1
        estatus_partida = "Compu Gana"
    elif resultado_partida ==2:
        player_score +=1
        n_partida +=1
        estatus_partida = "Usuario Gana"
    else:
        cpu_score = 0
        player_score = 0
    
    print("-----------------------------------------------")
    print("                                               ")
    print("Vamos en la partida no:",n_partida)
    print("El resultado de la partida es:",estatus_partida)
    print("Puntaje de la Compu:",cpu_score)
    print("Puntaje del usuario es:",player_score)
    
    return cpu_score,player_score,estatus_partida,n_partida


 
while n_partida != n_rondas:
    #llamamos la funcion de la opcion de la computadora
    cpu = seleccion_cpu()
    #Llamamos la funcion de la opcion de la computadora
    jugador = seleccion_jugador()
    #Llamamos la funcion de lar reglas de juego
    juego = reglas_de_juego(jugador,cpu)
    #llamamos las variables del juego
    variables_juego(juego)
    if n_partida >= n_rondas:
        print("-----------------------------------------------")
        print("                                               ")
        print("El juego ah acabado")
        if cpu_score > player_score:
            print("Computadora ah ganado")
            y_n = input("Desea un juego nuevo?: y/n")
            if y_n =="y":
                n_partida = 0
                cpu_score = 0
                player_score = 0           
            else:
                break
        else:
            print("Jugador ah ganado")
            y_n = input("Desea un juego nuevo?: y/n")
            if y_n =="y":
                n_partida = 0
                cpu_score = 0
                player_score = 0            
            else:
                break
    