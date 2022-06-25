from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import step

start = step.driver

step.pressbuttonText("Elements")
time.sleep(5)
step.pressbuttonText("Check Box")
time.sleep(5)
step.pressCheckBox("Home")
time.sleep(5)
step.pressCheckBox("Home")
time.sleep(5)
step.pressToggle("Home")
time.sleep(5)
step.pressToggle("Desktop")
time.sleep(5)
step.pressToggle("Documents")
time.sleep(5)
step.pressToggle("Downloads")
time.sleep(5)

step.pressToggle("WorkSpace")
time.sleep(5)

step.pressToggle("Office")
step.pressCheckBox("Private")
step.pressCheckBox("Classified")
time.sleep(2)
step.presstitle("Collapse all")
time.sleep(2)
step.presstitle("Expand all")
time.sleep(2)
finish = step.driver.quit()
