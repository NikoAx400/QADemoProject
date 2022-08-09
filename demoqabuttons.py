import time
import step
import allure
from allure_commons.types import AttachmentType



step.browserOpen()
step.pressbuttonText("Elements")
step.pressbuttonText("Buttons")
step.pressbuttonText("Click Me")
step.doublebuttonclik("Double Click Me")
step.findtext("You have done a dynamic click")
step.findtext("You have done a double click")
step.browserClose()