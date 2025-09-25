from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger

class Cart_page(Base):
    """Main page"""
    def __init__(self, driver):
        super().__init__(driver)

    Confirmation = '//*[@id="__nuxt"]/div/div[3]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/section[2]/button'

    #Getters

    def get_confirmation(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.Confirmation)))


    #Actions

    def click_confirmation(self):
        self.safe_click((By.XPATH, self.Confirmation))

    #Methods

    def cart_page_actions(self):

        Logger.add_start_step(method='cart_page_actions')
        self.get_current_url()
        self.click_confirmation()
        Logger.add_end_step(url=self.driver.current_url, method='cart_page_actions')