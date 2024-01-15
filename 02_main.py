from selenium import webdriver
from web_functions import *
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import time
import os

#incializar o chrome
driver_path = ChromeDriverManager().install()
driver = webdriver.Chrome()

#acessar site
url = 'https://forms.office.com/pages/responsepage.aspx?id=QhQEvrbz4UuFCeypyBdSj7tyC7WzU59DoUmUzzgLXidUNllOQ0JYNjVMSDZSN1Q4MUFZWlVXQkw0UC4u'
driver.get(url)
time.sleep(1.5)

#marcando opção efetivo "sim"
click_element(driver, css_selector='[data-automation-value="Sim"]')

#preenchendo cidade
xpath_cidade = "//span[contains(text(), 'Cidade')]/ancestor::div[@data-automation-id='questionItem']//input[@data-automation-id='textInput']"
inject_input(driver, keys="Ribeirão Preto" ,xpath=xpath_cidade)

#preenchendo Cargo
xpath_cargo = "//span[contains(text(), 'Cargo')]/ancestor::div[@data-automation-id='questionItem']//input[@data-automation-id='textInput']"
inject_input(driver, keys="Desenvolvedor Python Pleno" ,xpath=xpath_cargo)

#tirando print do preenchimento e salvando na pasta 'screenshots_forms'
screenshot_dir = "screenshots_forms"
os.makedirs(screenshot_dir, exist_ok=True)

dt_hr_atual = datetime.now()
dt_hora_atual = dt_hr_atual.strftime("%d-%m-%Y_%H-%M-%S")
screenshot_filename = f"{screenshot_dir}/preenchido_{dt_hora_atual}.png"

driver.save_screenshot(screenshot_filename)
print(f"Screenshot salvo como: {screenshot_filename}")

#clicando em enviar
click_element(driver, css_selector='[data-automation-id="submitButton"]')

driver.quit()