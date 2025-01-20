import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.5

## pyautogui.click -> clicar
## pyautogui.press -> pressionar
## pyautogui.write -> escrever
## pyautogui.hotkey -> atalho de teclado

## usando o pyautogui
pyautogui.press('win') ## apertando o botão do windows

pyautogui.write('chrome') ## escrevendo chrome

pyautogui.press('enter') ## apertando enter para abrir o chrome

pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login') ## escrevendo a url no chrome

pyautogui.press('enter') ## apertando enter para acessar a url

## pedir pro computador esperar 3s
time.sleep(3)

## fazer login
pyautogui.click(x=686, y=422)
pyautogui.write('devpedrosena1@gmai.com')

pyautogui.press('tab') ## pula para o campo de senha
pyautogui.write('200909')

pyautogui.press('tab') ## pula para o campo de logar e aperta enter
pyautogui.press('enter')

## importar a base de dados
tabela = pandas.read_csv('produtos.csv')

print(tabela)

time.sleep(3)

## Cadastrar um produto
## Repetir o passo 4 até acabar todos os produtos
for linha in tabela.index:
    pyautogui.click(x=738, y=314)

    ## codigo
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(str(codigo))
    pyautogui.press('tab')

    ## marca
    marca = tabela.loc[linha, 'marca']
    pyautogui.write(str(marca))
    pyautogui.press('tab')

    ## tipo
    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(str(tipo))
    pyautogui.press('tab')

    ## categoria
    categoria = tabela.loc[linha, 'categoria']
    pyautogui.write(str(categoria))
    pyautogui.press('tab')

    ## preco unitario
    preco_unitario = tabela.loc[linha, 'preco_unitario']
    pyautogui.write(str(preco_unitario))
    pyautogui.press('tab')

    ## custo
    custo = tabela.loc[linha, 'custo']
    pyautogui.write(str(custo))
    pyautogui.press('tab')

    ## obs
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)
    pyautogui.press('tab')

    pyautogui.press('enter') ## enviar

    ## numero positivo = scroll para cima
    ## numero negativo = scroll para baixo
    pyautogui.scroll(10000)