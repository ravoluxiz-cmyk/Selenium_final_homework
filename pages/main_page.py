from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger

URL = "https://www.chitai-gorod.ru/"

class Main_page(Base):
    """Main page"""
    def __init__(self, driver):
        super().__init__(driver)

    #Locators
    Yes_Im_here = '//*[@id="tippy-1"]/div/div/div/div/button[1]'
    Catalog = '//*[@id="__nuxt"]/div/div[2]/div/header/div/div[1]/button'
    Fiction = '//span[contains(text(), "Художественная литература")]'
    Russian = '//span[contains(text(), "Российская литература")]'

    #Getters

    def get_yes_im_here(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.Yes_Im_here)))

    def get_button_catalog(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.Catalog)))

    def get_button_fiction(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.Fiction)))

    def get_button_russian(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.Russian)))

    #Actions

    def click_yes_im_here(self):
        self.safe_click((By.XPATH, self.Yes_Im_here))

    def click_button_catalog(self):
        self.safe_click((By.XPATH, self.Catalog))

    def click_button_fiction(self):
        self.safe_click((By.XPATH, self.Fiction))

    def click_button_russian(self):
        self.safe_click((By.XPATH, self.Russian))
    #Methods

    def main_page_actions(self):

        Logger.add_start_step(method='main_page_actions')
        self.driver.get(URL)
        self.get_current_url()
        self.click_yes_im_here()
        self.click_button_catalog()
        self.click_button_fiction()
        self.click_button_russian()
        Logger.add_end_step(url=self.driver.current_url, method='main_page_actions')
