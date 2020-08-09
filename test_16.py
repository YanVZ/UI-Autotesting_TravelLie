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

    

   

    def test_guest_should_see_select_delivery(self, browser):
        print("start test3_select_delivery")
        browser.get(link)

        time.sleep(20)
        #ДОСТАВКА
        browser.find_element_by_xpath("//div[23]/div/div/fieldset/ul/li[1]/div/label/div").click() #
        time.sleep(3)
        browser.find_element_by_xpath("//div[24]/div/div/fieldset/ul/li[1]/div/label/div").click() #
        time.sleep(2)
        browser.find_element_by_xpath("//div[5]/div[1]/div[2]/a").click() #Жмём ссылку
        
        browser.switch_to.window(browser.window_handles[1]) #Переключаемся на открывшуюся вкладку 

        time.sleep(3)    
        delivery = browser.find_element_by_xpath("//div[2]/div[9]/div[2]/div[1]/div/div/div/div/div/div/div/div[4]/div[1]/div/div[2]/span[2]")
        delivery_tomorrow = browser.find_element_by_xpath("//div[9]/div[2]/div[1]/div/div/div/div/div/div/div/div[4]/div[1]/div/div[2]/span[3]")
        delivery = delivery.text
        assert "Бесплатно курьером" == delivery
        delivery_tomorrow = delivery_tomorrow.text
        assert "завтра" == delivery_tomorrow
    

        