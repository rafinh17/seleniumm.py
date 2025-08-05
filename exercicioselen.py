from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By

import time

# Configurações

options = webdriver.ChromeOptions()

options.headless = False

navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

navegador.get("https://docs.google.com/forms/d/e/1FAIpQLSe1kM6GuDUR34BcH88YdKuiCcjCQVevFWhElbNLtsoBHGob2A/viewform?usp=dialog")

time.sleep(2)

campos = navegador.find_elements(By.CLASS_NAME, "whsOnd")

campos[0].send_keys("João da Silva")

campos[1].send_keys("joao@email.com")



time.sleep(3)

