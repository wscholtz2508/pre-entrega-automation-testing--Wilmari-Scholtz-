# Page/inventory_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class InventoryPage:

    URL_CURRENT = '/inventory.html'
    MENU_BUTTON = (By.ID, 'react-burger-menu-btn')
    LINK_BUTTON = (By.ID, 'logout_sidebar_link')
    CART_BUTTON = (By.CLASS_NAME, 'shopping_cart_link')  # selector correcto (class)
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, ".btn_inventory")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self , driver):
        self.driver = driver

    def is_at_page(self):
        return self.URL_CURRENT in self.driver.current_url

    def logout(self):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.MENU_BUTTON)
        ).click()
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.LINK_BUTTON)
        ).click()

    def add_product_to_cart(self, index=0):
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)
        if len(buttons) == 0:
            raise Exception("No se encontraron productos para agregar al carrito")
        if index < 0 or index >= len(buttons):
            raise IndexError("Index fuera de rango en add_product_to_cart")
        # click normal en el botón Add to cart
        buttons[index].click()
        # espera corta para que la UI actualice el badge (si aplica)
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.CART_BADGE)
            )
        except Exception:
            # no abortamos; puede que el badge no se muestre inmediatamente
            time.sleep(0.5)

    def go_to_cart(self, max_attempts: int = 3, wait_after_click: float = 0.5):
        """
        Intenta navegar al carrito de forma robusta sin usar JS.
        - Busca el elemento con class 'shopping_cart_link'
        - Usa ActionChains para mover y clickear (evita overlays simples)
        - Reintenta varias veces si la URL no cambia
        """
        attempts = 0
        while attempts < max_attempts:
            attempts += 1
            try:
                # esperar que el elemento esté presente y clickable
                el = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.CART_BUTTON)
                )

                # Mover el mouse hacia el elemento y hacer click con ActionChains
                actions = ActionChains(self.driver)
                actions.move_to_element(el).pause(0.05).click(el).perform()

                # Esperar un pequeño tiempo a que la navegación ocurra
                time.sleep(wait_after_click)

                # Confirmar que la URL cambió a /cart.html
                if "/cart.html" in self.driver.current_url:
                    return  # éxito
                # si no cambió, intentamos de nuevo (posible overlay o animación)
                time.sleep(0.2)
            except Exception as e:
                # Esperar un poco antes de reintentar
                time.sleep(0.3)
                # seguir reintentando hasta max_attempts
        # Si llegamos aquí, no logró navegar al carrito
        raise Exception(f"No se pudo navegar al carrito luego de {max_attempts} intentos. URL actual: {self.driver.current_url}")
