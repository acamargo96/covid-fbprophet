from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from shutil import move
import glob
from time import sleep

def download_file():

    dl_path = get_download_path()

    # faz download do arquivo .xlsx dos dados do min. da saude
    driver = webdriver.Chrome()
    driver.get('https://covid.saude.gov.br/')
    btn = driver.find_elements_by_xpath('/html/body/app-root/ion-app/ion-router-outlet/app-home/ion-content/div[1]/div[2]/ion-button')[0]
    btn.click()
    
    while True:
        # não é robusto, falta verificar a data do arquivo
        file_name = glob.glob(os.path.join(dl_path, 'HIST_PAINEL_COVIDBR*.xlsx'))
        partial_file_name = glob.glob(os.path.join(dl_path, 'HIST_PAINEL_COVIDBR*.xlsx.part'))
        print(file_name)
        print(partial_file_name)

        if len(partial_file_name) != 0:
            sleep(10)
        elif len(file_name) != 0:
            break
        else:
            sleep(10)

    driver.quit()

def copy_from_downloads(destination):
    
    dl_path = get_download_path()
    files = os.listdir(dl_path)
    # lista os arquivos vindos do site do min. da saude
    file_paths = [os.path.join(dl_path, f) for f in files if 'HIST_PAINEL_COVIDBR' in f]
    
    most_recent_file = max(file_paths, key=os.path.getctime)
    new_file_path = os.path.join(dl_path, 'raw.xlsx')
    
    os.rename(most_recent_file, new_file_path)

    move(new_file_path, destination)

    
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

download_file()