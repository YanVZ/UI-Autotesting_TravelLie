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

    


    def test_guest_should_other_checkboxes(self, browser): 
        print("start test7_other_checkboxes")
        browser.get(link)
        time.sleep(20)  # Чтоб успеть вручную ввести капчу...
    
        # Тип крепления грифа
        browser.find_element_by_xpath("//div[13]/div/div/fieldset/ul/li/div/label/div").click() #Вкл 
        grif1 = browser.find_element_by_xpath("//article[7]/div[4]/div[2]/ul/li[4]")
        grif1 = grif1.text
        assert "болченый гриф" == grif1
        time.sleep(2)
        browser.find_element_by_xpath("//div[13]/div/div/fieldset/ul/li/div/label/div").click() #Выкл  
        time.sleep(3)

        browser.find_element_by_xpath("//div[13]/div/div/fieldset/ul/li[2]/div/label/div").click() #Вкл
        time.sleep(2)
        grif2 = browser.find_element_by_xpath("//div[1]/div/div/div/article[1]/div[4]/div[2]/ul/li[4]")
        grif2 = grif2.text
        assert "вклеенный гриф" == grif2
        browser.find_element_by_xpath("//div[13]/div/div/fieldset/ul/li[2]/div/label/div").click() #Выкл
        time.sleep(3)

        browser.find_element_by_xpath("//div[13]/div/div/fieldset/ul/li[3]/div/label/div").click() #Вкл
        time.sleep(2)
        grif3 = browser.find_element_by_xpath("//div[1]/div/div/div/article[2]/div[4]/div[2]/ul/li[4]")
        grif3 = grif3.text
        assert "сквозной гриф" == grif3
        time.sleep(2)
        browser.find_element_by_xpath("//div[13]/div/div/fieldset/ul/li[3]/div/label/div").click() #Выкл
        time.sleep(3)

       