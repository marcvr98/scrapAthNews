# buscar_noticia.py

import requests
from bs4 import BeautifulSoup
# Aunque importas pandas, no lo usas en esta función. Lo dejaremos por si lo usas en el futuro.
import pandas as pd 

def encontrada():
    url = "https://www.athletic-club.eus/noticias/club/1"
    try:
        response = requests.get(url)
        response.raise_for_status() # Lanza un error si la petición falla
        soup = BeautifulSoup(response.text, 'html.parser')
        main_div = soup.find('div', class_='list-posts__group')
        
        if main_div:
            noticias = main_div.find_all('a')
            for noticia in noticias:
                texto_h3 = noticia.find('h3')
                if texto_h3 and 'Newcastle' in texto_h3.get_text():
                    return True # Se encontró la palabra
        return False # No se encontró la palabra después de buscar en todo
    except requests.RequestException as e:
        print(f"Error al acceder a la web: {e}")
        return False

if __name__ == "__main__":
    # Si la función devuelve True, imprimimos "true" en la consola.
    # Esto es lo que leerá GitHub Actions.
    if encontrada():
        print("true")
