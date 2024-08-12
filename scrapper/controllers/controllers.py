from services.services import ScraperService

class ScraperController:
    def __init__(self):
        self.service = ScraperService()

    async def scrape_and_store(self):
        await self.service.stream_paginas()

    def get_sorted_numeros(self, page, per_page):
        return self.service.repo.get_numeros(page, per_page)
