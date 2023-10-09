from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inicializa o serviço do ChromeDriver usando o ChromeDriverManager para instalar automaticamente o ChromeDriver apropriado.
service = Service(ChromeDriverManager().install())

# Inicializa o driver do Chrome, utilizando o serviço configurado anteriormente.
driver = webdriver.Chrome(service=service)

# Abre o navegador e acessa o site do Google Brasil
driver.get('https://google.com.br')

# Localiza o elemento na página usando XPath e envia as teclas "José Leonardo" para o campo de entrada
element = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
element.send_keys("José Leonardo")

# Pressiona a tecla ENTER após o envio das teclas
element.send_keys(Keys.ENTER)

# Localiza o elemento que é o meu site
element_to_click = driver.find_element(By.XPATH, '//*[@id="rso"]/div[3]/div/div/div/div[1]/div/div/span/a/h3')

# Clique no elemento no caso o meu site
element_to_click.click()

# Aguarda 40 segundos antes de continuar a execução do programa
time.sleep(40)

# Fecha o navegador
driver.quit()