# Bibliotecas = pacotes de códigos prontos que podemos usar no nosso programa
# pip install pyautogui

import pyautogui
import time
import pandas

# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.write -> escrever algo no teclado
# pyautogui.press -> apertar alguma tecla do teclado
# pyautogui.hotkey -> apertar uma combinação de teclas do teclado (atalhos)

pyautogui.PAUSE = 2.5  # tempo de espera entre cada comando
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
email = "seu_email@mail.com"
senha = "sua_senha"

# Passo a passo do seu programa
# Passo 1: entrar no sistema da empresa
# abrir o navegador
#pyautogui.press("win")
#pyautogui.write("chrome")
#pyautogui.press("enter")
#pyautogui.write(link)
#pyautogui.press("enter")
# pausa para o navegador abrir a página
#time.sleep(3)

# para mac seria:
pyautogui.hotkey("command", "space")
pyautogui.write("safari") #ou safari
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(5)

# Passo 2: Fazer login
#clicar no campo de email
pyautogui.click(x=685, y=451)
pyautogui.write(email)
pyautogui.press("tab")  # passar para o próximo campo
pyautogui.write(senha)
pyautogui.click("tab")  # passar para o botão de login
pyautogui.press("enter")
time.sleep(4)
# Passo 3: Abrir a base de dados
tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    # Passo 4: Cadastrar 1 produto
    # codigo
    pyautogui.click(x=653, y=294)  # clicar no campo de código
    codigo = tabela.loc[linha, "codigo"]  # pegar o código do produto da tabela
    pyautogui.write(codigo)  # escrever o código do produto
    pyautogui.press("tab")  # passar para o próximo campo
    # marca
    marca = tabela.loc[linha, "marca"]  # pegar a marca do produto da tabela
    pyautogui.write(marca)  # escrever a marca do produto
    pyautogui.press("tab")  # passar para o próximo campo
    # tipo
    tipo = tabela.loc[linha, "tipo"]  # pegar o tipo do produto da tabela
    pyautogui.write(tipo)  # escrever o tipo do produto
    pyautogui.press("tab")  # passar para o próximo campo
    # categoria
    categoria = tabela.loc[linha, "categoria"]  # pegar a categoria do produto da tabela
    pyautogui.write(str(categoria))  # escrever a categoria do produto
    pyautogui.press("tab")  # passar para o próximo campo
    # preco_unitario
    preco_unitario = tabela.loc[linha, "preco_unitario"]  # pegar o preço unitário do produto da tabela
    pyautogui.write(str(preco_unitario))  # escrever o preço unitário do produto
    pyautogui.press("tab")  # passar para o próximo campo
    # custo
    custo = tabela.loc[linha, "custo"]  # pegar o custo do produto da tabela
    pyautogui.write(str(custo))  # escrever o custo do produto
    pyautogui.press("tab")  # passar para o próximo campo
    # Obs
    obs = tabela.loc[linha, "obs"]  # pegar as observações do produto da tabela
    if obs != "nan":  # verificar se o campo de observações não está vazio
        pyautogui.write(obs)  # escrever as observações do produto
    pyautogui.press("tab")  # passar para o próximo campo
    pyautogui.press("enter")  # apertar o botão de cadastrar

    pyautogui.scroll(5000) # rolar a tela para cima para cadastrar o próximo produto

# Passo 5: Repetir o passo 4 até acabar a lista de produtos
