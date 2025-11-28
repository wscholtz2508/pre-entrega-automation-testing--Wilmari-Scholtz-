from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import os


# Constantes de configuración
URL="https://www.saucedemo.com/"
USERNAME="standard_user"
PASSWORD="secret_sauce"

def get_driver():
    #Crea y devuelve una instancia de ChromeDriver configurada.

    options = Options()
    options.add_argument("--start-maximized")      # inicia maximizado
    options.add_argument("--disable-notifications") # evita popups
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")


    #instalacion de driver
    service= Service(ChromeDriverManager().install())
    driver= webdriver.Chrome(service=service, options=options)



    #time.sleep(5)
    driver.implicitly_wait(5)
    #driver.implicitly_wait(10)

    return driver 

def login_saucedemo(driver):
    #Inicia sesión en SauceDemo con credenciales por defecto. 

    driver.get(URL)

# Espera explícitamente a que el campo user esté visible y clickeable
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "user-name"))
    ).send_keys(USERNAME)

    #Ingresar las credenciales
    #driver.find_element(By.NAME, "user-name").send_keys(USERNAME)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()

    # Esperar que redirija al inventario (mejor que sleep)
    WebDriverWait(driver, 10).until(
        EC.url_contains("/inventory.html")
    )

    # Espera visible el título Products
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".title"))
    )

    # time.sleep opcional para debug visual 
    time.sleep(5)


def get_file_path(file_name, folder="Data"):
    current_file = os.path.dirname(__file__)
    file_path = os.path.join(current_file,"..",folder,file_name)

    #../Data/data_login.csv > rlativo qe se tien que transfrmar en absoluto
    return  os.path.abspath(file_path)