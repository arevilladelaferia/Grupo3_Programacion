from telegram.ext import (Updater, CommandHandler)
import random


def ods_aleatorio():
    ods_list = [
        "Erradicar la pobreza en todas sus formas sigue siendo uno de los principales desafíos que enfrenta la humanidad. Si bien la cantidad de personas que viven en la extrema pobreza disminuyó en más de la mitad entre 1990 y 2015, aún demasiadas luchan por satisfacer las necesidades más básicas. ",
        "Los Objetivos de Desarrollo Sostenible buscan terminar con todas las formas de hambre y desnutrición para 2030 y velar por el acceso de todas las personas, en especial los niños, a una alimentación suficiente y nutritiva durante todo el año. Esta tarea implica promover prácticas agrícolas sostenibles a través del apoyo a los pequeños agricultores y el acceso igualitario a la tierra, la tecnología y los mercados. Además, se requiere el fomento de la cooperación internacional para asegurar la inversión en la infraestructura y la tecnología necesaria para mejorar la productividad agrícola.",
        "La buena salud es esencial para el desarrollo sostenible, y la Agenda 2030 refleja la complejidad y la interconexión de ambos. Toma en cuenta la ampliación de las desigualdades económicas y sociales, la rápida urbanización, las amenazas para el clima y el medio ambiente, la lucha continua contra el VIH y otras enfermedades infecciosas, y los nuevos problemas de salud, como las enfermedades no transmisibles. La cobertura universal de salud será integral para lograr el ODS 3, terminar con la pobreza y reducir las desigualdades. Las prioridades de salud global emergentes que no se incluyen explícitamente en los ODS, incluida la resistencia a los antimicrobianos, también demandan acción.",
        "El objetivo de lograr una educación inclusiva y de calidad para todos se basa en la firme convicción de que la educación es uno de los motores más poderosos y probados para garantizar el desarrollo sostenible. Con este fin, el objetivo busca asegurar que todas las niñas y niños completen su educación primaria y secundaria gratuita para 2030. También aspira a proporcionar acceso igualitario a formación técnica asequible y eliminar las disparidades de género e ingresos, además de lograr el acceso universal a educación superior de calidad.",
        "Garantizar el acceso universal a salud reproductiva y sexual y otorgar a la mujer derechos igualitarios en el acceso a recursos económicos, como tierras y propiedades, son metas fundamentales para conseguir este objetivo. Hoy más mujeres que nunca ocupan cargos públicos, pero alentar a más mujeres para que se conviertan en líderes ayudará a alcanzar una mayor igualdad de género.",
        "La escasez de agua afecta a más del 40 por ciento de la población mundial, una cifra alarmante que probablemente crecerá con el aumento de las temperaturas globales producto del cambio climático. Aunque 2.100 millones de personas han conseguido acceso a mejores condiciones de agua y saneamiento desde 1990, la decreciente disponibilidad de agua potable de calidad es un problema importante que aqueja a todos los continentes.",
        "Expandir la infraestructura y mejorar la tecnología para contar con energía limpia en todos los países en desarrollo, es un objetivo crucial que puede estimular el crecimiento y a la vez ayudar al medio ambiente.",
        "Los Objetivos de Desarrollo Sostenible apuntan a estimular el crecimiento económico sostenible mediante el aumento de los niveles de productividad y la innovación tecnológica. Fomentar políticas que estimulen el espíritu empresarial y la creación de empleo es crucial para este fin, así como también las medidas eficaces para erradicar el trabajo forzoso, la esclavitud y el tráfico humano. Con estas metas en consideración, el objetivo es lograr empleo pleno y productivo y un trabajo decente para todos los hombres y mujeres para 2030.",
        "La inversión en infraestructura y la innovación son motores fundamentales del crecimiento y el desarrollo económico. Con más de la mitad de la población mundial viviendo en ciudades, el transporte masivo y la energía renovable son cada vez más importantes, así como también el crecimiento de nuevas industrias y de las tecnologías de la información y las comunicaciones.",
        "La desigualad de ingresos es un problema mundial que requiere soluciones globales. Estas incluyen mejorar la regulación y el control de los mercados y las instituciones financieras y fomentar la asistencia para el desarrollo y la inversión extranjera directa para las regiones que más lo necesiten. Otro factor clave para salvar esta distancia es facilitar la migración y la movilidad segura de las personas.",
        "Mejorar la seguridad y la sostenibilidad de las ciudades implica garantizar el acceso a viviendas seguras y asequibles y el mejoramiento de los asentamientos marginales. También incluye realizar inversiones en transporte público, crear áreas públicas verdes y mejorar la planificación y gestión urbana de manera que sea participativa e inclusiva.",
        "El consumo de una gran proporción de la población mundial sigue siendo insuficiente para satisfacer incluso sus necesidades básicas. En este contexto, es importante reducir a la mitad el desperdicio per cápita de alimentos en el mundo a nivel de comercio minorista y consumidores para crear cadenas de producción y suministro más eficientes. Esto puede aportar a la seguridad alimentaria y llevarnos hacia una economía que utilice los recursos de manera más eficiente.",
        "Apoyar a las regiones más vulnerables contriubuirá directamente no solo al Objetivo 13 sino tamién a otros Objetivos de Desarrollo Sostenible. Estas acciones deben ir de la mano con los esfuerzos destinados a integrar las medidas de reducción del riesgo de desastres en las políticas y estrategias nacionales. Con voluntad política y un amplio abanico de medidas tecnológicas, aún es posible limitar el aumento de la temperatura media global a dos grados Celsius por encima de los niveles pre-industriales, apuntando a 1,5°C. Para lograrlo, se requieren acciones colectivas urgentes.",
        "Se deben tomar medidas urgentes para reducir la pérdida de hábitats naturales y biodiversidad que forman parte de nuestro patrimonio común y apoyar la seguridad alimentaria y del agua a nivel mundial, la mitigación y adaptación al cambio climático, y la paz y la seguridad.",
        "Los Objetivos de Desarrollo Sostenible buscan reducir sustancialmente todas las formas de violencia y trabajan con los gobiernos y las comunidades para encontrar soluciones duraderas a los conflictos e inseguridad. El fortalecimiento del Estado de derecho y la promoción de los derechos humanos es fundamental en este proceso, así como la reducción del flujo de armas ilícitas y la consolidación de la participación de los países en desarrollo en las instituciones de gobernabilidad mundial.",
        "La finalidad de los objetivos es mejorar la cooperación Norte-Sur y Sur-Sur, apoyando los planes nacionales en el cumplimiento de todas las metas. Promover el comercio internacional y ayudar a los países en desarrollo para que aumenten sus exportaciones, forma parte del desafío de lograr un sistema de comercio universal equitativo y basado en reglas que sea justo, abierto y beneficie a todos.",
        "Los Objetivos de Desarrollo Sostenible generan un marco para ordenar y proteger de manera sostenible los ecosistemas marinos y costeros de la contaminación terrestre, así como para abordar los impactos de la acidificación de los océanos. Mejorar la conservación y el uso sostenible de los recursos oceánicos a través del derecho internacional también ayudará a mitigar algunos de los retos que enfrentan los océanos."]
    return random.choice(ods_list)


