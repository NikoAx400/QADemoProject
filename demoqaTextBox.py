from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import step

start = step.driver

step.pressbuttonText("Elements")
step.pressbuttonText("Text Box")
step.inputtext("Full Name", "Никоглай Гуревич")
step.inputtext("Email", "Nikoglay@mail.ru")
step.inputtextarea("Current Address", "Москва, такой город есть")
step.inputtextarea("Permanent Address", "это Москва")
step.pressbuttonText("Submit")
time.sleep(5)
finish = step.driver.quit()
