import time
import step


start = step.driver
step.pressbuttonText("Elements")
step.pressbuttonText("Radio Button")
step.pressradiobutton("Impressive")
time.sleep(2)
step.pressradiobutton("Yes")
time.sleep(2)
finish = step.driver.quit()