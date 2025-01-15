import pyautogui
import time

pyautogui.PAUSE = 1

# Passo 1: Abrir o sistema da empresa
#    Sistema: https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.press("win")

pyautogui.write("chrome")

pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)

# Passo 2: Fazer login
pyautogui.click(x=525, y=404)

pyautogui.write("treinamento@gmail.com")

pyautogui.press("tab")

pyautogui.write("1.2.3.5.6.")

pyautogui.press("tab")

pyautogui.press("enter")

# Passo 3: Importar a base de dados dos produtos
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

time.sleep(2)
# Passo 4: Cadastrar um produto.

for linha in tabela.index:
    pyautogui.click(x=423, y=292)

    #codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    # marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    #tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    #categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    #preço_unitario
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    #custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    #obs
    obs = str(tabela.loc[linha, "obs"])
    
    if obs != "NaN" or "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.scroll(5000)
# Passo 5: Repetir o passo 4 até acabar todos os produtos.