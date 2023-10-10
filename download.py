from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# Inicializa o serviço do ChromeDriver usando o ChromeDriverManager para instalar automaticamente o ChromeDriver apropriado
service = Service(ChromeDriverManager().install())

#segPlano = webdriver.ChromeOptions()
#segPlano.add_argument('--headless=new')

# Inicializa o driver do Chrome, utilizando o serviço configurado anteriormente
driver = webdriver.Chrome(service=service)
#options=segPlano
# Abre o navegador e acessa o site do Google Brasil
driver.get('https://google.com.br')

time.sleep(10)


# Localiza o elemento na página usando XPath e envia as teclas "José Leonardo" para o campo de entrada
element = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
element.send_keys("José Leonardo")

# Pressiona a tecla ENTER após digitar "José Leonardo"
element.send_keys(Keys.ENTER)

# Localiza a posição do meu site nos resultados de busca e clica nele
driver.find_element(By.XPATH, '//*[@id="rso"]/div[3]/div/div/div/div[1]/div/div/span/a/h3').click()






# Localiza a posição do meu site nos resultados de busca e clica nele
driver.find_element(By.XPATH, '/html/body/section/div/p[7]/a/strong').click()

# Aguarda 25 segundos antes de continuar a execução do programa
time.sleep(30)



driver.find_element(By.XPATH, '//*[@class="VfPpkd-vQzf8d"]').click()


time.sleep(30)


# //*[@id="identifierId"]


# //*[@id="identifierId"]

# //*[@id="identifierNext"]/div/button/span




# Fecha o navegador
driver.quit()


