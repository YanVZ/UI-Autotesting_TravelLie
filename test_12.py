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

    

    def test_guest_should_materials_of_body(self, browser): 
        print("start test12_materials_of_body")
        browser.get(link)
        time.sleep(20)  # Чтоб успеть вручную ввести капчу...
    
     #Материал корпуса
        browser.find_element_by_xpath("//div[14]/div/div/fieldset/ul/li/div/label/div").click() #Вкл
        time.sleep(2)

        browser.find_element_by_xpath("//div[1]/div/div/div/article[1]/div[4]/div[1]/h3/a").click()
        browser.switch_to.window(browser.window_handles[1])
        browser.find_element_by_xpath("//div[2]/div[8]/div/div/div/ul/li[2]/div/a").click() #Выбираем вкладку "Характеристики"
        time.sleep(2)
        wood = browser.find_element_by_xpath("//div[1]/div/div/div/div[3]/dl[2]/dd")
        wood = wood.text
        assert "красное дерево" == wood

        browser.close()

        browser.switch_to.window(browser.window_handles[0])
        
        browser.find_element_by_xpath("//div[14]/div/div/fieldset/ul/li/div/label/div").click() #Выкл
        time.sleep(2)




      