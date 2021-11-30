import random
import re
from datetime import datetime, timedelta


def botRespuestasPlanas():
    print("\nBot a la escucha... (pregunta cuando quieras) -- Si no quieres preguntar nada escribe: Salir -- ")
    salir_opcion = False
    while not salir_opcion:
        pregunta = input("> ")
        if pregunta in preguntas_respuestas:
            print("> " + preguntas_respuestas[pregunta])
        elif pregunta == "Salir":
            salir_opcion = True
        elif pregunta == "salir":
            salir_opcion = True
        else:
            print("No entiendo su pregunta")


def botRespuestasRegex():
    print("\nBot a la escucha... (pregunta cuando quieras) -- Si no quieres preguntar nada escribe: Salir -- ")
    salir_opcion = False
    while not salir_opcion:
        pregunta = input("> ")
        patron = "^Hola|^hola|Soy|soy"
        patron2 = "(Carrera|carrera)*(Formula 1|formula 1)"
        patron3 = "(Equipo|equipo)*(Futbol|futbol)"
        patron4 = "(Tiempo|tiempo)"
        patron5 = "(Número|número)*(Aleatorio|aleatorio)"
        patron6 = "(Dia|dia)*(Mañana|mañana)"
        patron7 = "(Quien|quien)*(Creado|creado)"
        patron8 = "(Salir|salir)"

        if re.search(patron, pregunta):
            botRespuestasRegexsaludo(pregunta)
        elif re.search(patron2, pregunta):
            botRespuestasRegexformula1()
        elif re.search(patron3, pregunta):
            botRespuestasRegexequipo()
        elif re.search(patron4, pregunta):
            botRespuestasRegextiempo()
        elif re.search(patron5, pregunta):
            botRespuestasRegexnumale()
        elif re.search(patron6, pregunta):
            botRespuestasRegexdia()
        elif re.search(patron7, pregunta):
            botRespuestasRegexcreado()
        elif re.search(patron8, pregunta):
            break
        else:
            print("No entiendo su pregunta")


def botRespuestasRegexcreado():
    print("> Me ha creado el grupo 3")


def botRespuestasRegexsaludo(pregunta):
    nombre = pregunta.split()
    print("> Muy buenas " + nombre[-1] + ", Soy Botarate:")


def botRespuestasRegexequipo():
    repuesta = ["Real Betis", "Real Madrid", "Barcelona", "Livepool", "Getafe", "Real Sociedad", "Monaco", "PSG"]
    random_index = random.randint(0, len(repuesta) - 1)
    print("> Hoy juega el " + repuesta[random_index])


def botRespuestasRegexformula1():
    repuesta = ["28-29 de marzo en Sakhir.", "16-18 de abril en Imola.", "30-2 de mayo e Portimao.",
                "7-9 de mayo en Catalunya.", "20-23 de mayo en Montecarlo.", "4-6 de junio en Baku city circuit."]
    random_index = random.randint(0, len(repuesta) - 1)
    print("> La próxima carrera sera del", repuesta[random_index])


def botRespuestasRegextiempo():
    repuesta = ["llovizna.", "lluvia.", "nieve.", "granizo.", "agua y nieve.", "lluvia congelada."]
    random_index = random.randint(0, len(repuesta) - 1)
    print("> La prediccion de hoy es de", repuesta[random_index])


def botRespuestasRegexnumale():
    print("> Su numero aleatorio es:", random.randint(1, 9999999))


def botRespuestasRegexdia():
    dias = {'0': 'Domingo', '1': 'lunes', '2': 'Martes', '3': 'Miércoles', '4': 'Jueves', '5': 'Viernes', '6': 'Sábado'}

    hoy = datetime.today()  # Obtener la fecha de hoy
    hoy = hoy + timedelta(days=1)  # le sumamos un dia mas
    dia = hoy.strftime('%w')  # obtengo el numero de dia
    print("> Mañana será " + dias[dia])


preguntas_respuestas = {"¿Que equipo de futbol juega hoy?": "Hoy juega el Betis",
                        "¿Cuando es la próxima carrera de formula 1?": "28-29 de marzo en Sakhir.",
                        "¿Que día es mañana?": "Mañana será Miercoles",
                        "¿Que tiempo va a hacer hoy?": "Parcialmente todo el dia soleado.",
                        "¿Dime un número aleatorio del 1 al 10?": "Su numero aleatorio es: 929293",
                        "Hola, soy Alex": "Muy buenas, Alex. Soy Botarate",
                        "¿Quien te ha creado?": "Me ha creado el grupo 3"}
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
