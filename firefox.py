from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

try:
    print('Enter the gmailid and password')
    gmailId, passWord = map(str, input().split())

    # Inicialize o driver do Firefox usando o GeckoDriverManager para instalar automaticamente o geckodriver apropriado
    driver = webdriver.Firefox()
    driver.get(r'https://accounts.google.com/signin/v2/identifier?continue=' +
               'https%3A%2F%2Fmail.google.com/mail%2F&service=mail&sacu=1&rip=1' +
               '&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

    # Espera implícita por até 15 segundos para os elementos estarem disponíveis
    driver.implicitly_wait(15)

    loginBox = driver.find_element(By.XPATH, '//*[@id ="identifierId"]')
    loginBox.send_keys(gmailId)

    nextButton = driver.find_element(By.XPATH, '//*[@id ="identifierNext"]')
    nextButton.click()

    passWordBox = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id ="password"]/div[1]/div/div[1]/input')))
    passWordBox.send_keys(passWord)

    nextButton = driver.find_element(By.XPATH, '//*[@id ="passwordNext"]')
    nextButton.click()

    print('Login Successful...!!')
except NoSuchElementException:
    print('Elemento não encontrado. Verifique os XPaths.')
except TimeoutException:
    print('Tempo de espera excedido. Verifique a disponibilidade dos elementos.')
except Exception as e:
    print(f'Ocorreu um erro: {str(e)}')
finally:
    if 'driver' in locals():
        driver.quit()
