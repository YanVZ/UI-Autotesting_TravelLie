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

class TestMainPage3():

    

   

    def test_guest_should_see_select_bonus(self, browser):
        print("start test15_select_bonus")
        browser.get(link)

        time.sleep(20)
        #ПОДАРОК ЗА ПОКУПКУ
        browser.find_element_by_xpath("//div[20]/div/div/fieldset/ul/li[3]/div/label/div").click() #
        time.sleep(3)
        bonus = browser.find_element_by_xpath("//div/article[1]/div[5]/div[1]/div[2]/div")
        bonus = bonus.text
        assert "Подарок за покупку" == bonus
        
        