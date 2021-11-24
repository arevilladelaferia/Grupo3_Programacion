from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from datetime import date
from collections import defaultdict

today = date.today()  # Fecha del sistema en el momento de la conversión a pdf ¿¿Fecha de conversación original??

conversacion = open('conversación.txt', "r", encoding="utf-8")
lines = conversacion.read()
c = canvas.Canvas("conversación.pdf", pagesize=A4)
y = 500

for line in lines.split('\n'):
    c.drawString(50, y, line)
    y = y - 25


numcar = len(lines)  # Conteo de carácteres
listpal = lines.split()  # Split de la cadena
numpal = len(listpal)  # Conteo de palabras en cadena

temp = defaultdict(int)

for sub in listpal:
    for wrd in sub.split():
        temp[wrd] += 1

palrep = max(temp, key=temp.get)
numrep = listpal.count(palrep)

c.drawImage("img.png", 100, 600, width=400, height=200)  # Imagen del directorio
c.drawString(100, 575, 'INFORME DE LA CONVERSACIÓN')
c.drawString(50, 100, 'La conversación es del '+str(today)+'.')  # CAMBIAR A FECHA DE LA CONVERSACIÓN DESDE TXT
c.drawString(50, 75, 'Consta de '+str(numcar)+' caracteres.')
c.drawString(50, 50, 'Está compuesta por '+str(numpal)+' palabras.')
c.drawString(50, 25, 'La palabra '+str(palrep)+' se repite '+str(numrep)+' veces.')
c.save()
