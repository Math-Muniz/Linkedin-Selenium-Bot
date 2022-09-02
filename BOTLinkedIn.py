### Import

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

### KEYS

email = ''
password = ''
search = 'cientista de dados'

### CODE

#Conectando ao Chrome, maximizando a tela e se conectando ao url desejada.

driver=webdriver.Chrome()
driver.maximize_window()
url = 'https://www.linkedin.com/'
driver.get(url)
wait = WebDriverWait(driver, 10)

# Consultando o Campo de email e preenchendo o campo com a váriavel email.

email_field = '//*[@id="session_key"]'
email_field = driver.find_element(By.XPATH, email_field)
email_field.send_keys(email)

# Consultando o Campo de senha e preenchendo o campo com a váriavel senha.

password_field = '//*[@id="session_password"]'
password_field = driver.find_element(By.XPATH, password_field)
password_field.send_keys(password)

# Consultando o botão de Entrar e clicando nele para efetuar o Login, coloquei um sleep (pause) de 3 segundos para a pagina poder carregar os botões

login_button = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form/button')
login_button.click()
time.sleep(5)

# Clica no botão search e digita 'Cientista de Dados' que seria a key registrada.

search_button = driver.find_element(By.XPATH, '//*[@id="global-nav-typeahead"]/input')
search_button.send_keys(search)
time.sleep(2)
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="global-nav-typeahead"]/input'))).send_keys(Keys.ENTER)
time.sleep(5)

# Clica no botão vagas na barra de filtro superior da pagina em que já procuramos sobre Cientista de Dados

jobs = driver.find_element(By.XPATH, '//*[@id="search-reusables__filters-bar"]/ul/li[1]/button')
time.sleep(3)
jobs.click()
time.sleep(2)

# Localiza aonde tem a lista das vagas para podermos extrair os dados da descrição e depois temos a criação de uma description_list para gravarmos os dados.

result_list = driver.find_element(By.XPATH, '//*[@id="main"]/div/section[1]/div')
results = result_list.find_elements(By.CLASS_NAME, 'job-card-container')
description_list=[]


# Looping para clicar nas vagas e salvar as descriçoes dela

for r in results:
    r.click()
    time.sleep(3)
    description = driver.find_element(By.CLASS_NAME, 'jobs-description')
    description_list.append(description.text)

# Aqui ele abre um arquivo .txt e escreve as descrições da vaga depois fecha e salva.    
    
print(description_list)
description_save = '\n'.join(description_list)
with open('descricoes_vagas.txt', 'w', encoding='utf-8') as f:
    f.write(description_save)
    f.close
driver.quit()
