import time
import step


step.browserOpen()
step.pressbuttonText("Elements")
step.pressbuttonText("Web Tables")
step.inputPlaceHolder("Type to search", "Alden")
time.sleep(2)
step.managOftable("Cantrell", "Edit")
time.sleep(2)
step.browserClose()
