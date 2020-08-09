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

class TestMainPage():

    
#ПОЛЯ ЦЕНЫ 
    def test_guest_should_see_price_of_guitar(self, browser): # Поля ввода цены
        print("start test1_price")
        browser.get(link)
        time.sleep(20)  # Чтоб успеть вручную ввести капчу...
    
        # Проверка функции поля "Цена"
        browser.find_element_by_id("glpricefrom").send_keys("57000")  # Вводим значение в поле цены "от"
        browser.find_element_by_id("glpriceto").send_keys("57000")  # Вводим значение цены "до"         
        time.sleep(5)
        price_text = browser.find_element_by_xpath("//a/div/span/span")
        price_text = price_text.text
        assert "57 000" == price_text

        
#МАРКА ГИТАРЫ
    def test_guest_should_see_model_of_guitar(self, browser):  # Выбор макрки гитары 
        print("start test2_model_guitar")
        browser.get(link)

        # time.sleep(20)

        browser.find_element_by_xpath("//li[4]/div/a/label/div").click() #Жмем чекбокс Epiphone
        time.sleep(3)
        guitar_name = browser.find_element_by_xpath("//h3/a/span")
        guitar_name = guitar_name.text
        assert "Электрогитара Epiphone Les Paul Special VE" == guitar_name

        
       
#ТИП ГИТАРЫ (бАС/ЭЛЕКТРО)   
    def test_guest_should_see_select_type(self, browser):
        print("start test3_select_type")
        browser.get(link)

        #time.sleep(20)

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

        browser.close()    

        browser.switch_to.window(browser.window_handles[0]) #Переключаемся обратно на первую вкладку
        time.sleep(2)
        browser.find_element_by_xpath("//div[5]/div/div/fieldset/ul/li[3]/div/label/div").click() #Жмем чекбокс выбрать типа - электрогитара
        browser.find_element_by_xpath("//div[5]/div/div/fieldset/ul/li[1]/div/label/div").click() #Чекбокс бас-гитара
        time.sleep(2)
        browser.find_element_by_xpath("//div[1]/div/div/div/article[1]/div[4]/div[1]/h3/a").click()
        browser.switch_to.window(browser.window_handles[1]) #Переключаемся на открывшуюся вкладку
        
        browser.find_element_by_xpath("//div[2]/div[8]/div/div/div/ul/li[2]/div/a").click()
        time.sleep(1)
        type_guitar1 = browser.find_element_by_xpath("//div[2]/dl[1]/dd")
        type_guitar1 = type_guitar1.text
        assert "бас-гитара" == type_guitar1 
        time.sleep(1)
        browser.close()


        browser.switch_to.window(browser.window_handles[0]) #Переключаемся на открывшуюся вкладку 
        #time.sleep(1)


#КОЛИЧЕСТВО СТРУН 
    def test_guest_should_see_select_guitar_strings(self, browser):
        print("start test4_select_guitar_strings")
        browser.get(link)

        #time.sleep(20)

        browser.find_element_by_xpath("//div[6]/div/div/fieldset/ul/li[5]/div/label/div").click() #Жмем чекбокс выбрать 8 струн
        time.sleep(3)
        browser.find_element_by_xpath("//div/div/article[1]/div[4]/div[1]/h3/a").click() #Переходим по ссылке
        
        browser.switch_to.window(browser.window_handles[1]) #Переключаемся на открывшуюся вкладку 

        time.sleep(1)    

        browser.find_element_by_xpath("//div[2]/div[8]/div/div/div/ul/li[2]/div/a").click() #Выбираем вкладку "Характеристики"
        time.sleep(1)
        string = browser.find_element_by_xpath("//div[1]/div/div/div/div[2]/dl[3]/dd")
        string = string.text
        assert "8" == string    
        browser.close()

        browser.switch_to.window(browser.window_handles[0]) #Переключаемся на открывшуюся вкладку 
        time.sleep(5)
        browser.find_element_by_xpath("//div[6]/div/div/fieldset/ul/li[5]/div/label").click()


