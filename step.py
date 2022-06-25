from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebdriverWait
import time




p = r'C:\Users\User\OneDrive\Рабочий стол\project_Ax400\chromedriver_py\chromedriver.exe' #расположение драйвера
driver = webdriver.Chrome(executable_path=p) # запуск драйвера
#driver.get("https://www.google.com/") # вход на сайт
driver.get("https://demoqa.com/")
driver.maximize_window()


def findtext(text):
    driver.find_element(by=By.XPATH, value=f'//*[text()="{text}"]')
    return text

def pressbuttonText(text):
    driver.find_element(by=By.XPATH, value=f'//*[text()="{text}"]').click()
    return text

def doublebuttonclik(text):
    elem = driver.find_element(by=By.XPATH, value=f'//*[text()="{text}"]')
    ActionChains(driver).double_click(elem).perform()



def pressCheckBox(text):
    driver.find_element(by=By.XPATH, value=f'//*[text()="{text}"]').click()
    return text

def pressradiobutton(text):
    driver.find_element(by=By.XPATH, value=f'//*[text()="{text}"]').click()

def presstitle(text):
    driver.find_element(by=By.XPATH, value=f'//*[@title="{text}"]').click()
    return text

def pressToggle(text):
    driver.find_element(by=By.XPATH, value=f'//*[text()="{text}"]/ancestor::label/parent::span/child::button/child::*').click()


def inputtext(text, input_word):
    driver.find_element(by=By.XPATH, value=f'//*[text() = "{text}"]/parent::div/following-sibling::div/input').send_keys(f"{input_word}")

def inputtextarea(text, input_word):
    driver.find_element(by=By.XPATH, value=f'//*[text() = "{text}"]/parent::div/following-sibling::div/textarea').send_keys(f"{input_word}")

def inputPlaceHolder(text, input_word):
    driver.find_element(by=By.XPATH, value=f'//*[@placeholder="{text}"]' ).send_keys(f"{input_word}")

def waitLoad():
    driver.implicitly_wait(100)

def managOftable(last_name, action):
    driver.find_element(by=By.XPATH, value=f'//*[text()="{last_name}"]/following::*[contains(@title, "{action}")]').click()





























