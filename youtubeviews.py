from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inicializa o serviço do ChromeDriver usando o ChromeDriverManager para instalar automaticamente o ChromeDriver apropriado
service = Service(ChromeDriverManager().install())

# Inicializa o driver do Chrome, utilizando o serviço configurado anteriormente
driver = webdriver.Chrome()

# Abre o navegador e acessa o site do Google Brasil
driver.get('https://youtu.be/RfuYL-9Nqhs')

# Localiza a posição do meu site nos resultados de busca e clica nele
driver.find_element(By.XPATH, '//*[@id="movie_player"]/div[30]/div[2]/div[1]/button').click()

# Aguarda 25 segundos antes de continuar a execução do programa
time.sleep(218)

# Fecha o navegador
driver.quit()