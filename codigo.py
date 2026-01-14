import pyautogui

# step 1: access the website - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# abrir o chrome
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

# step 2: login with your credentials
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

# step 3: Import dadabase (products.csv)
# step 4: register a product
# step 5: repeat step 4 for all products in the database
# pyautogui - library to automate mouse and keyboard actions