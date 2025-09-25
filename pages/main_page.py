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
    Russian_classics = '//*[@id="__nuxt"]/div/div[3]/div[1]/div/div/div[2]/div/aside/section/div[2]/a[4]'
    Fedor_dostoevsky = '//*[@id="__nuxt"]/div/div[3]/div[1]/div/div/div[2]/div/aside/div/section[8]/div[3]/div[2]/section/div/label[1]/span/span[2]/span'
    Buy_button = '//*[@id="__nuxt"]/div/div[3]/div[1]/div/div/div[2]/div/div/div[3]/div[1]/div[2]/div[4]/button[1]'
    Cart = '//*[@id="__nuxt"]/div/div[2]/div/header/div/div[2]/button[3]/span[2]'
    Confirmation = '//*[@id="__nuxt"]/div/div[3]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/section[2]/button'

    #Getters

    def get_yes_im_here(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.Yes_Im_here)))

    def get_button_catalog(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.Catalog)))

    def get_button_fiction(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.Fiction)))

    def get_button_russian(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.Russian)))

    def get_button_russian_classics(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.Russian_classics)))

    def get_button_fedor_dostoevsky(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.Fedor_dostoevsky))
        )
        # Прокрутка к элементу
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element

    def get_button_buy_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.Buy_button)))

    def get_button_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.Cart)))

    def get_confirmation(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.Confirmation)))


    #Actions

    def click_yes_im_here(self):
        self.safe_click((By.XPATH, self.Yes_Im_here))

    def click_button_catalog(self):
        self.safe_click((By.XPATH, self.Catalog))

    def click_button_fiction(self):
        self.safe_click((By.XPATH, self.Fiction))

    def click_button_russian(self):
        self.safe_click((By.XPATH, self.Russian))

    def click_button_russian_classics(self):
        self.safe_click((By.XPATH, self.Russian_classics))

    def click_button_fedor_dostoevsky(self):
        self.safe_click((By.XPATH, self.Fedor_dostoevsky))

    def click_button_buy_button(self):
        self.safe_click((By.XPATH, self.Buy_button))

    def click_button_cart(self):
        self.safe_click((By.XPATH, self.Cart))


    def click_confirmation(self):
        self.safe_click((By.XPATH, self.Confirmation))

    #Methods

    def main_page_actions(self):

        Logger.add_start_step(method='main_page_actions')
        self.driver.get(URL)
        self.get_current_url()
        self.click_yes_im_here()
        self.click_button_catalog()
        self.click_button_fiction()
        self.click_button_russian()
        self.click_button_russian_classics()
        self.click_button_fedor_dostoevsky()
        self.click_button_buy_button()
        self.click_button_cart()
        Logger.add_end_step(url=self.driver.current_url, method='main_page_actions')
