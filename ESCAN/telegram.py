import requests

def t():
    token = '6883275342:AAFoGQOEfX6EnpQjxbMlCKnLC0EuYGaeXDk'
    id_grupo = -4094599436
    ruta = "/home/alumne/Escriptori/MP14/inf.txt"

    mensaje = "Hola, soy un bot y estoy mandando un mensaje a Telegram usando Python"


    requests.post('https://api.telegram.org/bot' + token + '/sendMessage',
                  data={'chat_id': id_grupo, 'text': mensaje, 'parse_mode': 'HTML'})


    requests.post('https://api.telegram.org/bot' + token + '/sendDocument',
                  files={'document': (ruta, open(ruta, 'rb'))},
                  data={'chat_id': id_grupo, 'caption': 'imagen caption'})

    t()

