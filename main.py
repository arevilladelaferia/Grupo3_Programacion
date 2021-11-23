from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from datetime import date

today = date.today()  # Fecha del sistema en el momento de la conversión a pdf ¿¿Fecha de conversación original??

c = canvas.Canvas("conversación.pdf", pagesize=A4)
conversacion = open('conversación.txt', encoding="utf-8").read()
c.drawString(50, 600, str(conversacion))  # Los saltos de línea no se imprimen como carácteres reconocibles
c.drawString(50, 400, 'La conversación es del '+str(today))
c.save()
