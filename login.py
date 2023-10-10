from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from selenium import webdriver
from undetected_chromedriver import Chrome

driver = Chrome(headless=True, use_subprocess=False)
driver.get('https://nowsecure.nl')
driver.save_screenshot('nowsecure.png')

# Espera implícita por até 5 segundos para os elementos estarem disponíveis
driver.implicitly_wait(5)

try:
    print('Enter the gmailid and password')
    gmailId, passWord = map(str, input().split())

    driver.get(r'https://accounts.google.com/signin/v2/identifier?continue=' +
               'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1' +
               '&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

    loginBox = driver.find_element(By.XPATH, '//*[@id ="identifierId"]')
    loginBox.send_keys(gmailId)

    nextButton = driver.find_element(By.XPATH, '//*[@id ="identifierNext"]')
    nextButton.click()

    passWordBox = WebDriverWait(driver, 5).until(
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
    driver.quit()
