import aiohttp
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

    async def stream_paginas(self):
        page = 1
        while True:
            numeros = await self.carrega_pagina(page)
            if not numeros:
                break
            self.repo.add_numeros(numeros)
            page += 1

    def salvar_em_json(self):
        # Ordena os números e salva em JSON
        numeros_ordenados = self.repo.ordena_numeros()
        self.repo.salvar_em_json(numeros_ordenados)
