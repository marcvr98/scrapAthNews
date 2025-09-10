import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://www.athletic-club.eus/noticias/club/1"

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

main_div = soup.find('div', class_='list-posts__group')

if not main_div:
    print("No se encontró el div principal.")
else:
    noticias = main_div.find_all('a')
    if not noticias:
        print("No se encontraron noticias.")
    else:
        for noticia in noticias:
            texto = noticia.find('h3')
            if texto:
                if 'Newcastle' in texto.get_text():
                    print(texto.get_text(strip=True))
