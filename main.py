import requests
from bs4 import BeautifulSoup
import pandas as pd

def encontrada():
    url = "https://www.athletic-club.eus/noticias/club/1"
    
    response = requests.get(url)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    main_div = soup.find('div', class_='list-posts__group')
    
    if not main_div:
        return False
    else:
        noticias = main_div.find_all('a')
        if not noticias:
            return False
        else:
            for noticia in noticias:
                texto = noticia.find('h3')
                if texto:
                    if 'Newcastle' in texto.get_text():
                        return True
            return False
