import aiohttp
import json
from repositories.repositories import NumeroRepository

class ScraperService:
    def __init__(self):
        self.repo = NumeroRepository()

    async def carrega_pagina(self, page):
        link = f'http://localhost:4910/api/{page}'
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as response:
                numeros = await response.json()
                print(f"[DEBUG] Página {page}: {numeros}")  # Debug: Verificando os dados recebidos
                return numeros
    
    def salvar_em_json(self, numeros):
        with open('database/numeros_ordenados.json', 'w') as f:
            json.dump(numeros, f)

    def ordenar_e_salvar(self, numeros):
        numeros_ordenados = sorted(numeros)
        self.salvar_em_json(numeros_ordenados)
    
    async def stream_paginas(self):
        page = 1
        todos_numeros = []
        while True:
            numeros = await self.carrega_pagina(page)
            if not numeros:
                break
            todos_numeros.extend(numeros)
            page += 1
        self.ordenar_e_salvar(todos_numeros)
