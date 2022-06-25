from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import step

start = step.driver

step.waitLoad()

step.buttonText("Почта")
step.buttonText("Зарегистрироваться в Gmail")
step.inputtext_ariaLabel("Имя", "Никоглай")
step.inputtext_ariaLabel("Фамилия", "Никоглаев")
step.inputtext_ariaLabel("Пароль", "19898989dP")
step.inputtext_ariaLabel("Подтвердить", "19898989dP")
step.buttonText("Показать пароль")
time.sleep(3)
step.buttonText("Далее")
step.inputtext_arialabelledby("c4", "49585858br")
time.sleep(3)
step.buttonText("Далее")

assert step.findtext("Неизвестный формат. Убедитесь, что страна и номер телефона указаны правильно."), "фраза не найдена, тест не выполнен"
time.sleep(5)
finish = step.driver.quit()

#kolyan.v1988@gmail.com



