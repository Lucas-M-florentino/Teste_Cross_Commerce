import json
import os

class NumeroRepository:
    def __init__(self):
        self.numeros = []

    def add_numeros(self, numeros):
        self.numeros.extend(numeros)

    def ordena_numeros(self):
        return self.merge_sort(self.numeros)

    def merge_sort(self, list_num):
        if len(list_num) > 1:
            meio = len(list_num) // 2
            esquerda = list_num[:meio]
            direita = list_num[meio:]

            # Chamada recursiva em cada metade da lista
            self.merge_sort(esquerda)
            self.merge_sort(direita)

            i = 0  # Índice para percorrer o lado esquerdo
            j = 0  # Índice para percorrer o lado direito
            k = 0  # Índice para preencher a lista original

            while i < len(esquerda) and j < len(direita):
                if esquerda[i] <= direita[j]:
                    list_num[k] = esquerda[i]
                    i += 1
                else:
                    list_num[k] = direita[j]
                    j += 1
                k += 1

            # Preencher a lista com os elementos restantes
            while i < len(esquerda):
                list_num[k] = esquerda[i]
                i += 1
                k += 1

            while j < len(direita):
                list_num[k] = direita[j]
                j += 1
                k += 1

        return list_num

    def salvar_em_json(self, numeros_ordenados, arquivo='database/numeros_ordenados.json'):
        with open(arquivo, 'w') as f:
            json.dump(numeros_ordenados, f, indent=4)
        print(f"Números salvos em {arquivo}")
