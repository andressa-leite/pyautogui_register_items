# Difference between PyAutoGUI functions:
#
# pyautogui.press():
#
# 01 SINGLE KEY PRESS
# Simulates pressing [A SINGLE keyboard] key (or a sequence of individual keys),
# such as "enter", "tab", or "esc". It does not type text character by character.
#
#
# pyautogui.write():
#
# TEXT
# Types text as if it were typed on the keyboard, [CHARACTER BY CHARACTER] (text).
# It is mainly used for writing strings, numbers, or text into input fields.
#
#
# pyautogui.hotkey():
#
# KEY COMBINATION
# Simulates a keyboard shortcut by pressing multiple keys together [COMBINATION],
# (for example: Ctrl + C, Ctrl + V, or Alt + Tab).
#
#
#
# pyautogui.PAUSE is a module-level configuration setting.
# Uppercase indicates a global setting that affects the entire library behavior.
# Lowercase names are typically used for local variables or functions.
# PAUSE controls the delay (in seconds) after every PyAutoGUI action.

