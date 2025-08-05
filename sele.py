from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Caminho para o ChromeDriver
driver_path = 'CAMINHO/DO/SEU/CHROMEDRIVER'

# Inicializa o navegador
driver = webdriver.Chrome(executable_path=driver_path)

# Acessa o Google
driver.get("https://www.google.com")

# Localiza a barra de pesquisa e envia seu nome
search_box = driver.find_element("name", "q")
search_box.send_keys("Seu Nome")
search_box.send_keys(Keys.RETURN)

# Acessa o YouTube
driver.get("https://www.youtube.com")

# Aguarda a página carregar
driver.implicitly_wait(5)

# Localiza a barra de pesquisa e envia o nome do vídeo
search_box = driver.find_element("name", "search_query")
search_box.send_keys("Nome do Vídeo que Você Gosta")
search_box.send_keys(Keys.RETURN)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Caminho para o ChromeDriver
driver_path = 'CAMINHO/DO/SEU/CHROMEDRIVER'

# Inicializa o navegador
driver = webdriver.Chrome(executable_path=driver_path)

# Acessa o formulário
driver.get("URL_DO_SEU_FORMULARIO")

# Aguarda a página carregar
driver.implicitly_wait(5)

# Preenche os campos
driver.find_element(By.XPATH, 'CAMINHO_XPATH_NOME').send_keys("Seu Nome")
driver.find_element(By.XPATH, 'CAMINHO_XPATH_EMAIL').send_keys("seuemail@dominio.com")
driver.find_element(By.XPATH, 'CAMINHO_XPATH_MENSAGEM').send_keys("Sua mensagem aqui.")

# Envia o formulário
driver.find_element(By.XPATH, 'CAMINHO_XPATH_BOTAO_ENVIAR').click()

# Aguarda a confirmação
time.sleep(5)

# Fecha o navegador
driver.quit()
