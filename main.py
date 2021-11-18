import random

def botRespuestasPlanas():
    print("\nBot a la escucha... (pregunta cuando quieras) -- Si no quieres preguntar nada escribe: Salir -- ")
    salir_opcion = False
    while not salir_opcion:
        pregunta = input("> ")
        if pregunta in preguntas_respuestas:
            print("> " + preguntas_respuestas[pregunta])
        elif pregunta == "Salir":
            salir_opcion = True
        else:
            print("No entiendo su pregunta")


def botRespuestasRegex():
    print("\nBot a la escucha... (pregunta cuando quieras) -- Si no quieres preguntar nada escribe: Salir -- ")
    salir_opcion = False
    while not salir_opcion:
        pregunta = input("> ")
        if pregunta == "¿Que equipo de futbol juega hoy?":
            botRespuestasRegex1()
        elif pregunta == "¿Cuando es la próxima carrera de formula 1?":
            botRespuestasRegex2()
        elif pregunta == "¿Que tiempo va a hacer mañana?":
            botRespuestasRegex4()
        elif pregunta == "¿Dime un número aleatorio del 1 al 10?":
            botRespuestasRegex5()
        elif pregunta == "Salir":
            salir_opcion = True
        else:
            print("No entiendo su pregunta")


def botRespuestasRegex1():
    repuesta = ["Real Betis", "Real Madrid", "Barcelona", "Livepool", "Getafe", "Real Sociedad", "Monaco", "PSG"]
    random_index = random.randint(0, len(repuesta) - 1)
    print(repuesta[random_index])

def botRespuestasRegex2():
    repuesta = ["28-28 de marzo en Sakhir.", "16-18 de abril en Imola.", "30-2 de mayo e Portimao.", "7-9 de mayo en Catalunya.", "20-23 de mayo en Montecarlo.", "4-6 de junio en Baku city circuit."]
    random_index = random.randint(0, len(repuesta) - 1)
    print("La próxima carrera sera del", repuesta[random_index])

def botRespuestasRegex4():
    repuesta = ["llovizna.", "lluvia.", "nieve.", "granizo.", "agua y nieve.", "lluvia congelada."]
    random_index = random.randint(0, len(repuesta) - 1)
    print("Mañana la prediccion es de", repuesta[random_index])

def botRespuestasRegex5():
    random_index = random.randrange(1, 10)
    print(random_index)


preguntas_respuestas = {"¿Que equipo de futbol juega hoy?": "Eso no se decirtelo",
                        "¿Cuando es la próxima carrera de formula 1? ": "Eso nose decirtelo",
                        "¿Que día es mañana?": "Miercoles",
                        "¿Que tiempo va a hacer mañana?": "Parcialmente todo el dia soleado.",
                        "¿Dime un número aleatorio del 1 al 10?": "7",
                        "Hola, soy Alex": "Muy buenas, Alex. Soy Botarate",
                        "¿Quien te ha creado?": "El Grupo 3"}
salir = False
opcion = 0

print("\t\t\t\t\t\033[1m\033[4mAPLICACIÓN BOT-ARATE\033[0m \n")
while not salir:
    print("\t\t\t1) Bot simple (respuestas planas...)")
    print("\t\t\t2) Bot simple (respuestas REGEX)")
    print("\t\t\t3) Bot simple mejorado desde fichero")
    print("\t\t\t4) Informe de la conversación (PDF)")
    print("\t\t\t5) Salir\n")
    opcion = int(input("\t\t\tOpcion: "))

    if opcion == 1:
        botRespuestasPlanas()
    elif opcion == 2:
        botRespuestasRegex()
    elif opcion == 3:
        print("\t\t\t3) Bot simple mejorado desde fichero")
    elif opcion == 4:
        print("\t\t\t4) Informe de la conversación (PDF)")
    elif opcion == 5:
        print("\t\t\t5) Salir\n")
        salir = True
