import allure
from allure_commons.types import AttachmentType
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebdriverWait
import time

#p = r'C:\Users\User\OneDrive\Рабочий стол\project_Ax400\chromedriver_py\chromedriver.exe' #расположение драйвера
#driver = webdriver.Chrome(executable_path=p) # запуск драйвера
#driver.get("https://www.google.com/") # вход на сайт
#driver.get('https://www.selenium.dev/documentation/webdriver/actions_api/mouse/')
#driver.get("https://demoqa.com/")
#driver.maximize_window()

def browserOpen():
    p = r'C:\Users\User\OneDrive\Рабочий стол\project_Ax400\chromedriver_py\chromedriver.exe'  # расположение драйвера
    global driver
    driver = webdriver.Chrome(p)
    driver.get("https://demoqa.com/")
    driver.maximize_window()

def browserClose():
    driver.quit()


def findtext(text):
    driver.find_element(by=By.XPATH, value=f'//*[text()="{text}"]')
    return text


#("Нажать на кнопку с текстом")
def pressbuttonText(text):
    driver.find_element(by=By.XPATH, value=f'//*[text()="{text}"]').click()
    return text


#("Двойное нажатие на кнопку")
def doublebuttonclik(text):
    elem = driver.find_element(by=By.XPATH, value=f'//*[text()="{text}"]')
    ActionChains(driver).double_click(elem).perform()


#("активировать/снять чекбокс")
def pressCheckBox(text):
    driver.find_element(by=By.XPATH, value=f'//*[text()="{text}"]').click()
    return text

#("Нажать на радиокнопку")
def pressradiobutton(text):
    driver.find_element(by=By.XPATH, value=f'//*[text()="{text}"]').click()

#("Двойное нажатие на кнопку с title")
def presstitle(text):
    driver.find_element(by=By.XPATH, value=f'//*[@title="{text}"]').click()
    return text

#("Двойное нажатие на кнопку с toogle")
def pressToggle(text):
    driver.find_element(by=By.XPATH, value=f'//*[text()="{text}"]/ancestor::label/parent::span/child::button/child::*').click()

#("Ввести текст в поле напротив")
def inputtext(text, input_word):
    driver.find_element(by=By.XPATH, value=f'//*[text() = "{text}"]/parent::div/following-sibling::div/input').send_keys(f"{input_word}")

#("Ввести текст в поле напротив, где есть area")
def inputtextarea(text, input_word):
    driver.find_element(by=By.XPATH, value=f'//*[text() = "{text}"]/parent::div/following-sibling::div/textarea').send_keys(f"{input_word}")

#("Ввести текст в поле напротив, где есть placeholder")
def inputPlaceHolder(text, input_word):
    driver.find_element(by=By.XPATH, value=f'//*[@placeholder="{text}"]').send_keys(f"{input_word}")


# ("Ввести текст в поле напротив, где есть placeholder")
def inputtextClick(text, text2):
    driver.find_element(by=By.XPATH, value=f'//*[contains(text(), "{text}")]').click()
    driver.find_element(by=By.XPATH, value=f'//*[text()="{text2}"]').click()



#("Ожидание")
def waitLoad():
    driver.implicitly_wait(20)

#("управление в таблице")
def managOftable(last_name, action):
    driver.find_element(by=By.XPATH, value=f'//*[text()="{last_name}"]/following::*[contains(@title, "{action}")]').click()

#("перемещение курсора мыши относительно заданного объекта")
def moveMouseClick(text):
    mouse_tracker = driver.find_element(by=By.XPATH, value=f'//*[text()="{text}"]')
    ActionChains(driver) \
        .move_to_element_with_offset(mouse_tracker, 1300, 500).click() \
        .perform()

#def scrollToElement(text):
#    elem = driver.find_element(by=By.XPATH, value=f'//*[text()="{text}"]')
#    ActionChains(driver) \
#        .scroll_to_element(elem) \
#        .perform()

#("прокуртить полосу прокуртки доконца вниз")
def scrollBarDown():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


