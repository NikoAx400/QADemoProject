import time
import step

"""автотеcт проверяет поиск по таблице и открытие регистрационной формы
в разделе "Web tables" в меню "Elements" на сайте demoqa.com """

step.browserOpen()
step.pressbuttonText("Elements")
step.pressbuttonText("Web Tables")
step.inputPlaceHolder("Type to search", "Alden")
time.sleep(2)
step.managOftable("Cantrell", "Edit")
time.sleep(2)
step.browserClose()
