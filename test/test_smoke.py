import time
from pages.main_page import Main_page
from utilities.conftest import set_up


def test_smoke(set_up):

    mp = Main_page(set_up)  # Передаем драйвер из фикстуры
    mp.main_page_actions()
    time.sleep(3)
