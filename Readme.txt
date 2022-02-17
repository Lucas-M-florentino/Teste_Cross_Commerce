### Programa feito por Lucas Matheus de Moraes Florentino ####

Programa feito em python, com o intuito de solucionar o teste de ETL Cross Comerce, com paralelismo multithreading 
para uma busca mais rápida dos dados.

para rodar o Programa é necessário ter o python instalado na máquina

para ver somente os resultados rode o programa apiRest.py e abra no navegador http://127.0.0.1:5000/ para verificar os dados

para iniciar toda etapa de ETL utilize o programa inicializa.py 
para rodar no computador pessoal já existe uma configuração automática de instalação de bibliotecas necessárias em libs.txt,

caso ocorra algum erro por falta de biblioteca rode o seguinte comando com terminal ou CMD na pasta do programa: python -m pip install -r libs.txt,

se for rodar o programa em um ambiente online como repl.it que já baixa as bibliotecas automaticamente 
editar no inicializa.py em if __name__ == "__main__": comentar o instaled() e descomentar o #main()

após rodar o programa, abrir no navegador http://127.0.0.1:5000/ e aguardar as informações serem carregadas, enquanto o programa carrega
mensagens serão carregadas em cada passo que o programa está em andamento