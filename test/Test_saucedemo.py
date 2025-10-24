import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from utils.helpers import login_saucedemo, get_driver


def take_screenshot(driver, test_name):
    """Guarda una captura de pantalla con el nombre del test y timestamp."""
    timestamp = time.strftime("%Y%m%d-%H%M%S")

    # Ruta absoluta desde la raíz del proyecto
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    screenshots_dir = os.path.join(project_root, "screenshots")
    os.makedirs(screenshots_dir, exist_ok=True)

    filename = f"{test_name}_{timestamp}.png"
    filepath = os.path.join(screenshots_dir, filename)

    # Guardar captura
    success = driver.save_screenshot(filepath)
    if success:
        print(f" Captura guardada en: {filepath}")
    else:
        print(f" No se pudo guardar la captura en: {filepath}")



@pytest.fixture()
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_login(driver):

    login_saucedemo(driver)
    assert "/inventory.html" in driver.current_url
    titulo = driver.find_element(By.CSS_SELECTOR, "div.header_secondary_container .title").text
    assert titulo == "Products"
    take_screenshot(driver, "test_login")

    


#logueo de usuer con username y pssword
#click en boton de login 
#validar que redirika a la pag de inventari
#verificr eltitulo de pagina (venanita)


def test_catalogo(driver):
    login_saucedemo(driver)

    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(products) > 0
    take_screenshot(driver, "test_catalogo")


#logueo de usuer con username y pssword
#click en boton de login 
#verificar el tt pero del html 
#Comprobar si existen productos en la pagina visible (len())
#verificar elemntos importantes en la  pagina


def test_carrito(driver):
    login_saucedemo(driver)
    wait = WebDriverWait(driver, 10)  # tiempo de espera más largo

    # Esperar a que cargue el inventario
    wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    total_productos = len(products)
    assert total_productos > 0


    # --- Paso 1: Agregar el primer producto ---
    first_button = products[0].find_element(By.TAG_NAME, "button")
    driver.execute_script("arguments[0].click();", first_button)  # clic más confiable

    # Esperar hasta que el botón cambie a "Remove"
    wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "btn_secondary"), "Remove"))

    # --- Paso 2: Esperar que aparezca el badge del carrito ---
    badge = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    ).text

    assert badge == "1", f"El badge debería ser '1', pero es {badge}"

    # --- Paso 3: Agregar segundo producto (si hay más) ---
    if total_productos >= 2:
        second_button = products[1].find_element(By.TAG_NAME, "button")
        driver.execute_script("arguments[0].click();", second_button)
        wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "shopping_cart_badge"), "2"))
        badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert badge == "2", f"El badge debería ser '2', pero es {badge}"

    take_screenshot(driver, "test_carrito")
   
   #No pude hacer funcionar la captura :(