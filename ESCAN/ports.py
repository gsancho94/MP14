import subprocess
import os 

def guardar_informacion(info):
    try:
        with open("inf.txt", "a") as file:
            file.write(info)
        print("La informació s'ha guardat correctament a 'inf.txt'.")
    except Exception as e:
        print(f"S'ha produït un error en guardar la informació: {e}")

def ports():
    ip = input("\nDONA'M LA IP A CERCAR EN FORMAT x.x.x.x\n →")
    ports = subprocess.run(["nmap", "-p-", ip], capture_output=True, text=True)

    if ports.returncode == 0:
        nmap_output = ports.stdout
        print("Resultats de l'escaneig de ports:")
        print(nmap_output)

        guardar = input("Vols guardar la informació en 'inf.txt'? (si/no)\n → ").lower()
        if guardar == 'si':
            guardar_informacion(nmap_output)
    else:
        print("Error al executar l'escaneig de ports.")

# Aquí pots cridar la funció ports per provar el funcionament
# ports()
