import aiohttp
import asyncio
from bs4 import BeautifulSoup
import pandas as pd
import json

async def carrega_pagina(page): 
    try: 
        link  = f'http://localhost:4910/api/{page}'
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as response:
                html = await response.text()
                cont = str(BeautifulSoup(html, 'html.parser'))

                if not verifica_vazio(cont):
                    arr_cont = pd.DataFrame(json.loads(cont))
                    return arr_cont
                else:
                    return False
    except aiohttp.ClientError:
        return False

def verifica_vazio(conteudo):
    if json.loads(conteudo) == []:
        return True  # Indica que a página está vazia
    return False

async def stream_pagina():
    page = 1
    while True:
        print(f"Pagina {page}")

        result = await carrega_pagina(page)
        if result is False:
            break  # Se a página for vazia ou erro, parar o loop
        yield result
        page += 1

def ordena(list_num): #Ordena a lista
    if len(list_num) > 1:
        meio = len(list_num) // 2
        esquerda = list_num[:meio]
        direita = list_num[meio:]

        # chamada recursiva de cada metade da lista
        ordena(esquerda)
        ordena(direita)
        i = 0 # variaveis para percorrer os vetores
        j = 0
        k = 0
        
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] <= direita[j]:
              list_num[k] = esquerda[i]
              i += 1

            else:
                list_num[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            list_num[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            list_num[k]=direita[j]
            j += 1
            k += 1
    return list_num

    

async def main():
    async for data in stream_pagina():
        print(data)  # Aqui você pode processar os dados conforme necessário

if __name__ == "__main__":
    asyncio.run(main())
