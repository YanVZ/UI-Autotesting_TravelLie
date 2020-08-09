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

    

   
#КНОПКА "ВСЕ ФИЛЬТРЫ"
    def test_guest_should_see_select_all_filters(self, browser):
        print("start test17_select_all_filters")
        browser.get(link)

        time.sleep(20)

        browser.find_element_by_xpath("//div[3]/div/div/div[3]/div/div/a").click() #Все фильтры
        
        time.sleep(3)
        all_filters = browser.find_element_by_xpath("//div[2]/div[5]/section/div[1]/h1") #Ищем надпись "Все фильтры"
        all_filters = all_filters.text
        assert "Все фильтры" == all_filters
        

        
     
        
       