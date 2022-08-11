import time
import step

#автотест проверяет нажатие радиокнопок в разделе "Radio Button" в меню "Elements" на сайте demoqa.com

step.browserOpen()
step.pressbuttonText("Elements")
step.pressbuttonText("Radio Button")
step.pressradiobutton("Impressive")
step.waitLoad()
time.sleep(2)
step.pressradiobutton("Yes")
time.sleep(2)
step.browserClose()