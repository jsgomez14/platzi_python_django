from datetime import datetime
import pytz

bogota_timezone = pytz.timezone('America/Bogota')
bogota_date = datetime.now(bogota_timezone)

print('Bogota', bogota_date.strftime('%Y-%m-%d %H:%M:%S'))

mexico_timezone = pytz.timezone('America/Mexico_City')
mexico_date = datetime.now(mexico_timezone)

print('Ciudad de Mexico', mexico_date.strftime('%Y-%m-%d %H:%M:%S'))


caracas_timezone = pytz.timezone('America/Caracas')
caracas_date = datetime.now(caracas_timezone)

print('Caracas', caracas_date.strftime('%Y-%m-%d %H:%M:%S'))

baires_timezone = pytz.timezone('America/Buenos_Aires')
baires_date = datetime.now(baires_timezone)

print('Buenos Aires', baires_date.strftime('%Y-%m-%d %H:%M:%S'))