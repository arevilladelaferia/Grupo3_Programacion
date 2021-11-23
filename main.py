from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from datetime import date
from collections import defaultdict

today = date.today()  # Fecha del sistema en el momento de la conversión a pdf ¿¿Fecha de conversación original??

c = canvas.Canvas("conversación.pdf", pagesize=A4)
conversacion = open('conversación.txt', encoding="utf-8").read()
c.drawString(50, 500, str(conversacion))  # Los saltos de línea no se imprimen como carácteres reconocibles

numcar = len(conversacion)  # Conteo de carácteres
listpal = conversacion.split()  # Split de la cadena
numpal = len(listpal)  # Conteo de palabras en cadena

temp = defaultdict(int)

for sub in listpal:
    for wrd in sub.split():
        temp[wrd] += 1

palrep = max(temp, key=temp.get)
numrep = int(0)


for item in listpal:
    if palrep in listpal:
        numrep += 1
strnumrep = str(numrep)

c.drawImage("img.png", 100, 600, width=400, height=200)  # Imagen del directorio
c.drawString(100, 575, 'INFORME DE LA CONVERSACIÓN')
c.drawString(50, 100, 'La conversación es del '+str(today)+'.')  # CAMBIAR A FECHA DE LA CONVERSACIÓN DESDE TXT
c.drawString(50, 75, 'Consta de '+str(numcar)+' caracteres.')
c.drawString(50, 50, 'Está compuesta por '+str(numpal)+' palabras.')
c.drawString(50, 25, 'La palabra '+str(palrep)+' se repite '+strnumrep+' veces.')
c.save()
