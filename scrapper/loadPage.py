from ast import arg
from pydoc import doc
from bs4 import BeautifulSoup
import requests
import threading as th
import time
import apiRest as ar

def carregaPagina(page): # carrega a informação da página
    var = -1
    while var !=1:
        try: 
            link  = 'http://localhost:4910/api/'+str(page)
            html = requests.get(link).content
            cont = str(BeautifulSoup(html, 'html.parser'))
            var = 1
        except requests.exceptions.RequestException:
            var =0
            time.sleep(0.2)
    
    return cont

def verificaVazio(conteudo):   # verifica se a página e vazia
    condicao_atual = conteudo.split('[')[-1] 
    if condicao_atual[0]==']':
        return False #condição de sair
    else:
        return True #condição de continuar buscando

def localUltimaPag(pag,param): # localiza ultima página para saber quantas são
    page = pag
    par = param
    
    while verificaVazio(carregaPagina(page)) == verificaVazio(carregaPagina(page+1)):
        while verificaVazio(carregaPagina(page)):
            
            page+=par

        page = page - par
        par = par/10
    return int(page)
    
def Ordena(listNum): #Ordena a lista
    if len(listNum) > 1:
        meio = len(listNum) // 2
        esquerda = listNum[:meio]
        direita = listNum[meio:]

        # chamada recursiva de cada metade da lista
        Ordena(esquerda)
        Ordena(direita)
        i = 0 # variaveis para percorrer os vetores
        j = 0
        k = 0
        
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] <= direita[j]:
              listNum[k] = esquerda[i]
              i += 1

            else:
                listNum[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            listNum[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            listNum[k]=direita[j]
            j += 1
            k += 1

class MinhaThread(th.Thread): #classe que constroi thread para percorrer as páginas e baixar os números
    
    def __init__(self,thrId,inicio,fim,mtx): 
        self.thrId = thrId
        self.inicio = inicio
        self.fim = fim
        self.mtx = mtx
        th.Thread.__init__(self)

    def run(self): # metodo que atribui as partes para cada thread buscar
        global listaNumeros
        global visitPag
        for i in range(self.inicio,self.fim):
            
            listaNumeros[i-1] = carregaPagina(i).split('[')[-1].split(']')[0].split(',')
            visitPag[i-1] = i
            time.sleep(0.2)
            

def load(): # função principal para gerenciar a verificação e salva de numeros
    inicio = 1
    global listaNumeros
    global visitPag
    global vlistOrdena
    
    mutex = th.Lock()
    tot = 8 # numero de threads
    listaFinal = ['']
    vthreads =[]
    html = ['<html><head><html lang="pt-br"><meta http-equiv="refresh" content="60";url=index.php><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Lucas Florentino - Teste Cross Commerce</title></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">"']
    html.append('"</pre></body></html>')
    print('Contando Paginas...')
    txt='Contando Paginas...'
    msg=html[0]+txt+html[1]
    with open('index.html','w',encoding='utf-8') as f:
        f.write(msg)
    
    page = localUltimaPag(inicio,1000)# buscar a ultima página com numeros para total de paginas com parametro de busca para ir mais rápido
    sizePag = len(carregaPagina(1).split('[')[-1].split(']')[0].split(','))
    
    listaNumeros = [['']]*page
    visitPag = [0]*page
    s = page//tot # quantidade para cada thread
    p= [1] # primeiro começa em 1
    for i in range(1,tot+1):
        p.append(s*i)
    p[-1] =  p[-1]+1

    print('Buscando numeros...')
    txt='Buscando numeros... '
    msg=html[0]+txt+html[1]
    with open('index.html','w',encoding='utf-8') as f:
       f.write(msg)
    
    for i in range(tot):
        vthreads.append(MinhaThread(i,p[i],p[i+1],mutex))
        vthreads[-1].start()

    for i in vthreads:
        i.join()
    
    a=0 #auxiliares para calculos
    b=0
    if page/tot > page//tot: #verifica se sobraram paginas sem coletar informações
        a = page//tot
        b = page - (tot*a)
        print("Acrescentando as ",b," paginas restantes...")
        txt='Acrescentando as '+b+' paginas restantes...'
        msg=html[0]+txt+html[1]
        with open('index.html','w',encoding='utf-8') as f:
            f.write(msg)

        rest = MinhaThread(1,tot*a,page,mutex)
        rest.start()
        rest.join()

    for i in listaNumeros:
        listaFinal = listaFinal + i
    listaFinal.pop(0)
    vthreads.clear()

    Ordena(visitPag)

    print('Ordenando...')
    txt='Ordenando... '
    msg=html[0]+txt+html[1]
    with open('index.html','w',encoding='utf-8') as f:
        f.write(msg)
    
    Ordena(listaFinal)
    
    txt = ''
    for i in listaFinal:
        if listaFinal[-1] != i:
            txt = txt + i + ','
        else:
            txt = txt + i
    
    html[0] = '<html><head><html lang="pt-br"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Lucas Florentino - Teste Cross Commerce</title></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">"'
    msg=html[0]+'{Numeros ordenados: ['+txt+']}'+html[1]
    with open('index.html','w',encoding='utf-8') as f:
        f.write(msg)
    
if __name__ == '__main__':
    load()