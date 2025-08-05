from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configurações do navegador
options = Options()
options.headless = False  # Mude para True se quiser rodar "escondido"

# Inicia o navegador
navegador = webdriver.Chrome(options=options)

try:
    # Abre o YouTube
    navegador.get("https://www.youtube.com")
    time.sleep(3)  # Espera carregar a página

    # Encontra o campo de busca e pesquisa o tema
    campo_busca = navegador.find_element(By.NAME, "search_query")
    tema = "Lo-fi music"
    campo_busca.send_keys(tema)
    campo_busca.send_keys(Keys.ENTER)
    time.sleep(4)  # Espera os resultados carregarem

    # Pega os títulos dos vídeos
    titulos = navegador.find_elements(By.ID, "video-title")

    print(f"\n🎧 Resultados para: {tema}\n")
    for i in range(min(5, len(titulos))):
        print(f"{i+1}. {titulos[i].text}")

    # Vai para o formulário fictício
    navegador.get("https://exemplo.com/formulario")
    time.sleep(2)  # Espera carregar

    # Preenche os campos do formulário
    campo_nome = navegador.find_element(By.ID, "nome")
    campo_nome.send_keys("João")

    campo_email = navegador.find_element(By.ID, "email")
    campo_email.send_keys("joao@email.com")

finally:
    # Fecha o navegador ao final, mesmo se der erro
    navegador.quit()