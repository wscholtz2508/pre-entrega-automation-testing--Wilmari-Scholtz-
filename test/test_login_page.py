import pytest
from Page.login_page import LoginPage
from Data.data_login import CASOS_LOGIN
from utils.example_csv import get_login_csv, get_login_json
import os



@pytest.mark.parametrize("username, password, login_bool", get_login_csv())
def test_login( driver, username, password, login_bool):
    #craer objeto
    loginPage = LoginPage (driver)
    loginPage.open()
    loginPage.login(username, password)

    if login_bool:
        assert "inventory.html" in driver.current_url
    else:
        assert "inventory.html" not in driver.current_url



