import os
import time
import datetime

while True:
    fecha_completa_actual = datetime.datetime.now()
    print('Fecha y hora actual:')
    print(fecha_completa_actual.strftime("%Y/%m/%d, %H:%M:%S"))
    time.sleep(1)
    os.system('clear')