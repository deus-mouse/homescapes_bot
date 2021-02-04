import cv2
import pyautogui
import numpy as np




image = pyautogui.screenshot(region=(560, 202, 1365, 768))
# image = pyautogui.screenshot()
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
cv2.imwrite('needles/table.png', image)