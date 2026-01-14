import pyautogui
import time

pyautogui.PAUSE = 0.8  # pause for 0.8 second after each PyAutoGUI call

# step 1: access the website - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# abrir o chrome
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(2)  # wait for the page to load

# step 2: login with your credentials
pyautogui.click(x=597, y=408)  # click on the email field
pyautogui.write('seu_email@gmail.com')
pyautogui.press('tab')  # move to the password field
pyautogui.write('sua_senha')
pyautogui.press('enter')  # submit the login form
time.sleep(3)  # wait for the dashboard to load

# step 3: Import dadabase (products.csv)
# step 4: register a product
# step 5: repeat step 4 for all products in the database
# pyautogui - library to automate mouse and keyboard actions