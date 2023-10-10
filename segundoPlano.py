from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inicializa o serviço do ChromeDriver usando o ChromeDriverManager para instalar automaticamente o ChromeDriver apropriado
service = Service(ChromeDriverManager().install())

# SEGUNDO PLANO
# Comandos para funcionar em segundo plano
segPlano = webdriver.ChromeOptions()
segPlano.add_argument('--headless=new')

# SEGUNDO PLANO adicionado ( , options=segPlano )
# Inicializa o driver do Chrome, utilizando o serviço configurado anteriormente 
driver = webdriver.Chrome(service=service, options=segPlano)