def cita_aleatorio():
    cita_list = ["Al no ser los únicos, decidimos ser los mejores. (Gorka Lomeña)",
                 "Con demasiada frecuencia damos a los estudiantes respuestas para recordar en lugar de problemas para resolver (Roger Lewin)",
                 "Si la depuración es el proceso de eliminar errores, entonces la programación debe ser el proceso de introducirlos. (Edsger Dijkstra)",
                 "Pensar es el trabajo más difícil que existe. Quizá esa sea la razón por la que haya tan pocas personas que lo practiquen. (Henry Ford)",
                 "No es que sea muy inteligente. Es simplemente que estoy más tiempo con los problemas. (Albert Einstein)",
                 "Programar no es un talento; es una habilidad. En tu mano está desarrollarla. (Codecademy)",
                 "No digas: “Es imposible”. Di: “No lo he hecho todavía”. (Proverbio japonés)",
                 "La experiencia demuestra que el éxito de un curso de programación depende críticamente de la elección de los ejemplos que se utilice. (Niklaus Wirth)",
                 "Al ordenador le importa tres leches tu problema, así que el esfuerzo por que éste realice un proceso por el cual se resuelve dicho problema lo tienes que hacer TÚ. Y el esfuerzo consiste en dárselo mascado para que lo lleve a cabo una y otra vez. (Alex Tolón)",
                 "Las raíces del estudio son amargas. Los frutos, dulces. (Cicerón)",
                 "Los malos programadores se preocupan del código. Los buenos se preocupan de las estructuras de datos y de sus relaciones. (Linus Torvalds)",
                 "La práctica te perfecciona. Descubre cuánta práctica necesitas tú. (Alex Tolón)",
                 "Un problema se transforma en desafío cuando le pones fecha de solución. (Anónimo)",
                 "Un problema se transforma en desafío cuando le pones fecha de solución. (Anónimo)"]
    return random.choice(cita_list)


def inicio(update, context):
    # Enviar un mensaje a un ID determinado.
    context.bot.send_message(update.message.chat_id, "Oído cocina. Tú dirás...")
    global inicio_bot
    inicio_bot = True


def ods(update, context):
    # Enviar un mensaje a un ID determinado.
    if inicio_bot == True:
        context.bot.send_message(update.message.chat_id, ods_aleatorio())


def cita(update, context):
    # Enviar un mensaje a un ID determinado.
    global inicio_bot
    if inicio_bot == True:
        context.bot.send_message(update.message.chat_id, cita_aleatorio())


def final(update, context):
    # Enviar un mensaje a un ID determinado.

    global inicio_bot
    if inicio_bot==True:
        context.bot.send_message(update.message.chat_id,
                                 "¡Que pases un buen día!")
        inicio_bot = False


TOKEN = "2119015416:AAEvm_Tf4oNQZaDlGr3JkM4Gt8L7G52yAH8"
updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

inicio_bot = False
updater.start_polling()

dp.add_handler(CommandHandler('inicio', inicio))
dp.add_handler(CommandHandler('ods', ods))
dp.add_handler(CommandHandler('cita', cita))
dp.add_handler(CommandHandler('final', final))
