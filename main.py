import os
from web_functions import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs
import requests
import numpy as np
import openpyxl as op
from selenium.common.exceptions import WebDriverException
import pandas as pd


#get no url informado para o webscrapping
req = requests.get("https://gruposeb.gupy.io/")
site = bs(req.content, 'html.parser')
dados = site.findAll('a', attrs={'data-testid': 'job-list__listitem-href'})

#criando um array vazio com a estrutura adequada para receber os dados
arr_vagas = np.empty((len(dados),), dtype=object)

#percorrendo os elementos encontrados
for i, vaga in enumerate(dados):
    #pegar as 'divs' dentro de cada <li>
    divs = vaga.find('div')

    #pegar o texto de cada 'div' e adicionar na lista de vagas
    arr_vagas[i] = [div.get_text(strip=True) for div in divs]

#print no console os dados capturados
for vaga in arr_vagas:
    print(vaga)

#formatar um excel com o retorno do webscrapping
excel_dir = "excel_vagas_seb"
os.makedirs(excel_dir, exist_ok=True)

workbook = op.Workbook()
sheet = workbook.active

head = ["Cargo", "Localidade", "Efetividade"]
sheet.append(head)

for vagas in arr_vagas:
    sheet.append(vagas)

workbook.save(f"{excel_dir}/vagas_seb.xlsx")

time.sleep(2)
# fechar o excel
workbook.close()

#lendo excel
df = pd.read_excel(f"{excel_dir}/vagas_seb.xlsx")

# iniciar o chrome
driver_path = ChromeDriverManager().install()
driver = webdriver.Chrome()

# acessar site
url = 'https://forms.office.com/pages/responsepage.aspx?id=QhQEvrbz4UuFCeypyBdSj7tyC7WzU59DoUmUzzgLXidUNllOQ0JYNjVMSDZSN1Q4MUFZWlVXQkw0UC4u'
driver.get(url)
time.sleep(1)

cont = 0
# percorrer excel e preencher formulário
for indice, linha in df.iloc[1:].iterrows():
    cargo = linha['Cargo']
    localidade = linha['Localidade']
    efetividade = linha['Efetividade']

    time.sleep(3)

    # marcando opção efetivo "sim" ou "não"
    if efetividade.lower() == "efetivo":
        click_element(driver, css_selector='[data-automation-value="Sim"]')
    else:
        click_element(driver, css_selector='[data-automation-value="Não"]')

    # preenchendo cidade
    null_verif_localidade = df.at[indice, 'Localidade']
    if pd.isnull(null_verif_localidade):
        localidade = "sem localidade informada"

    xpath_cidade = "//span[contains(text(), 'Cidade')]/ancestor::div[@data-automation-id='questionItem']//input[@data-automation-id='textInput']"
    inject_input(driver, keys=localidade, xpath=xpath_cidade)

    # preenchendo Cargo
    null_verif_cargo = df.at[indice, 'Cargo']
    if pd.isnull(null_verif_cargo):
        cargo = "sem cargo informado"

    xpath_cargo = "//span[contains(text(), 'Cargo')]/ancestor::div[@data-automation-id='questionItem']//input[@data-automation-id='textInput']"
    inject_input(driver, keys=cargo, xpath=xpath_cargo)

    # tirando print do preenchimento e salvando na pasta 'screenshots_forms'
    screenshot_dir = "screenshots_forms"
    os.makedirs(screenshot_dir, exist_ok=True)
    time.sleep(1)

    try:
        screenshot_filename = f"{screenshot_dir}/preenchido__{cont}.jpg"
        driver.save_screenshot(screenshot_filename)
        print(f"Screenshot salvo como: {screenshot_filename}")
        time.sleep(5)
    except WebDriverException as e:
        print(f"Erro ao salvar o screenshot: {e}")

    # clicando em enviar
    click_element(driver, css_selector='[data-automation-id="submitButton"]')

    time.sleep(3)

    #clicando para enviar um novo formulário
    click_element(driver, css_selector='[data-automation-id="submitAnother"]')

    print(cont)
    cont += 1


# fechar navegador
driver.quit()