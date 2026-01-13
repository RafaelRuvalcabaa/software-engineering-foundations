# Trabajando con fechas y horas en Python

from datetime import datetime, timedelta 


#-------------------------------
# 1. Obtener la fecha y hora actual
now = datetime.now()  # Fecha y hora actual
print(f"Fecha y hora actual: {now}")


# 2.- Crear una fecha específica

specific_date = datetime(2025,12,1,5,30,14)

print(f"Fecha específica: {specific_date}")

# 3.- Formatear fechas
# Metodo strftime para formatear fechas a cadenas
# Pasarle el objeto datetime y el formado especificado. 
import locale
locale.setlocale(locale.
LC_TIME, 'es_ES.UTF-8')
#Locale sirve para configurar la "localización" de la fecha y hora. 
# Configurar para español (España)
formatted_date = now.strftime("%A %B %Y %H:%M:%S")
# Se usa / para separar dia pero puede ser cualquier otro caracter.
# Se usan %d para el dia, %m para el mes, %Y para el año, %H para la hora en formato 24 horas, %M para los minutos y %S para los segundos.
#Si pones la "Y" en mayuscula te da el año con 4 digitos, si es minuscula solo 2 digitos.

print(f"Fecha formateada: {formatted_date}")

# 4.- Operaciones con fechas 

yesterday = datetime.now() - timedelta(days=1)
print(f"Fecha de ayer: {yesterday}")

tomorrow = datetime.now() + timedelta(days=1)
print(f"Fecha de mañana: {tomorrow}")

one_hour_after = datetime.now() + timedelta(hours=1)

print(f"Fecha y hora de mañana con una hora más: {one_hour_after}")

# Solo motrar la el dia y no la hora.

just_date = now.date()
print(f"Sólo la fecha: {just_date}")


# 5. Obtener componentes individuales de una fecha

year = now.year
month = now.month
day = now.day   
print(f"Año: {year}, Mes: {month}, Día: {day}")

# Calcular la diferencia entre dos fechas

first_date = datetime(2020,9,1)
second_date = datetime(2024,12,1)

difference = second_date - first_date
print(f"Diferencia entre fechas: {difference.days} días")

#-------------------------------
date1 = datetime.now()
date2 = datetime(2024,1,1)
diff = date2 - date1 
print(f"Dias entre las fechas: {diff}")

#-------------------------------

print(f"Minutos: {diff.total_seconds() / 60}")