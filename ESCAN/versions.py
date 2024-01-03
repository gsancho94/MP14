import subprocess

def guardar_informacion(info):
    try:
        with open("inf.txt", "a") as file:
            file.write(info)
        print("La informació s'ha guardat correctament a 'inf.txt'.")
    except Exception as e:
        print(f"S'ha produït un error en guardar la informació: {e}")

def versions():
    ip = input("\nDONA'M LA IP A CERCAR EN FORMAT x.x.x.x\n →")
    port = input("\nDONA'M UN POR O RANG DE PORTS O '-' EN CAS DE VOLER TOTS:\n")
    versions = subprocess.run(["nmap", "-sV", "-p", port, ip], capture_output=True, text=True)

    if versions.returncode == 0:
        nmap_output = versions.stdout
        print("Resultats de l'escaneig de versions:")
        print(nmap_output)

        guardar = input("Vols guardar la informació en 'inf.txt'? (si/no)\n → ").lower()
        if guardar == 'si':
            guardar_informacion(nmap_output)
    else:
        print("Error al executar l'escaneig de versions.")

# Pots provar la funció versions cridant-la aquí
# versions()
