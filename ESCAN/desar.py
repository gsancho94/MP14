import os
import subprocess

def desarinfo():
    try:
        with open("escann.txt", "w") as file:
           desar =  file.write()
        print("La informació s'ha guardat correctament a 'escann.txt'.")
    except Exception as e:
        print(f"S'ha produït un error en guardar la informació: {e}")
    return desar 
