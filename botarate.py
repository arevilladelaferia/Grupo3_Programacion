import re
import json
import random
from datetime import datetime, timedelta
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from datetime import date
from collections import defaultdict
from reportlab.lib.units import mm


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


def guardarinfotxt(pregunta, respuesta_pregunta):
    with open("conversación.txt", "a") as f:
        conversacion = "> " + str(pregunta) + "\n> " + str(respuesta_pregunta + "\n")
        f.write(conversacion)


def bot_ficheros():
    print("\nBot a la escucha... (pregunta cuando quieras) -- Si no quieres preguntar nada escribe: Salir -- ")
    salir_opcion = False
    while not salir_opcion:
        with open('pyr.json', 'w') as f:
            pyr = {"pregunta1": "^Hola|^hola|Soy|soy",
                   "respuesta1": "Muy buenas, (variable). Soy Botarate",
                   "pregunta2": "(Carrera|carrera)*(Formula 1|formula 1)",
                   "respuesta2": "La próxima carrera sera del (variable)",
                   "pregunta3": "(Equipo|equipo)*(Futbol|futbol)",
                   "respuesta3": "Hoy juega el (variable)",
                   "pregunta4": "(Tiempo|tiempo)",
                   "respuesta4": "La prediccion de hoy es de (variable)",
                   "pregunta5": "(Número|número)*(Aleatorio|aleatorio)",
                   "respuesta5": "Su numero aleatorio es: (variable)",
                   "pregunta6": "(Dia|dia)*(Mañana|mañana)",
                   "respuesta6": "Mañana será (variable)",
                   "pregunta7": "(Quien|quien)*(Creado|creado)",
                   "respuesta7": "Me ha creado el grupo 3",
                   "pregunta8": "(Salir|salir)"
                   }
            json.dump(pyr, f)

        with open('pyr.json', 'r') as f:
            conj_datos = json.load(f)

        with open("conversación.txt", "w") as f:
            f.close()
        while True:
            pregunta = input("> ")
            if re.search(conj_datos["pregunta1"], pregunta):
                nombre = pregunta.split()
                respuesta_pregunta = conj_datos["respuesta1"]
                respuesta_pregunta = respuesta_pregunta.replace("(variable)", nombre[-1])
                print(">", respuesta_pregunta)
                guardarinfotxt(pregunta, respuesta_pregunta)

            elif re.search(conj_datos["pregunta2"], pregunta):
                respuesta = ["28-29 de marzo en Sakhir.", "16-18 de abril en Imola.", "30-2 de mayo e Portimao.",
                             "7-9 de mayo en Catalunya.", "20-23 de mayo en Montecarlo.",
                             "4-6 de junio en Baku city circuit."]
                random_index = random.randint(0, len(respuesta) - 1)
                respuesta_pregunta = conj_datos["respuesta2"]
                respuesta_pregunta = respuesta_pregunta.replace("(variable)", respuesta[random_index])
                print(">", respuesta_pregunta)
                guardarinfotxt(pregunta, respuesta_pregunta)

            elif re.search(conj_datos["pregunta3"], pregunta):
                respuesta = ["Real Betis", "Real Madrid", "Barcelona", "Livepool", "Getafe", "Real Sociedad", "Monaco",
                             "PSG"]
                random_index = random.randint(0, len(respuesta) - 1)
                respuesta_pregunta = conj_datos["respuesta3"]
                respuesta_pregunta = respuesta_pregunta.replace("(variable)", respuesta[random_index])
                print(">", respuesta_pregunta)
                guardarinfotxt(pregunta, respuesta_pregunta)

            elif re.search(conj_datos["pregunta4"], pregunta):
                respuesta = ["llovizna.", "lluvia.", "nieve.", "granizo.", "agua y nieve.", "lluvia congelada."]
                random_index = random.randint(0, len(respuesta) - 1)
                respuesta_pregunta = conj_datos["respuesta4"]
                respuesta_pregunta = respuesta_pregunta.replace("(variable)", respuesta[random_index])
                print(">", respuesta_pregunta)
                guardarinfotxt(pregunta, respuesta_pregunta)

            elif re.search(conj_datos["pregunta5"], pregunta):
                respuesta = random.randint(1, 9999999)
                respuesta_pregunta = conj_datos["respuesta5"]
                respuesta_pregunta = respuesta_pregunta.replace("(variable)", str(respuesta))
                print(">", respuesta_pregunta)
                guardarinfotxt(pregunta, respuesta_pregunta)

            elif re.search(conj_datos["pregunta6"], pregunta):
                respuesta = {'0': 'Domingo', '1': 'lunes', '2': 'Martes', '3': 'Miércoles', '4': 'Jueves',
                             '5': 'Viernes',
                             '6': 'Sábado'}
                hoy = datetime.today()  # Obtener la fecha de hoy
                hoy = hoy + timedelta(days=1)  # le sumamos un dia mas
                dia = hoy.strftime('%w')  # obtengo el numero de dia
                respuesta_pregunta = conj_datos["respuesta6"]
                respuesta_pregunta = respuesta_pregunta.replace("(variable)", respuesta[dia])
                print(">", respuesta_pregunta)
                guardarinfotxt(pregunta, respuesta_pregunta)

            elif re.search(conj_datos["pregunta7"], pregunta):
                respuesta_pregunta = conj_datos["respuesta7"]
                print(">", respuesta_pregunta)
                guardarinfotxt(pregunta, respuesta_pregunta)

            elif re.search(conj_datos["pregunta8"], pregunta):
                salir_opcion = True
                break
            else:
                guardarinfotxt(pregunta, "No entiendo su pregunta")
                print("No entiendo su pregunta")


