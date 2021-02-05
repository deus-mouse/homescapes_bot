
import pyautogui
import time
import cv2 as cv
import numpy as np


time.sleep(3)



image = pyautogui.screenshot(region=(560, 202, 1365, 768))
image = cv.cvtColor(np.array(image), cv.COLOR_RGB2BGR)
cv.imwrite('needles/window2.png', image)
