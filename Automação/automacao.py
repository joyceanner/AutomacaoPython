# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas


import pyautogui
import time
pyautogui.PAUSE = 0.7  



# Passo a passo do projeto

# passo 1: Entrar no sistema da empresa

#Abir o navegador
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

#Entrar no link
link = 'https://projetinho-gomes.netlify.app/'
pyautogui.write (link)
pyautogui.press('enter')
time.sleep(3)


#Selecionar campo de e-mail
pyautogui.click(x=844, y=537)
#Escrever e-mail
pyautogui.write('joyceannerodrigues@gmail.com')
pyautogui.press('tab')
pyautogui.write(str('156578'))
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')

# Passo 3: Importar a base de produtos pra cadastrar 

import pandas as pd

tabela= pd.read_csv('produtos.csv')

print(tabela)

# Passo 4: Cadastrar produto
for linha in tabela.index:
    #clicar no campo de código
    pyautogui.click(x=863, y=333)
    #pegar da tabela o valor do campoque quer preecher
    codigo =  tabela.loc[linha, "codigo"]
    #preencher campo
    pyautogui.write(str(codigo))
    #passar para o proximo campo
    pyautogui.press('tab')
    #preencher campo
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')

    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, 'obs']))
    pyautogui.press('tab')
    pyautogui.press('enter') #cadastrar produto (botão enviar)
    #dar scroll de tudo pra cima
    #pyautogui.scroll(5000)    



