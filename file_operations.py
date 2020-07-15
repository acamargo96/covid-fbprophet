from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests

import os
from shutil import move, copyfileobj
import glob
import gzip
import csv

from time import sleep
from datetime import datetime as dt

def download_file_min_saude():

    dl_path = get_download_path()

    # faz download do arquivo .xlsx dos dados do min. da saude
    driver = webdriver.Chrome()
    driver.get('https://covid.saude.gov.br/')
    
    sleep(1)

    btn = driver.find_elements_by_xpath('/html/body/app-root/ion-app/ion-router-outlet/app-home/ion-content/div[1]/div[2]/ion-button')[0]
    btn.click()
    
    start_time = dt.now().timestamp()
    not_found = True

    while not_found:

        file_names = glob.glob(os.path.join(dl_path, '*PAINEL_COVIDBR*.xlsx'))
        partial_file_names = glob.glob(os.path.join(dl_path, '*PAINEL_COVIDBR*.xlsx.part'))

        if len(partial_file_names) != 0:
            sleep(10)
        elif len(file_names) != 0:
            for f in file_names:
                # Se o arquivo foi criado depois da execução da função, sai do while
                if os.path.getctime(f) > start_time: not_found = False 
        else:
            sleep(10)

    driver.quit()

# -------------------------------------------------------------------------

def download_file_brasil_io():

    # Baixa o .rar
    url = 'https://data.brasil.io/dataset/covid19/caso_full.csv.gz'
    r = requests.get(url, allow_redirects=True)
    open('data.csv.gz', 'wb').write(r.content)

# -------------------------------------------------------------------------
def move_xlsx_to(destination):
    
    dl_path = get_download_path()
    files = os.listdir(dl_path)
    # lista os arquivos vindos do site do min. da saude
    file_paths = [os.path.join(dl_path, f) for f in files if 'PAINEL_COVIDBR' in f]
    
    most_recent_file = max(file_paths, key=os.path.getctime)
    
    # renomeia o arquivo do min. da saude
    new_file_path = os.path.join(dl_path, 'raw.xlsx')
    os.rename(most_recent_file, new_file_path)

    # remove o raw.xlsx da pasta do script
    os.remove(os.path.join(destination, 'raw.xlsx'))

    move(new_file_path, destination)

# -------------------------------------------------------------------------
    
def get_download_path():
    """
    Fonte :https://stackoverflow.com/questions/35851281/python-finding-the-users-downloads-folder
    Retorna o caminho padrão da pasta "Downloads" no windows ou linux """

    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')