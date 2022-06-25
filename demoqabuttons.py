import time

import step

start = step.driver
step.pressbuttonText("Elements")
step.pressbuttonText("Buttons")
step.pressbuttonText("Click Me")
step.doublebuttonclik("Double Click Me")
time.sleep(3)
step.findtext("You have done a dynamic click")
step.findtext("You have done a double click")
finish = step.driver.quit()