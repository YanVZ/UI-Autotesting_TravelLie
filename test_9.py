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

    

    def test_guest_should_see_lads(self, browser): 
        print("start test9_lads")
        browser.get(link)
        time.sleep(20)  # Чтоб успеть вручную ввести капчу...
    
        # Поля колличество ладов
        browser.find_element_by_name("Количество ладов от").send_keys("0")  # Заполнение поля "Количество ладов от"
        browser.find_element_by_name("Количество ладов до").send_keys("20") # Заполнение поля "Количество ладов до"
        time.sleep(2)
 
        browser.find_element_by_xpath("//div/article[1]/div[4]/div[1]/h3/a").click()
        time.sleep(2)
        browser.switch_to.window(browser.window_handles[1])
        time.sleep(2)
        browser.find_element_by_xpath("//div[2]/div[8]/div/div/div/ul/li[2]/div/a").click() #Выбираем вкладку "Характеристики"
        time.sleep(2)

        lads = browser.find_element_by_xpath("//div[4]/dl[3]/dd")  # 
        lads = lads.text
        assert "20" == lads         
        time.sleep(1)
        browser.close()
        browser.switch_to.window(browser.window_handles[0])
  
        browser.find_element_by_xpath("//div[11]/div/div/fieldset/div/ul/li/p/button").click() #Жмём кнопку очистить поле от
        browser.find_element_by_xpath("//div[11]/div/div/fieldset/div/ul/li[2]/p/button").click() #Жмём кнопку очистить поле до

        time.sleep(1)

        browser.find_element_by_name("Количество ладов от").send_keys("20")  # Заполнение поля "Количество ладов от"
        browser.find_element_by_name("Количество ладов до").send_keys("0") # Заполнение поля "Количество ладов до"
        time.sleep(2)

        
        lads1 = browser.find_element_by_xpath("//article/div/div[2]") #Сообщение: "Таких товаров нет, увы"
        lads1 = lads1.text
        assert "Таких товаров нет, увы" == lads1
        time.sleep(3)

        browser.find_element_by_xpath("//div[11]/div/div/fieldset/div/ul/li/p/button").click() #Жмём кнопку очистить поле от
        browser.find_element_by_xpath("//div[11]/div/div/fieldset/div/ul/li[2]/p/button").click() #Жмём кнопку очистить поле до

        browser.find_element_by_name("Количество ладов от").send_keys("24")  # Заполнение поля "Количество ладов от"
        browser.find_element_by_name("Количество ладов до").send_keys("24") # Заполнение поля "Количество ладов до"
        time.sleep(2)
        browser.find_element_by_xpath("//div[1]/div/div/div/article[1]/div[4]/div[1]/h3/a").click()
        browser.switch_to.window(browser.window_handles[1])
        time.sleep(1)
        browser.find_element_by_xpath("//div[2]/div[8]/div/div/div/ul/li[2]/div/a").click() #Выбираем вкладку "Характеристики"
        time.sleep(1)
        lads2 = browser.find_element_by_xpath("//div[4]/dl[2]/dd") #Сообщение: "24"
        lads2 = lads2.text
        assert "24" == lads2
        browser.close()
        browser.switch_to.window(browser.window_handles[0])
     