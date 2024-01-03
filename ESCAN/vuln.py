import subprocess

def guardar_informacion(info):
    try:
        with open("inf.txt", "a") as file:
            file.write(info)
        print("La informació s'ha guardat correctament a 'inf.txt'.")
    except Exception as e:
        print(f"S'ha produït un error en guardar la informació: {e}")

def vuln():
    ip = input("DONA'M LA IP A CERCAR EN FORMAT x.x.x.x →")
    port = input("\nDONA'M UN POR O RANG DE PORTS O '-' EN CAS DE VOLER TOTS:\n")
    vuln = subprocess.run(["nmap", "-sV", "-p", port, "--script", "vuln", ip], capture_output=True, text=True)

    if vuln.returncode == 0:
        nmap_output = vuln.stdout
        print("Resultats de l'escaneig de vulnerabilitats:")
        print(nmap_output)

        guardar = input("Vols guardar la informació en 'inf.txt'? (si/no)\n → ").lower()
        if guardar == 'si':
            guardar_informacion(nmap_output)
    else:
        print("Error al executar l'escaneig de vulnerabilitats.")

# Pots provar la funció vuln cridant-la aquí
# vuln()
