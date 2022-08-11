import time
import step

#автотест проверяет выделение чекбоксов в разделе "Check Box" в меню "Elements" на сайте demoqa.com

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
