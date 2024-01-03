from shodan import Shodan

# Setup the Shodan API object
api = Shodan('iMiL2gPRQrMDCg3qWREgaPWE7BjNwB3g')

# Submit a scan request for 1 IP and 1 network range
print("TRIA EL TIPUS D'ESCANEIG QUE VOLS FER:")
print("[1] : ESCANEIG DE HOSTS D'UNA XARXA")
print("[2] : ESCANEIG DE PORTS OBERTS")
print("[3] : ESCANEIG DE VERSIONS DE PORT/S")
print("[4] : ESCANEIG DE VULNERABILITATS DE SERVEI/S")
print("[5] : SORTIR")
scan = api.scan(['8.8.8.8'])
print(scan)
