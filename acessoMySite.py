from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inicializa o serviço do ChromeDriver usando o ChromeDriverManager para instalar automaticamente o ChromeDriver apropriado
service = Service(ChromeDriverManager().install())

# Inicializa o driver do Chrome, utilizando o serviço configurado anteriormente
driver = webdriver.Chrome(service=service)

# Abre o navegador e acessa o site do Google Brasil
driver.get('https://google.com.br')

# Localiza o elemento na página usando XPath e envia as teclas "José Leonardo" para o campo de entrada
element = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
element.send_keys("José Leonardo")

# Pressiona a tecla ENTER após digitar "José Leonardo"
element.send_keys(Keys.ENTER)

# Localiza a posição do meu site nos resultados de busca e clica nele
driver.find_element(By.XPATH, '//*[@id="rso"]/div[3]/div/div/div/div[1]/div/div/span/a/h3').click()

# Aguarda 25 segundos antes de continuar a execução do programa
time.sleep(25)

# Localiza no header a opção "Portfólio" e clica nele
driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[2]/a').click()

# Aguarda 30 segundos antes de continuar a execução do programa
time.sleep(30)

# Localiza no header a opção "Contato" e clica nele
driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[4]/a').click()

# Aguarda 14 segundos antes de continuar a execução do programa
time.sleep(14)

# Localiza no header a opção "Blog" e clica nele
driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[3]/a').click()

# Aguarda 32 segundos antes de continuar a execução do programa
time.sleep(32)

# Localiza no card a opção "Otimização de Imagens" e clica nele
driver.find_element(By.XPATH, '/html/body/section/div[2]/div[1]/div').click()

# Aguarda 40 segundos antes de continuar a execução do programa
time.sleep(40)

# Localiza o botão de "Voltar ao Blog" e clica nele
driver.find_element(By.XPATH, '/html/body/section/a/button').click()

# Aguarda 22 segundos antes de continuar a execução do programa
time.sleep(22)

# Localiza no card a opção "Sitemap" e clica nele
driver.find_element(By.XPATH, '/html/body/section/div[2]/div[2]/div').click()

# Aguarda 111 segundos antes de continuar a execução do programa
time.sleep(111)

# Localiza o botão de "Voltar ao Blog" e clica nele
driver.find_element(By.XPATH, '/html/body/section/a/button').click()

# Aguarda 13 segundos antes de continuar a execução do programa
time.sleep(13)

# Localiza no card a opção "Meta tag" e clica nele
driver.find_element(By.XPATH, '/html/body/section/div[2]/div[3]/div').click()

# Aguarda 132 segundos antes de continuar a execução do programa
time.sleep(132)

# Localiza o botão de "Voltar ao Blog" e clica nele
element_to_click = driver.find_element(By.XPATH, '/html/body/section/a/button').click()

# Aguarda 17 segundos antes de continuar a execução do programa
time.sleep(17)

# Localiza no card a opção "React com Vite" e clica nele
driver.find_element(By.XPATH, '/html/body/section/div[2]/div[4]/div').click()

# Aguarda 256 segundos antes de continuar a execução do programa
time.sleep(256)

# Localiza o botão de "Voltar ao Blog" e clica nele
element_to_click = driver.find_element(By.XPATH, '/html/body/section/a/button').click()

# Aguarda 20 segundos antes de continuar a execução do programa
time.sleep(20)

# Localiza no card a opção "Meu nome aparece entre..." e clica nele
driver.find_element(By.XPATH, '/html/body/section/div[2]/div[5]/div').click()

# Aguarda 302 segundos antes de continuar a execução do programa
time.sleep(302)

# Localiza o botão de "Voltar ao Blog" e clica nele
element_to_click = driver.find_element(By.XPATH, '/html/body/section/a/button').click()

# Aguarda 12 segundos antes de continuar a execução do programa
time.sleep(12)

# Localiza no card a opção "Conheça os comandos essenciais..." e clica nele
element_to_click = driver.find_element(By.XPATH, '/html/body/section/div[2]/div[6]/div').click()

# Aguarda 323 segundos antes de continuar a execução do programa
time.sleep(323)

# Localiza o botão de "Voltar ao Blog" e clica nele
driver.find_element(By.XPATH, '/html/body/section/a/button').click()

# Aguarda 28 segundos antes de continuar a execução do programa
time.sleep(28)

# Fecha o navegador
driver.quit()