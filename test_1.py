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

    
    def test_guest_should_see_price_of_guitar(self, browser): # Поля ввода цены
        print("start test1_price")
        browser.get(link)
        time.sleep(20)  # Чтоб успеть вручную ввести капчу...
    
        # Проверка функции поля "Цена"
        browser.find_element_by_id("glpricefrom").send_keys("57000")  # Вводим значение в поле цены "от"
        browser.find_element_by_id("glpriceto").send_keys("57000")  # Вводим значение цены "до"         
        time.sleep(5)
        price_text = browser.find_element_by_xpath("//a/div/span/span")
        price_text = price_text.text
        assert "57 000" == price_text