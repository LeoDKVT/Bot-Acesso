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

# Aguarda 18 segundos antes de continuar a execução do programa
time.sleep(4)

# # Localiza no header a opção "Portfólio"
element_to_click = driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[2]/a')

# Clique no "Portfólio"
element_to_click.click()

# Aguarda 20 segundos antes de continuar a execução do programa
time.sleep(4)

# Localiza no header a opção "Contato"
element_to_click = driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[4]/a')

# Clique no "Contato"
element_to_click.click()

# Aguarda 20 segundos antes de continuar a execução do programa
time.sleep(4)

# Localiza no header a opção "Blog"
element_to_click = driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[3]/a')

# Clique no "Blog"
element_to_click.click()

# Aguarda 20 segundos antes de continuar a execução do programa
time.sleep(10)


element_to_click = driver.find_element(By.XPATH, '/html/body/section/div[2]/div[1]/div')

element_to_click.click()

time.sleep(10)


element_to_click = driver.find_element(By.XPATH, '/html/body/section/a/button')

element_to_click.click()

time.sleep(10)





element_to_click = driver.find_element(By.XPATH, '/html/body/section/div[2]/div[2]/div')

element_to_click.click()

time.sleep(10)

element_to_click = driver.find_element(By.XPATH, '/html/body/section/a/button')

element_to_click.click()

time.sleep(10)






element_to_click = driver.find_element(By.XPATH, '/html/body/section/div[2]/div[3]/div')

element_to_click.click()

time.sleep(10)

element_to_click = driver.find_element(By.XPATH, '/html/body/section/a/button')

element_to_click.click()

time.sleep(10)






element_to_click = driver.find_element(By.XPATH, '/html/body/section/div[2]/div[4]/div')

element_to_click.click()

time.sleep(210)

element_to_click = driver.find_element(By.XPATH, '/html/body/section/a/button')

element_to_click.click()

time.sleep(10)







element_to_click = driver.find_element(By.XPATH, '/html/body/section/div[2]/div[5]/div')

element_to_click.click()

time.sleep(10)

element_to_click = driver.find_element(By.XPATH, '/html/body/section/a/button')

element_to_click.click()

time.sleep(10)





element_to_click = driver.find_element(By.XPATH, '/html/body/section/div[2]/div[6]/div')

element_to_click.click()

time.sleep(10)

element_to_click = driver.find_element(By.XPATH, '/html/body/section/a/button')

element_to_click.click()

time.sleep(10)







# Fecha o navegador
driver.quit()