# buscar_noticia.py

import requests
from bs4 import BeautifulSoup

equipos = ['Mallorca', 'Newcastle', 'Dortmund', 'Qaraba']

STATE_FILE = "notified_temas.txt"

def leer_notificados():
    try:
        with open(STATE_FILE, 'r') as f:
            # Usamos un set para búsquedas más eficientes
            return set(line.strip() for line in f)
    except FileNotFoundError:
        # Si el archivo no existe, es la primera vez que se ejecuta
        return set()
        

def encontrar(notificados):
    url = "https://www.athletic-club.eus/noticias/club/1"
    equipos_encontrados_en_web = set()
    try:
        response = requests.get(url)
        response.raise_for_status() # Lanza un error si la petición falla
        soup = BeautifulSoup(response.text, 'html.parser')
        main_div = soup.find('div', class_='list-posts__group')
        
        if main_div:
            noticias = main_div.find_all('a')
            for noticia in noticias:
                texto_h3 = noticia.find('h3')
                if texto_h3:
                    texto = texto_h3.get_text()
                    for equipo in equipos:
                        if equipo in texto:
                            if equipo == "Qaraba":
                                equipos_encontrados_en_web.add("Qarabag")
                            else:
                               equipos_encontrados_en_web.add(equipo)
        nuevos = equipos_encontrados_en_web - notificados
        return list(nuevos), list(equipos_encontrados_en_web)
    except requests.RequestException as e:
        print(f"Error al acceder a la web: {e}")
        return False

def actualizar(todos):
    """Sobrescribe el archivo de estado con la lista actual de equipos en la web."""
    with open(STATE_FILE, 'w') as f:
        for equipo in sorted(todos):
            f.write(equipo + '\n')

if __name__ == "__main__":
    notificados_previamente = leer_notificados()
    nuevos, todos = encontrar(notificados_previamente)
    if nuevos:
        # Imprimimos solo los nuevos para que el workflow los envíe
        print(", ".join(nuevos_partidos))
        # Actualizamos nuestro archivo de "memoria" con todos los que hay ahora
        actualizar_notificados(todos_los_partidos)
