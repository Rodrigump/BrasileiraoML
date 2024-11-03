#Modelo de Machine Learning de previsão de classificação do Campeonato Brasileiro de Futebols
#Autor: Rodrigo Rossi dos Santos

from bs4 import BeautifulSoup
import pandas as pd
import requests
import time

#Download do histórico de classificações rodada a rodada do Campeonato Brasileiro
def download_data_from_source(ano, train_or_test, inicio=1, fim=38):

    print(ano)

    data = []

    for rodada in range(inicio, fim+1):

        print(rodada)

        responsive_table = None

        while(responsive_table is None):

            url = f'https://www.transfermarkt.com.br/campeonato-brasileiro-serie-a/formtabelle/wettbewerb/GB1?saison_id={ano}&min={1}&max={rodada}'

            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}

            req = requests.get(url, headers=headers)

            #time.sleep(1)

            soup = BeautifulSoup(req.text, 'html.parser')

            responsive_table = soup.find('div', class_='responsive-table')

        rows = responsive_table.find_all('tr')

        for r in rows[1:]:
            split_row = r.text.split('\n')
            format_row = [i.replace('\xa0', '').strip() for i in split_row if i.replace('\xa0', '').strip() != '']
            data_row = format_row[:9]
            data_row.append(ano)
            data_row.append(rodada)
            data.append(data_row)

    columns = ['Posicao', 'Clube', 'J', 'V', 'E', 'D', 'Gols', 'SG', 'Pts', 'Ano', 'Rodada']

    df = pd.DataFrame(data, columns=columns)

    output_filename = f"./{train_or_test}/EPL_{ano}.csv"

    df.to_csv(output_filename, index=False)

if __name__ == '__main__':

    download_data_from_source(2024, 'test')