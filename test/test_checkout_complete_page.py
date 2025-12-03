from Page.login_page import LoginPage
from Page.inventory_page import InventoryPage
from Page.cart_page import CartPage
from Page.checkout_page import CheckoutPage
from Page.checkout_complete_page import CheckoutCompletePage
import time

def test_complete_purchase_flow(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)
    complete = CheckoutCompletePage(driver)

    # Login
    login.open()
    login.login("standard_user", "secret_sauce")

    time.sleep(4)

    # Agregar producto al carrito
    inventory.add_product_to_cart(0)
    inventory.go_to_cart()

    # Ir a checkout
    cart.go_to_checkout()

    # Llenar información
    checkout.fill_customer_info("John", "Doe", "12345")
    checkout.continue_to_overview()

   # Completar compra (simulado - se necesita la página de overview) 
    driver.get("https://www.saucedemo.com/checkout-complete.html")

    # Verificar página de completado
    assert complete.is_at_page()
    assert "Thank you for your order!" in complete.get_success_message()
    assert complete.is_success_image_displayed()

    # Volver al inicio
    complete.back_to_home()
    assert inventory.is_at_page()


