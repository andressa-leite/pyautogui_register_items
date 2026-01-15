import pyautogui
import time
import pandas

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
time.sleep(2)  # wait for the dashboard to load

# step 3: Import dadabase (products.csv)
tabela = pandas.read_csv('produtos.csv')

# step 4: register a product
for linha in tabela.index:
    # open the product registration form
    pyautogui.click(x=486, y=292)  # "Register Product" button
    time.sleep(2)  # wait for the form to load

    # get data from the DataFrame
    codigo = str(tabela.loc[linha, 'codigo'])
    marca = str(tabela.loc[linha, 'marca'])
    tipo = str(tabela.loc[linha, 'tipo'])
    categoria = str(tabela.loc[linha, 'categoria'])
    preco_unitario = str(tabela.loc[linha, 'preco_unitario'])
    custo = str(tabela.loc[linha, 'custo'])
    obs = tabela.loc[linha, 'obs']

   

    # fill in the form fields
    pyautogui.click(x=551, y=294)  # click on the first input field
    pyautogui.write(codigo)
    
    pyautogui.press('tab')

    pyautogui.write(marca)
    pyautogui.press('tab')

    pyautogui.write(tipo)
    pyautogui.press('tab')

    pyautogui.write(categoria)
    pyautogui.press('tab')

    pyautogui.write(preco_unitario)
    pyautogui.press('tab')

    pyautogui.write(custo)
    pyautogui.press('tab')

    # handle empty observations (NaN)
    if pandas.notna(obs):  # if obs != 'nan':
        pyautogui.write(str(obs))  # pyautogui.write(obs)

    # submit the form
    pyautogui.press('tab')  

    pyautogui.press('enter')       
    pyautogui.scroll(10000)  # scroll up to the top of the page
    time.sleep(0.5)  # short pause before the next registration


# step 5: repeat step 4 for all products in the database
# pyautogui - library to automate mouse and keyboard actions