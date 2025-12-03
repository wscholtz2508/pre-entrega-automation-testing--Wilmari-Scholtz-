from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutCompletePage:
    COMPLETE_HEADER = (By.CLASS_NAME, 'complete-header')
    COMPLETE_TEXT = (By.CLASS_NAME, 'complete-text')
    BACK_HOME_BUTTON = (By.ID, 'back-to-products')
    URL_CURRENT = '/checkout-complete.html'
    SUCCESS_MESSAGE = (By.CLASS_NAME, 'complete-header')  # Selector del mensaje de éxito
    SUCCESS_IMAGE = (By.CLASS_NAME, 'pony_express')  # Imagen de éxito

    def __init__(self, driver):
        self.driver = driver

    def is_at_page(self):
        """Verifica si estamos en la página de checkout completo."""
        return self.URL_CURRENT in self.driver.current_url

    def get_complete_header(self):
        """Obtiene el título principal "THANK YOU FOR YOUR ORDER"."""
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.COMPLETE_HEADER)
        ).text

    def get_complete_text(self):
        """Obtiene el texto secundario debajo del título."""
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.COMPLETE_TEXT)
        ).text

    def back_to_home(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.BACK_HOME_BUTTON)
        ).click()

    def get_success_message(self):
        # Espera a que el mensaje esté visible y lo devuelve
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
        ).text

    def is_success_image_displayed(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SUCCESS_IMAGE)
        ).is_displayed()