def botInformeConver():
    today = date.today()  # Obtenemos fecha del sistema
    conversacion = open('conversación.txt', "r", encoding="utf-8")  # Abrimos conversación.txt
    lines = conversacion.read()
    lines2 = ""
    c = canvas.Canvas("conversación.pdf", pagesize=A4)  # Creamos el pdf
    y = 500

    c.drawImage("chatbot_python.jpg", 100, 600, width=400, height=200)  # Imagen del directorio
    c.drawString(100, 575, 'INFORME DE LA CONVERSACIÓN')

    for line in lines.split('\n'):  # Con un replace eliminamos ">" y los espacios para que el programa no los cuente como palabras
        line = line.replace(" ", "")
        line = line.replace(">", "")
        lines2 += line

    numcar = len(lines2)  # Conteo de carácteres
    lines2 = ""
    for line in lines.split("\n"):
        line = line.replace(">", " ")
        lines2 += line

    listpal = lines2.split()  # Split de la cadena
    numpal = len(listpal)  # Conteo de palabras en cadena

    temp = defaultdict(int)

    lines2 = ""
    for line in lines.split('\n'):
        line = line.replace(">", " ")
        line = line.replace(".", " ")
        line = line.replace(",", " ")
        lines2 += line

    listpal2 = lines2.split()  # Split de la cadena
    for sub in listpal2:
        for wrd in sub.split():
            temp[wrd] += 1

    palrep = max(temp, key=temp.get)  # En estas variables se almacenan la palabra más repetida y el nº de veces
    numrep = listpal2.count(palrep)

    def addpagenumber():  # Función para escribir el número de página
        page_num = c.getPageNumber()
        text = "Página #%s" % page_num
        c.drawRightString(200 * mm, 20 * mm, text)

    for line in lines.split('\n'):  # Vamos escribiendo línea por línea en el pdf
        c.drawString(50, y, line)
        y = y - 25  # Así hacemos que cada línea esté separada por 25 pixeles
        if y == 25:  # Al llegar a la altura que deseamos, se imprime el nº de página y se salta a la página siguiente
            addpagenumber()
            c.showPage()
            y = 800  # Establecemos la altura arriba del documento para la siguiente página y repetimos

    addpagenumber()  # Para imprimir el número de página de la página final
    c.drawString(50, y - 25, 'La conversación es del ' + str(today) + '.')  # Datos del informe de la conversación
    c.drawString(50, y - 50, 'Consta de ' + str(numcar) + ' caracteres.')
    c.drawString(50, y - 75, 'Está compuesta por ' + str(numpal) + ' palabras.')
    c.drawString(50, y - 100, 'La palabra ' + str(palrep) + ' se repite ' + str(numrep) + ' veces.')
    c.save()  # Guardamos documento
    print("El PDF ha sido creado \n")


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
        bot_ficheros()
    elif opcion == 4:
        botInformeConver()
    elif opcion == 5:
        print("\t\t\t5) Salir\n")
        salir = True
