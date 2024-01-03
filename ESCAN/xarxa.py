'''import subprocess
import re

def guardar_informacio_fitxer(informacio):
    try:
        with open("inf.txt", "a") as file:
            file.write(informacio)
        print("La informació s'ha guardat correctament a 'inf.txt'.")
    except Exception as e:
        print(f"S'ha produït un error en guardar la informació: {e}")

def xarxa():
    xarxa_input = input("\nDONA'M LA XARXA EN FORMAT x.x.x.x/MSK\n →")
    result = subprocess.run(["nmap", "-sP", xarxa_input], capture_output=True, text=True)

    if result.returncode == 0:
        nmap_output = result.stdout
        ip_addresses = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', nmap_output)

        informacio_a_guardar = "\n".join(ip_addresses)
        for ip in ip_addresses:
            print(ip)
        
        guardar = input("Vols guardar la informació en 'inf.txt'? (si/no)\n → ").lower()
        if guardar == 'si':
            guardar_informacio_fitxer(informacio_a_guardar)
    else:
        print("Error al executar Nmap.")

xarxa()'''

import subprocess
import re

def guardar_informacio_fitxer(informacio):
    try:
        with open("inf.txt", "a") as file:
            file.write(informacio)
        print("La informació s'ha guardat correctament a 'inf.txt'.")
    except Exception as e:
        print(f"S'ha produït un error en guardar la informació: {e}")

def xarxa():
    xarxa_input = input("\nDONA'M LA XARXA EN FORMAT x.x.x.x/MSK\n →")
    result = subprocess.run(["nmap", "-sP", xarxa_input], capture_output=True, text=True)

    if result.returncode == 0:
        nmap_output = result.stdout
        ip_addresses = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', nmap_output)

        informacio_a_guardar = "\n".join(ip_addresses)
        for ip in ip_addresses:
            print(ip)
        
        guardar = input("Vols guardar la informació en 'inf.txt'? (si/no)\n → ").lower()
        if guardar == 'si':
            guardar_informacio_fitxer(informacio_a_guardar)
    else:
        print("Error al executar Nmap.")

if __name__ == "__main__":
    xarxa() # Esto se ejecutará solo si se ejecuta xarxa.py directamente, no si se importa desde otro script.
