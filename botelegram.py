from telegram.ext import (Updater, CommandHandler)
import random


def ods_aleatorio():
    ods_list = [
        "Erradicar la pobreza en todas sus formas sigue siendo uno de los principales desafíos que enfrenta la humanidad. Si bien la cantidad de personas que viven en la extrema pobreza disminuyó en más de la mitad entre 1990 y 2015, aún demasiadas luchan por satisfacer las necesidades más básicas. ",
        "Desgraciadamente, el hambre y la desnutrición siguen siendo grandes obstáculos para el desarrollo de muchos países. Se estima que 821 millones de personas sufrían de desnutrición crónica al 2017, a menudo como consecuencia directa de la degradación ambiental, la sequía y la pérdida de biodiversidad. Más de 90 millones de niños menores de cinco años tienen un peso peligrosamente bajo. La desnutrición y la inseguridad alimentaria parece estar incrementándose tanto en casi todas las de regiones de África, como en América del Sur.",
        "La buena salud es esencial para el desarrollo sostenible, y la Agenda 2030 refleja la complejidad y la interconexión de ambos. Toma en cuenta la ampliación de las desigualdades económicas y sociales, la rápida urbanización, las amenazas para el clima y el medio ambiente, la lucha continua contra el VIH y otras enfermedades infecciosas, y los nuevos problemas de salud, como las enfermedades no transmisibles. La cobertura universal de salud será integral para lograr el ODS 3, terminar con la pobreza y reducir las desigualdades. Las prioridades de salud global emergentes que no se incluyen explícitamente en los ODS, incluida la resistencia a los antimicrobianos, también demandan acción.",
        ""]
    return random.choice(ods_list)


def inicio(update, context):
    # Enviar un mensaje a un ID determinado.
    context.bot.send_message(update.message.chat_id, "Oído cocina. Tú dirás...")


def ods(update, context):
    # Enviar un mensaje a un ID determinado.
    context.bot.send_message(update.message.chat_id, ods_aleatorio())


def cita(update, context):
    # Enviar un mensaje a un ID determinado.
    context.bot.send_message(update.message.chat_id,
                             "Un problema se transforma en desafío cuando le pones fecha de solución. (Anónimo)")


def final(update, context):
    # Enviar un mensaje a un ID determinado.
    context.bot.send_message(update.message.chat_id,
                             "¡Que pases un buen día!")


TOKEN = "2119015416:AAEvm_Tf4oNQZaDlGr3JkM4Gt8L7G52yAH8"
updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

# Eventos que activarán nuestro bot.
dp.add_handler(CommandHandler('inicio', inicio))
dp.add_handler(CommandHandler('ods', ods))
dp.add_handler(CommandHandler('cita', cita))
dp.add_handler(CommandHandler('final', final))

# Comienza el bot
updater.start_polling()
# Lo deja a la escucha. Evita que se detenga.
updater.idle()
