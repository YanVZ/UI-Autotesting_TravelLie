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

    

   

    def test_guest_should_see_select_type(self, browser):
        print("start test3_select_type")
        browser.get(link)

        time.sleep(20)

        browser.find_element_by_xpath("//div[5]/div/div/fieldset/ul/li[3]/div/label").click() #Жмем чекбокс выбрать типа - электрогитара
        time.sleep(3)
        browser.find_element_by_xpath("//div[1]/div/div/div/article[1]/div[4]/div[1]/h3/a").click() #Переходим по ссылке
        
        browser.switch_to.window(browser.window_handles[1]) #Переключаемся на открывшуюся вкладку 

        time.sleep(1)    

        browser.find_element_by_xpath("//div[2]/div[8]/div/div/div/ul/li[2]/div/a").click() #Выбираем вкладку "Характеристики"
        time.sleep(1)
        type_guitar = browser.find_element_by_xpath("//div[2]/div[5]/div[4]/div[1]/div/div/div/div[2]/dl[1]/dd")
        type_guitar = type_guitar.text
        assert "электрогитара" == type_guitar    

        browser.switch_to.window(browser.window_handles[0]) #Переключаемся обратно на первую вкладку

        browser.find_element_by_xpath("//div/fieldset/ul/li[3]/div/label/div").click() #Жмем чекбокс выбрать типа - электрогитара
        browser.find_element_by_xpath("//div[5]/div/div/fieldset/ul/li[1]/div/label/div").click() #Чекбокс бас-гитара
        time.sleep(3)
        browser.find_element_by_xpath("//div[1]/div/div/div/article[1]/div[4]/div[1]/h3/a").click()

        browser.switch_to.window(browser.window_handles[2]) #Переключаемся на открывшуюся вкладку 

        time.sleep(1)

        browser.find_element_by_xpath("//div[2]/div[8]/div/div/div/ul/li[2]/div/a").click()
        time.sleep(1)
        type_guitar1 = browser.find_element_by_xpath("//div[2]/dl[1]/dd")
        type_guitar1 = type_guitar1.text
        assert "бас-гитара" == type_guitar1 



       