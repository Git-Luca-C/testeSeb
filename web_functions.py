import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#funcoes para navegação web

def inject_input(driver, keys, xpath=None, id=None, css_selector=None, text=None):
    if xpath:
        input_box = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, xpath)))
    elif id:
        input_box = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID, id)))
    elif text:
        input_box = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, text)))
        input_box.click()
    else:
        input_box = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
    input_box.send_keys(keys)
    time.sleep(.1)
    time.sleep(.9)


def inject_input_submit(driver, keys, xpath=None, id=None, css_selector=None, text=None):
    if xpath:
        input_box = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, xpath)))
    elif id:
        input_box = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID, id)))
    elif text:
        input_box = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, text)))
        input_box.click()
    else:
        input_box = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))

    input_box.send_keys(keys, Keys.ENTER)
    time.sleep(.9)


def click_element(driver, xpath=None, id=None, css_selector=None, text=None):
    if xpath:
        input_box = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, xpath)))
        input_box.click()
    elif id:
        input_box = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID, id)))
        input_box.click()
    elif text:
        input_box = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.LINK_TEXT, text)))
        input_box.click()
    else:
        input_box = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
        input_box.click()
        time.sleep(.1)
    time.sleep(.9)