#ТИП БРИДЖА
    def test_guest_should_see_select_strings(self, browser):
        print("start test5_select_strings")
        browser.get(link)

        #time.sleep(20)

        browser.find_element_by_xpath("//div/div[3]/div/div/div[2]/div[7]/div/div/fieldset/ul/li[1]/div/label/div").click() #Tremolo
        time.sleep(3)
        browser.find_element_by_xpath("//div[1]/div/div/div/article[1]/div[4]/div[1]/h3").click() #Переходим по ссылке
        
        browser.switch_to.window(browser.window_handles[1]) #Переключаемся на открывшуюся вкладку 

        time.sleep(1)    

        browser.find_element_by_xpath("//div[2]/div[8]/div/div/div/ul/li[2]/div/a").click() #Выбираем вкладку "Характеристики"
        time.sleep(1)
        string = browser.find_element_by_xpath("//div[1]/div/div/div/div[3]/dl[2]/dd")
        string = string.text
        assert "тремоло, система Floyd Rose" == string  
        browser.close()
        browser.switch_to.window(browser.window_handles[0])  
        time.sleep(3)

#ТИП КОРПУСА
    def test_guest_should_see_select_form_guitar(self, browser):
        print("start test6_select_form_gutar")
        browser.get(link)

        #time.sleep(20)

        browser.find_element_by_xpath("//div[8]/div/div/fieldset/footer/button").click() #Показать список
        time.sleep(3)
        browser.find_element_by_xpath("//div[8]/div/div/fieldset/ul/li[8]/div/label/div").click() #Выбрать"агрессивная"
        time.sleep(2)
        browser.find_element_by_xpath("//div[1]/div/div/div/article[1]/div[4]/div[1]/h3/a").click() #Жмём ссылку
        
        browser.switch_to.window(browser.window_handles[1]) #Переключаемся на открывшуюся вкладку 

        time.sleep(1)    

        browser.find_element_by_xpath("//div[2]/div[8]/div/div/div/ul/li[2]/div/a").click() #Выбираем вкладку "Характеристики"
        time.sleep(1)
        form_guitar = browser.find_element_by_xpath("//div[3]/dl[1]/dd")
        form_guitar = form_guitar.text
        assert "агрессивная" == form_guitar
        time.sleep(3)
        browser.close()
        
        browser.switch_to.window(browser.window_handles[0]) 
        
        


#СХЕМА ЗВУКОСНИМАТЕЛЕЙ
    def test_guest_should_see_select_electronic(self, browser):
        print("start test7_select_electronic")
        browser.get(link)

        #time.sleep(20)

        browser.find_element_by_xpath("//div[9]/div/div/fieldset/footer/button").click() #Показать список
        time.sleep(3)
        browser.find_element_by_xpath("//div[9]/div/div/fieldset/ul/li[5]/div/label/div/span").click() #H-S-H"
        time.sleep(2)
        browser.find_element_by_xpath("//div[2]/div/div[1]/div/div/div/article[1]/div[4]/div[1]/h3/a").click() #Жмём ссылку
        
        browser.switch_to.window(browser.window_handles[1]) #Переключаемся на открывшуюся вкладку 

        time.sleep(1)    

        browser.find_element_by_xpath("//div[2]/div[8]/div/div/div/ul/li[2]/div/a").click() #Выбираем вкладку "Характеристики"
        time.sleep(1)
        electronic = browser.find_element_by_xpath("//div[5]/dl[1]/dd")
        electronic = electronic.text
        assert "H-S-H" == electronic
        time.sleep(3)
        browser.close()

        browser.switch_to.window(browser.window_handles[0]) #Переключаемся обратно на  первую вкладку
        
   


#АКТИВНАЯ ЭЛЕКТРОНИКА
    def test_guest_should_active_electronic(self, browser): 
        print("start test8_active_electronic")
        browser.get(link)
        #time.sleep(20)  # Чтоб успеть вручную ввести капчу...
    
        # Активная электроника
        browser.find_element_by_xpath("//div[10]/div/div/fieldset/ul/li[1]/div/label/div").click()  # Да
        time.sleep(2)
        active_elc = browser.find_element_by_xpath("//div[1]/div/div/div/article[1]/div[4]/div[2]/ul/li[5]")  # 
        active_elc = active_elc.text
        assert "активная электроника" == active_elc         
        time.sleep(3)

