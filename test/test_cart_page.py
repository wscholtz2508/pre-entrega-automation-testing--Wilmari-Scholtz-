import pytest
from Page.login_page import LoginPage
from Page.inventory_page import InventoryPage
from Page.cart_page import CartPage
import time

def test_cart_operations(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")

    time.sleep(2)
    #Agregar producto e ir al carrito
    inventory.add_product_to_cart(0)
    inventory.go_to_cart()

    # dentro de test_cart_page.py, justo después de inventory.go_to_cart()
    print("DEBUG -> URL actual (post go_to_cart):", driver.current_url)

    try:
        title_text = driver.find_element("class name", "title").text
    except Exception as e:
        title_text = f"no title ({e})"
    print("DEBUG -> Título encontrado:", title_text)

    print("DEBUG -> is_at_page():", cart.is_at_page())



    assert cart.is_at_page()
    assert cart.get_cart_items_count() == 1

    #Seguir comprando 
    cart.continue_shopping()
    assert inventory.is_at_page()

    def test_remove_from_cart(driver):
        login = LoginPage(driver)
        inventory = InventoryPage(driver)
        cart = CartPage(driver)

        login.open()
        login.login("standar_user", "secret_sauce")
        time.sleep(3)

        inventory.add_product_to_cart(0)
        inventory.go_to_cart()

   

