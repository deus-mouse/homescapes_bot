import pyautogui
from time import sleep


DELAY_BETWEEN_COMANDS = 0.5


def main():
    initializePyAutoGUI()
    countDownTimer(5)
    reportMousePosition()


def initializePyAutoGUI():
    # initialized PyAutoGUI
    pyautogui.FAILSAFE = True


def countDownTimer(seconds):
    # Countdown timer
    print("Starting", end="")
    for i in range(0, seconds):
        print(".", end="")
        sleep(1)
    print("Go")


def reportMousePosition(seconds=10):
    for i in range(0, seconds):
        print(pyautogui.position())
        sleep(DELAY_BETWEEN_COMANDS)


if __name__ == "__main__":
    main()