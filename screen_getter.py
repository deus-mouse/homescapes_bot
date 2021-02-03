

from engine import initialize_pyautogui, countdown_timer, play_actions
from time import sleep
import pyautogui as pg

DELAY_BETWEEN_LOOPS = 3.00



def main():
    initialize_pyautogui()
    countdown_timer()

    LOOP_REPITITIONS = 4
    for i in range(0, LOOP_REPITITIONS):
        # get_starting_pos() should return an integer that corresponds with which
        # recorded action script should be played
        try:
            found = confirm_position("puzzle")
            if found:
                play_actions('?.json')
        except Exception as ex:
            print('Exception', ex)
        finally:
            print('sleep')
            sleep(DELAY_BETWEEN_LOOPS)

        # Completed loop
        print("Completed loop")

    print("Done")


def confirm_position(position_name):
    if position_name == "puzzle":
        x, y = (958, 973)
        rgb = (48, 207, 75)
    else:
        raise Exception("Position to confirm not recognized")

    pixel_matches = pg.pixelMatchesColor(x, y, rgb, tolerance=10)
    if not pixel_matches:
        debug_str = "Pos: {} RGB expected: {} RGB found: {}".format(
            (x, y),
            rgb,
            pg.pixel(x, y)
        )
        raise Exception("Detected off course for {}. Debug: {}".format(
            position_name,
            debug_str
        ))

    print("On track for {}".format(position_name))
    return True


if __name__ == "__main__":
    main()
