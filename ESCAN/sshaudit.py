import subprocess

def guardar_informacion(info):
    try:
        with open("inf.txt", "a") as file:
            file.write(info)
        print("La informació s'ha guardat correctament a 'inf.txt'.")
    except Exception as e:
        print(f"S'ha produït un error en guardar la informació: {e}")

def sshaudit():
    ip = input("A quin host vols auditar? Format = 192.xxx.xxx.xxx\n → ")
    res = subprocess.run(["/home/alumne/Escriptori/MP14/ESCAN/ssh-audit-master/ssh-audit.py", ip], capture_output=True, text=True)

    if res.returncode == 0:
        output = res.stdout
        print("Resultats de l'auditoria SSH:")
        print(output)

        guardar = input("Vols guardar la informació en 'inf.txt'? (si/no)\n → ").lower()
        if guardar == 'si':
            guardar_informacion(output)
    else:
        print("Error al executar l'auditoria SSH.")

# Pots provar la funció sshaudit cridant-la aquí
# sshaudit()
