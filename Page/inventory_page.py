from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:

    URL_CURRENT = '/inventory.html'
    MENU_BUTTON = (By.ID, 'react-burger-menu-btn')
    LINK_BUTTON = (By.ID, 'logout_sidebar_link')

    def __init__(self , driver):
        self.driver = driver

    def is_at_page( self ):
        return self.URL_CURRENT in self.driver.current_url
    
    def logout( self ):
        self.driver.find_element(*self.MENU_BUTTON).click()
        time.sleep(5)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LINK_BUTTON)
        ).click()



