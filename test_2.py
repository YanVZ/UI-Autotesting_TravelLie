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

    
    def test_guest_should_see_model_of_guitar(self, browser):  # Выбор макрки гитары 
        print("start test2_model_guitar")
        browser.get(link)

        # time.sleep(20)

        browser.find_element_by_xpath("//li[4]/div/a/label/div").click() #Жмем чекбокс Epiphone
        time.sleep(3)
        guitar_name = browser.find_element_by_xpath("//h3/a/span")
        guitar_name = guitar_name.text
        assert "Электрогитара Epiphone Les Paul Special VE" == guitar_name

        time.sleep(3)