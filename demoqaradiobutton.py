import time
import step

step.browserOpen()
step.pressbuttonText("Elements")
step.pressbuttonText("Radio Button")
step.pressradiobutton("Impressive")
step.waitLoad()
time.sleep(2)
step.pressradiobutton("Yes")
time.sleep(2)
step.browserClose()