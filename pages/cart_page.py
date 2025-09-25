# from selenium.webdriver import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException  # Добавьте этот импорт
#
# from base.base_class import Base
# from utilities.logger import Logger
#
#
# class Cart_page(Base):
#     """Cart page"""
#
#     def __init__(self, driver):
#         super().__init__(driver)
#
#     # Локаторы (переместил в начало класса)
#     button_locator = "//button[@type='button' and contains(text(), 'Перейти к оформлению')]"
#
#     # Getters
#     def get_confirmation(self):
#         return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_locator)))
#
#     def find_checkout_button(self):
#         """Найти кнопку 'Перейти к оформлению' с несколькими вариантами локаторов"""
#         locators = [
#             (By.XPATH, "//button[contains(text(), 'Перейти к оформлению')]"),
#             (By.CSS_SELECTOR, "button.chg-app-button--primary"),
#             (By.XPATH, "//button[@type='button' and contains(text(), 'оформлению')]"),
#             (By.XPATH, "//*[contains(@class, 'chg-app-button--primary')]"),
#             (By.XPATH, self.button_locator)  # Ваш исходный локатор
#         ]
#
#         for locator in locators:
#             try:
#                 element = WebDriverWait(self.driver, 10).until(
#                     EC.element_to_be_clickable(locator)
#                 )
#                 print(f"Элемент найден с локатором: {locator}")
#                 return element
#             except TimeoutException:
#                 print(f"Локатор {locator} не сработал, пробуем следующий...")
#                 continue
#
#         raise Exception("Не удалось найти кнопку 'Перейти к оформлению' ни одним локатором")
#
#     # Actions
#     def click_confirmation(self):
#         """Клик по кнопке подтверждения с использованием надежного поиска"""
#         try:
#             # Сначала пробуем найти элемент надежным способом
#             element = self.find_checkout_button()
#             element.click()
#         except Exception:
#             # Если не получилось, используем fallback через safe_click
#             self.safe_click((By.XPATH, self.button_locator))
#
#     # Methods
#     def cart_page_actions(self):
#         """Основные действия на странице корзины"""
#         Logger.add_start_step(method='cart_page_actions')
#         self.get_current_url()
#
#         # Дождаться загрузки страницы корзины
#         WebDriverWait(self.driver, 15).until(
#             EC.presence_of_element_located((By.CLASS_NAME, "cart-sidebar__footer"))
#         )
#
#         self.click_confirmation()
#         Logger.add_end_step(url=self.get_current_url(), method='cart_page_actions')