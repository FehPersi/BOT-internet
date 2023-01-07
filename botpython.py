import pyautogui

pyautogui.pause = 3

# abrir a ferramenta/ o sistema / o programa

pyautogui.press("win")
pyautogui.write("login.xlsx")
pyautogui.press("backspace")
pyautogui.press("enter")
 
# preencher login

"""é preciso descobrir a posição do em que o mouse irá clicar dentro do arquivo.
com isso, é preciso utilizar o seguinte código

import.time
time.sleep(3)
pyautogui.position()

quando rodar o código, o comando vai printar a posição que estará o mouse, 
indicando a posição em que deve preencher para clicar

ex- 

x=800, y=768"""

pyautogui.click(x=800, y=768)
pyautogui.write("login")

#mesmo procedimento para preecher a senha
pyautogui.click(x=90, y=76)
pyautogui.write("senha")

#mesmo procedimento para clicar em login
pyautogui.click(x=90, y=76)

# importante que em cada procedimento de click, é preciso descobrir a posição 
# terminamos o bot no computador
