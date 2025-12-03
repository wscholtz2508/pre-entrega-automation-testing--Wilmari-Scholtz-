import pytest
from Page.login_page import LoginPage
from Data.data_login import CASOS_LOGIN
from utils.example_csv import get_login_csv, get_login_json
import os
from utils.faker import get_login_faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.mark.parametrize("username, password, login_bool", get_login_faker())
def test_login( driver, username, password, login_bool):
    #crear objeto
    loginPage = LoginPage (driver)
    loginPage.open()
    loginPage.login(username, password)

    if login_bool:
        # Espera que el catálogo se cargue (elemento de inventario)
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "inventory_container"))
        )
    else:
        # Espera error
        assert "https://www.saucedemo.com/" in driver.current_url