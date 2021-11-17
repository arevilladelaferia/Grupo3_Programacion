def botRespuestasPlanas():
    salir_opcion = False
    while not salir_opcion:
        print("\nBot a la escucha... (pregunta cuando quieras) -- Si no quieres preguntar nada escribe: Salir -- ")
        pregunta = input("> ")
        if pregunta in preguntas_respuestas:
            print("> " + preguntas_respuestas[pregunta])
        elif pregunta == "Salir":
            salir_opcion = True
        else:
            print("No entiendo su pregunta")


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
        print("\t\t\t2) Bot simple (respuestas REGEX)")
    elif opcion == 3:
        print("\t\t\t3) Bot simple mejorado desde fichero")
    elif opcion == 4:
        print("\t\t\t4) Informe de la conversación (PDF)")
    elif opcion == 5:
        print("\t\t\t5) Salir\n")
        salir = True
