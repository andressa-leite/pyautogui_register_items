# This file is used exclusively to capture mouse coordinates: it waits 5 seconds so the user can move the cursor to the desired position or window, then prints the current (x, y) mouse position to be used later in PyAutoGUI automations.

import pyautogui
import time

pyautogui.sleep(5)
  # wait 5 seconds to give you time to switch to the target window
print(pyautogui.position())