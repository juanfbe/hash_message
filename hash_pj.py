def tit():
    """Muestra en pantalla el titulo de la aplicacion y el autor"""

    print("""  _  _     _     ___   _  _     ___    ___    ___     __  __   ___   ___   ___     _      ___   ___   ___ 
 | || |   /_\   / __| | || |   | __|  / _ \  | _ \   |  \/  | | __| / __| / __|   /_\    / __| | __| / __|
 | __ |  / _ \  \__ \ | __ |   | _|  | (_) | |   /   | |\/| | | _|  \__ \ \__ \  / _ \  | (_ | | _|  \__ \ 
 |_||_| /_/ \_\ |___/ |_||_|   |_|    \___/  |_|_\   |_|  |_| |___| |___/ |___/ /_/ \_\  \___| |___| |___/

 By Juan
                                                                                                          """)

def app():
    tit()
    m = input("Introduce tu mensaje: ")
    print("El hash de tu mensaje es:",hash(m))

app()