#ПОЛЯ КОЛИЧЕСТВО ЛАДОВ
    def test_guest_should_see_lads(self, browser): 
        print("start test9_lads")
        browser.get(link)
        #time.sleep(20)  # Чтоб успеть вручную ввести капчу...
    
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
        time.sleep(2)
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
        time.sleep(3)
        browser.close()

        browser.switch_to.window(browser.window_handles[0])
     

#МЕНЗУРА
    def test_guest_should_see_scale(self, browser): 
        print("start test10_scale")
        browser.get(link)
        #time.sleep(20)  # Чтоб успеть вручную ввести капчу...
    
        # Мензура
        browser.find_element_by_name("Мензура от").send_keys("0")  # Заполнение поля "Мензура от"Ы
        browser.find_element_by_name("Мензура до").send_keys("0") # Заполнение поля "Мензура до"
        time.sleep(2)
        scale0 = browser.find_element_by_xpath("//article/div/div[2]")  # 
        scale0 = scale0.text
        assert "Таких товаров нет, увы" == scale0         
        time.sleep(3)
  
        browser.find_element_by_xpath("//div[12]/div/div/fieldset/div/ul/li/p/button").click() #Жмём кнопку yочистить поле от
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
        time.sleep(3)
        browser.close()
        
        browser.switch_to.window(browser.window_handles[0])
        time.sleep(5)


#ТИПА КРЕПЛЕНИЯ ГРИФА
    def test_guest_should_guitar_neck_mount(self, browser): 
        print("start test11_guitar_neck_mount")
        browser.get(link)
        #time.sleep(20)  # Чтоб успеть вручную ввести капчу...
    
        # Тип крепления грифа
        browser.find_element_by_xpath("//div[13]/div/div/fieldset/ul/li[1]/div/label/div/span").click() #Вкл 
        time.sleep(2)
        guitar_neck_mount = browser.find_element_by_xpath("//article[7]/div[4]/div[2]/ul/li[4]")
        guitar_neck_mount = guitar_neck_mount.text
        assert "болченый гриф" == guitar_neck_mount
        time.sleep(2)
        browser.find_element_by_xpath("//div[13]/div/div/fieldset/ul/li[1]/div/label/div/span").click() #Выкл  
        time.sleep(3)

        browser.find_element_by_xpath("//div[13]/div/div/fieldset/ul/li[2]/div/label/div/span").click() #Вкл
        time.sleep(2)
        grif2 = browser.find_element_by_xpath("//div[1]/div/div/div/article[1]/div[4]/div[2]/ul/li[4]")
        grif2 = grif2.text
        assert "вклеенный гриф" == grif2
        browser.find_element_by_xpath("//div[13]/div/div/fieldset/ul/li[2]/div/label/div/span").click() #Выкл
        time.sleep(3)

        browser.find_element_by_xpath("//div[13]/div/div/fieldset/ul/li[3]/div/label/div/span").click() #Вкл
        time.sleep(2)
        grif3 = browser.find_element_by_xpath("//div[1]/div/div/div/article[2]/div[4]/div[2]/ul/li[4]")
        grif3 = grif3.text
        assert "сквозной гриф" == grif3
        time.sleep(2)
        browser.find_element_by_xpath("//div[13]/div/div/fieldset/ul/li[3]/div/label/div/span").click() #Выкл
        time.sleep(5)



#МАТЕРИАЛ КОРПУСА
    def test_guest_should_materials_of_body(self, browser): 
        print("start test12_materials_of_body")
        browser.get(link)
        #time.sleep(20)  # Чтоб успеть вручную ввести капчу...
    
     #Материал корпуса
        browser.find_element_by_xpath("//div[14]/div/div/fieldset/ul/li/div/label/div").click() #Вкл
        time.sleep(2)

        browser.find_element_by_xpath("//div[1]/div/div/div/article[1]/div[4]/div[1]/h3/a").click()
        browser.switch_to.window(browser.window_handles[1])
        time.sleep(2)
        browser.find_element_by_xpath("//div[2]/div[8]/div/div/div/ul/li[2]/div/a").click() #Выбираем вкладку "Характеристики"
        time.sleep(2)
        wood = browser.find_element_by_xpath("//div[1]/div/div/div/div[3]/dl[2]/dd")
        wood = wood.text
        assert "красное дерево" or "красное дерево, топ: клен" == wood
        time.sleep(2)
        browser.close()
        browser.switch_to.window(browser.window_handles[0])
        



        
        browser.find_element_by_xpath("//div[14]/div/div/fieldset/ul/li/div/label/div").click() #Выкл
        time.sleep(5)



