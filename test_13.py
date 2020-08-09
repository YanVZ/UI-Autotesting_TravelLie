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

    


    def test_guest_should_matherial_of_vultures(self, browser): 
        print("start test13_matherial_of_vultures")
        browser.get(link)
        time.sleep(20)  # Чтоб успеть вручную ввести капчу...
    
        # Материал грифа
        browser.find_element_by_xpath("//div[15]/div/div/fieldset/ul/li[2]/div/label/div").click() #Вкл 
        browser.find_element_by_xpath("//div[16]/div/div/fieldset/ul/li[4]/div/label/div").click() #Вкл  
        time.sleep(3)

        browser.find_element_by_xpath("//div[1]/div/div/div/article[3]/div[4]/div[1]/h3/a").click() #Переход на страницу товара
        time.sleep(2)

        browser.switch_to.window(browser.window_handles[1]) #Переход на другую вкладку
        browser.find_element_by_xpath("//div[2]/div[8]/div/div/div/ul/li[2]/div/a").click() #Выбираем вкладку "Характеристики"
        time.sleep(2)
        vilture = browser.find_element_by_xpath("//div[4]/div[1]/div/div/div/div[4]/dl[1]/dd")
        vilture = vilture.text
        assert "красное дерево, накладка: черное дерево" == vilture
        
        time.sleep(3)