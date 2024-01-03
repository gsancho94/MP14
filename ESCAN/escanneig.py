import os
import subprocess
import requests
import requests

def enviarTelegram():
    token = '6883275342:AAFoGQOEfX6EnpQjxbMlCKnLC0EuYGaeXDk'
    id_grupo = -4094599436
    ruta = "/home/alumne/Escriptori/MP14/inf.txt"

    mensaje = "Hola, soy un bot y estoy mandando un mensaje a Telegram usando Python"

    # Enviar mensaje
    response_mensaje = requests.post('https://api.telegram.org/bot' + token + '/sendMessage',
                  data={'chat_id': id_grupo, 'text': mensaje, 'parse_mode': 'HTML'})

    # Enviar documento
    response_documento = requests.post('https://api.telegram.org/bot' + token + '/sendDocument',
                  files={'document': (ruta, open(ruta, 'rb'))},
                  data={'chat_id': id_grupo, 'caption': 'imagen caption'})

    # Verificar si los envíos fueron exitosos (código 200 indica éxito)
    if response_mensaje.status_code == 200 and response_documento.status_code == 200:
        return True
    else:
        return False

while True:
    port = "-"

    print("\nTRIA EL TIPUS D'ESCANEIG QUE VOLS FER:")
    print("[1] : ESCANEIG DE HOSTS D'UNA XARXA")
    print("[2] : ESCANEIG DE PORTS OBERTS")
    print("[3] : ESCANEIG DE VERSIONS DE PORT/S")
    print("[4] : ESCANEIG DE VULNERABILITATS DE SERVEI/S")
    print("[5] : ESCANEIG DE SEGURETAT SSH")
    print("[6] : ESCANEIG DE ENUM4LINUX")
    print("[7] : ENVIAR RESULTAT AL TELEGRAM")
    print("[8] : SORTIR")

    piv = input("\nPosa un nombre entre 1 - 6\n → ")

    if piv == '1':
        from xarxa import xarxa
        xarxa()
    elif piv == '2':
        from ports import ports
        ports()
    elif piv == '3':
        from versions import versions
        versions()
    elif piv == '4':
        from vuln import vuln
        vuln()
    elif piv == '5':
        from sshaudit import sshaudit
        sshaudit()
    elif piv == '6':
        from enum4linux import enum4linux_tool
        enum4linux_tool()
    elif piv == '7':
       enviarTelegram()
    elif piv == '8':
        break  # Sortir del bucle
    else:
        print("ERROR")
    
    # Preguntar si vol fer algo més o sortir
        
    if piv != '8':
        continuar = input("Vols fer una altra funció? (si/no) \n → ").lower()
        if continuar != 'si':
            break


