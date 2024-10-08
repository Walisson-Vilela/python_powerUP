# Passo 1: Acessar o site https://dlp.hashtagtreinamentos.com/python/intensivao/login
#rodar comando pip install pyautogui
#rodar comando pip install time
import pyautogui
import time

pyautogui.PAUSE = 0.5

# Passo 2: Fazer o login

##Acessar o link
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

## Quero dar uma pausa de 3 segundos para dar tempo de carregamento da pagina
time.sleep(3)
pyautogui.press("tab")
pyautogui.write("walissonvilela@gmail.com")
pyautogui.press("tab")
pyautogui.write("123")
pyautogui.press("enter")

time.sleep(2)

# Passo 3: Importar base de dados
#rodar comando pip install pandas
import pandas as pd

tabela = pd.read_csv("produtos.csv")
print(tabela)
time.sleep(2)

pyautogui.PAUSE = 0.1
for linha in range(len(tabela)):
    pyautogui.press("tab")
    
    # Código
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    
    # Marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    
    # Tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    
    # Categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    
    # Preço unitário
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")
    
    # Custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    
    # Obs
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")
    
    # Clicar em enviar
    pyautogui.press("enter")    
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    
    # Pausar para garantir que o sistema processe antes do próximo cadastro
# Passo 5: Repetir o processo de cadastro até acabar os produtos