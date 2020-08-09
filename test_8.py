# Проверка полей цены "от" и "до"
import pytest
from selenium import webdriver
import time

link = "https://market.yandex.ru/catalog--elektrogitary-v-ioshkar-ole/17478561/list?hid=91244&onstock=1"



@pytest.fixture(scope="class")  # фикстура открытия и закрытия браузера
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")

class TestMainPage9():

    

    def test_guest_should_active_electronic(self, browser): 
        print("start test4_price")
        browser.get(link)
        time.sleep(20)  # Чтоб успеть вручную ввести капчу...
    
        # Активная электроника
        browser.find_element_by_xpath("//div[10]/div/div/fieldset/ul/li[1]/div/label/div").click()  # Да
        time.sleep(2)
        active_elc = browser.find_element_by_xpath("//div[1]/div/div/div/article[1]/div[4]/div[2]/ul/li[4]")  # 
        active_elc = active_elc.text
        assert "активная электроника" == active_elc         
        time.sleep(3)