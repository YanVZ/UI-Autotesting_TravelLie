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

    

   

    def test_guest_should_see_select_electronic(self, browser):
        print("start test3_select_electronic")
        browser.get(link)

        time.sleep(20)

        browser.find_element_by_xpath("//div[9]/div/div/fieldset/footer/button").click() #Показать список
        time.sleep(3)
        browser.find_element_by_xpath("//div[9]/div/div/fieldset/ul/li[4]/div/label/div/span").click() #H-S-H"
        time.sleep(2)
        browser.find_element_by_xpath("//div[2]/div/div[1]/div/div/div/article[1]/div[4]/div[1]/h3/a").click() #Жмём ссылку
        
        browser.switch_to.window(browser.window_handles[1]) #Переключаемся на открывшуюся вкладку 

        time.sleep(1)    

        browser.find_element_by_xpath("//div[2]/div[8]/div/div/div/ul/li[2]/div/a").click() #Выбираем вкладку "Характеристики"
        time.sleep(1)
        electronic = browser.find_element_by_xpath("//div[5]/dl[1]/dd")
        electronic = electronic.text
        assert "H-S-H" == electronic
    

        