import subprocess

def enum4linux_tool():
    def print_enum4linux():
        # Imprime las opciones disponibles para enum4linux
        help_text = """
        Options are (like "enum"):
            -U        get userlist
            -M        get machine list*
            -S        get sharelist
            -P        get password policy information
            -G        get group and member list
            -d        be detailed, applies to -U and -S
            -u user   specify username to use (default "")  
            -p pass   specify password to use (default "")   

        The following options from enum.exe aren't implemented: -L, -N, -D, -f

        Additional options:
            -a        Do all simple enumeration (-U -S -G -P -r -o -n -i).
                      This option is enabled if you don't provide any other options.
            -h        Display this help message and exit
            -r        enumerate users via RID cycling
            -R range  RID ranges to enumerate (default: 500-550,1000-1050, implies -r)
            -K n      Keep searching RIDs until n consective RIDs don't correspond to
                      a username.  Impies RID range ends at 999999. Useful 
                      against DCs.
            -l        Get some (limited) info via LDAP 389/TCP (for DCs only)
            -s file   brute force guessing for share names
            -k user   User(s) that exists on remote system (default: administrator,guest,krbtgt,domain admins,root,bin,none)
                      Used to get sid with "lookupsid known_username"
                      Use commas to try several users: "-k admin,user1,user2"
            -o        Get OS information
            -i        Get printer information
            -w wrkg   Specify workgroup manually (usually found automatically)
            -n        Do an nmblookup (similar to nbtstat)
            -v        Verbose.  Shows full commands being run (net, rpcclient, etc.)
            -A        Aggressive. Do write checks on shares etc
        """

        print(help_text)

    def run_enum4linux(ip, options):
        # Ejecuta enum4linux con las opciones proporcionadas
        command = ["enum4linux"] + options + [ip]
        subprocess.run(command)

    print_enum4linux()  # Muestra la ayuda de enum4linux
    ip_address = input("Ingresa una dirección IP: ")
    user_options = input("Ingresa las opciones (separadas por espacio, ej. -U -o): ").split()
    run_enum4linux(ip_address, user_options)

# Ejecutar la función enum4linux_tool
enum4linux_tool()
















'''import subprocess

def enum4linux_tool():
    def print_enum4linux():
        # Imprime las opciones disponibles para enum4linux
        # (El mismo contenido de ayuda que ya tenías)
        help_text = """
        Options are (like "enum"):
            -U        get userlist
            ...
            -v        Verbose.  Shows full commands being run (net, rpcclient, etc.)
            -A        Aggressive. Do write checks on shares etc
        """

        print(help_text)

    def run_enum4linux(ip, options):
        # Ejecuta enum4linux con las opciones proporcionadas
        command = ["enum4linux"] + options + [ip]
        result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode == 0:
            # Si la ejecución fue exitosa, guardar la salida en el archivo inf.txt
            output = result.stdout
            try:
                with open("inf.txt", "a") as file:
                    file.write(f"enum4linux output for {ip}:\n\n")
                    file.write(output)
                print("La información de enum4linux se ha guardado correctamente en 'inf.txt'.")
            except Exception as e:
                print(f"Se ha producido un error al guardar la información: {e}")
        else:
            print("Error al ejecutar enum4linux.")

    print_enum4linux()  # Muestra la ayuda de enum4linux
    ip_address = input("Ingresa una dirección IP: ")
    user_options = input("Ingresa las opciones (separadas por espacio, ej. -U -o): ").split()
    run_enum4linux(ip_address, user_options)

# Ejecutar la función enum4linux_tool
enum4linux_tool()
'''