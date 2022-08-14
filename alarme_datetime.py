import datetime
import time

def esta_na_hora(hora, minuto, hora_atual):
  if hora_atual.hour == hora and hora_atual.minute == minuto:
    return True
  return False


while True:
    hora = 21
    minuto = 55
    now = datetime.datetime.now()
    print("alarme: "+ str(hora), str(minuto))
    print(now)



    if esta_na_hora(hora, minuto, now):
        print("ACORDAR")

    time.sleep(5)

