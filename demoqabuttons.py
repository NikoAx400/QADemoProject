import time
import step

#автотест проверяет нажатие кнопок "Buttons" в меню "Elements" на сайте demoqa.com

step.browserOpen()
step.pressbuttonText("Elements")
step.pressbuttonText("Buttons")
step.pressbuttonText("Click Me")
step.doublebuttonclik("Double Click Me")
step.findtext("You have done a dynamic click")
step.findtext("You have done a double click")
step.browserClose()