#МАТЕРИАЛ ГРИФА, НАКЛАДКИ ГРИФА
    def test_guest_should_material_of_vultures(self, browser): 
        print("start test13_material_of_vultures")
        browser.get(link)
        #time.sleep(20)  # Чтоб успеть вручную ввести капчу...
    
       
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
        browser.switch_to.window(browser.window_handles[0])
        browser.close()

        
        
        

    def test_guest_should_see_type_orientation(self, browser):
        print("start test14_select_type_orientation")
        browser.get(link)

        #time.sleep(20)

        #ОРИЕНТАЦИЯ
        browser.find_element_by_xpath("//div[17]/div/div/fieldset/ul/li[2]/div/label/div").click() #
        time.sleep(3)
        browser.find_element_by_xpath("//div/article[1]/div[4]/div[1]/h3/a").click() #
        
        browser.switch_to.window(browser.window_handles[1]) #Переключаемся на открывшуюся вкладку 

        time.sleep(2)    

        browser.find_element_by_xpath("//div[2]/div[8]/div/div/div/ul/li[2]/div/a").click() #Выбираем вкладку "Характеристики"
        time.sleep(1)
        orientation = browser.find_element_by_xpath("//div[6]/dl[5]/dd")
        orientation = orientation.text
        assert "правосторонняя" == orientation
        browser.close()

        browser.switch_to.window(browser.window_handles[0])



    def test_guest_should_see_select_bonus(self, browser):
        print("start test15_select_bonus")
        browser.get(link)

        #time.sleep(20)

        #ПОДАРОК ЗА ПОКУПКУ
        browser.find_element_by_xpath("//div[20]/div/div/fieldset/ul/li[3]/div/label/div").click() #
        time.sleep(3)
        bonus = browser.find_element_by_xpath("//div/article[1]/div[5]/div[1]/div[2]/div")
        bonus = bonus.text
        assert "Подарок за покупку" == bonus



    def test_guest_should_see_select_delivery(self, browser):
        print("start test16_select_delivery")
        browser.get(link)

        #time.sleep(20)
        #ДОСТАВКА
        browser.find_element_by_xpath("//div[23]/div/div/fieldset/ul/li[1]/div/label/div").click() #
        time.sleep(3)
        browser.find_element_by_xpath("//div[24]/div/div/fieldset/ul/li[1]/div/label/div").click() #
        time.sleep(2)
        browser.find_element_by_xpath("//div[5]/div[1]/div[2]/a").click() #Жмём ссылку
        
        browser.switch_to.window(browser.window_handles[1]) #Переключаемся на открывшуюся вкладку 

        time.sleep(1)    
        delivery = browser.find_element_by_xpath("//div[2]/div[9]/div[2]/div[1]/div/div/div/div/div/div/div/div[4]/div[1]/div/div[2]/span[2]")
        delivery_tomorrow = browser.find_element_by_xpath("//div[9]/div[2]/div[1]/div/div/div/div/div/div/div/div[4]/div[1]/div/div[2]/span[3]")
        delivery = delivery.text
        assert "Бесплатно курьером" == delivery
        delivery_tomorrow = delivery_tomorrow.text
        assert "завтра" == delivery_tomorrow
        browser.close()



    def test_guest_should_see_select_all_filters(self, browser):
        print("start test17_select_all_filters")
        browser.get(link)
        #time.sleep(20)


#КНОПКА "ВСЕ ФИЛЬТРЫ"
        browser.find_element_by_xpath("//div[3]/div/div/div[3]/div/div/a").click() #Все фильтры
        
        time.sleep(3)
        all_filters = browser.find_element_by_xpath("//div[2]/div[5]/section/div[1]/h1") #Ищем надпись "Все фильтры"
        all_filters = all_filters.text
        assert "Все фильтры" == all_filters
        
    

    