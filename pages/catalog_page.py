import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Catalog_page(Base):
    """Main page"""
    def __init__(self, driver):
        super().__init__(driver)

    #Locators
    Russian_classics = '//*[@id="__nuxt"]/div/div[3]/div[1]/div/div/div[2]/div/aside/section/div[2]/a[4]'
    Fedor_dostoevsky = '//*[@id="__nuxt"]/div/div[3]/div[1]/div/div/div[2]/div/aside/div/section[8]/div[3]/div[2]/section/div/label[1]/span/span[2]/span'
    Buy_button = '//*[@id="__nuxt"]/div/div[3]/div[1]/div/div/div[2]/div/div/div[3]/div[1]/div[2]/div[4]/button[1]'
    Cart = '//*[@id="__nuxt"]/div/div[2]/div/header/div/div[2]/button[3]/span[2]'

    #Getters

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

    #Actions

    def click_button_russian_classics(self):
        self.safe_click((By.XPATH, self.Russian_classics))

    def click_button_fedor_dostoevsky(self):
        self.safe_click((By.XPATH, self.Fedor_dostoevsky))

    def click_button_buy_button(self):
        self.safe_click((By.XPATH, self.Buy_button))

    def click_button_cart(self):
        self.safe_click((By.XPATH, self.Cart))

    #Methods

    def catalog_page_actions(self):
        with allure.step("Покупка книги и переход в корзину"):
            Logger.add_start_step(method='cart_page_actions')
            self.get_current_url()
            self.click_button_russian_classics()
            self.click_button_fedor_dostoevsky()
            self.click_button_buy_button()
            self.click_button_cart()
            Logger.add_end_step(url=self.get_current_url(), method='cart_page_actions')