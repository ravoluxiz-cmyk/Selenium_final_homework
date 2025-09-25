import datetime
import time

from selenium.common import ElementClickInterceptedException, TimeoutException, StaleElementReferenceException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base():

    def __init__(self, driver):
        self.driver = driver



    def get_current_url(self):
        """Method get current url"""
        get_url = self.driver.current_url
        print("Current url is: ", get_url)

    def assert_word(self, word, result):
        """Method assert word"""
        value_word = word.text
        assert value_word == result
        print("Word is good")

    def screenshot(self):
        """Method screenshot"""
        now_date = datetime.datetime.today().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = now_date + ".png"
        self.driver.save_screenshot("/Users/dmitry/PycharmProjects/main_project/screen/" + name_screenshot)

    def assert_url(self, expected_url):
        actual_url = self.driver.current_url
        print(f"Ожидаемый URL: {expected_url}")
        print(f"Фактический URL: {actual_url}")

        assert actual_url == expected_url, f"URL не совпадает! Ожидался: {expected_url}, получен: {actual_url}"

    def safe_click(self, locator, timeout=20, retries=3):
        """
        Универсальный метод для безопасного клика с обработкой Stale Element
        """
        for attempt in range(retries):
            try:
                # Всегда ищем элемент заново для избежания Stale Element
                element = WebDriverWait(self.driver, timeout).until(
                    EC.element_to_be_clickable(locator)
                )

                # Дополнительная проверка видимости элемента
                if not element.is_displayed():
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                    time.sleep(1)

                # Попытка клика
                element.click()
                return True

            except StaleElementReferenceException:
                print(f"Stale element, повторный поиск элемента {locator}, попытка {attempt + 1}/{retries}")
                # При Stale Element просто переходим к следующей попытке

            except ElementClickInterceptedException:
                try:
                    # JavaScript клик при перекрытии элемента
                    element = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located(locator)
                    )
                    self.driver.execute_script("arguments[0].click();", element)
                    return True
                except Exception:
                    pass

            except TimeoutException:
                print(f"Элемент {locator} не найден, попытка {attempt + 1}/{retries}")
                # Дополнительное ожидание загрузки страницы
                time.sleep(2)

            except Exception as e:
                print(f"Ошибка при клике: {e}, попытка {attempt + 1}/{retries}")

            if attempt < retries - 1:
                time.sleep(2)

        raise Exception(f"Не удалось кликнуть по элементу {locator} после {retries} попыток")