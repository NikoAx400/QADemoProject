from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import step

step.browserOpen()
step.pressbuttonText("Elements")
step.pressbuttonText("Check Box")
step.pressCheckBox("Home")
step.pressCheckBox("Home")
step.pressToggle("Home")
step.pressToggle("Desktop")
step.pressToggle("Documents")
step.pressToggle("Downloads")
step.pressToggle("WorkSpace")

step.pressToggle("Office")
step.pressCheckBox("Private")
step.pressCheckBox("Classified")
step.presstitle("Collapse all")
step.presstitle("Expand all")
time.sleep(2)
step.browserClose()
