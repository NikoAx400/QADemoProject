import time
import step

#автотест проверяет заполнение всех полей в разделе "Text Box" в меню "Elements" на сайте demoqa.com

step.browserOpen()
step.pressbuttonText("Elements")
step.pressbuttonText("Text Box")
step.inputtext("Full Name", "Никоглай Гуревич")
step.inputtext("Email", "Nikoglay@mail.ru")
step.inputtextarea("Current Address", "Москва, такой город есть")
step.inputtextarea("Permanent Address", "это Москва")
step.pressbuttonText("Submit")
time.sleep(2)
step.browserClose()
