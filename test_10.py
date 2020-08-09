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

    

    def test_guest_should_see_scale(self, browser): 
        print("start test9_scale")
        browser.get(link)
        time.sleep(20)  # Чтоб успеть вручную ввести капчу...
    
        # Мензура
        browser.find_element_by_name("Мензура от").send_keys("0")  # Заполнение поля "Мензура от"
        browser.find_element_by_name("Мензура до").send_keys("0") # Заполнение поля "Мензура до"
        time.sleep(2)
        scale0 = browser.find_element_by_xpath("//article/div/div[2]")  # 
        scale0 = scale0.text
        assert "Таких товаров нет, увы" == scale0         
        time.sleep(3)
  
        browser.find_element_by_xpath("//div[12]/div/div/fieldset/div/ul/li/p/button").click() #Жмём кнопку очистить поле от
        browser.find_element_by_xpath("//div[12]/div/div/fieldset/div/ul/li[2]/p/button").click() #Жмём кнопку очистить поле до

        time.sleep(1)

        browser.find_element_by_name("Мензура от").send_keys("35")  # Заполнение поля "Количество ладов от"
        browser.find_element_by_name("Мензура до").send_keys("35") # Заполнение поля "Количество ладов до"
        time.sleep(2)

        browser.find_element_by_xpath("//div[1]/div/div/div/article[1]/div[4]/div[1]/h3/a").click()
        browser.switch_to.window(browser.window_handles[1])
        browser.find_element_by_xpath("//div[2]/div[8]/div/div/div/ul/li[2]/div/a").click() #Выбираем вкладку "Характеристики"
        time.sleep(2)
        scale1 = browser.find_element_by_xpath("//div[2]/dl[2]/dd") #Сообщение: "35"
        scale1 = scale1.text
        assert '35"' == scale1
        time.sleep(1)
        browser.close()

        browser.switch_to.window(browser.window_handles[0])