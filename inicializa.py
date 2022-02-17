import threading
import os
import time
import apiRest as ar
import loadPage as lp
    
def inicia_programa():
    os.system('python3 -m pip install -r {}'.format('libs.txt'))
    os.system('python -m pip install -r {}'.format('libs.txt'))
    with open('libs.txt','a') as f:
        f.write('\n')
        f.write('#instalados#')


def instaled():
    inst = '#instalados#'
    Ok = False
    with open('libs.txt','r') as f:
        txt = f.readlines()
    
    for i in txt:
        if i == inst:
            Ok = True
    if Ok:
        main()
    else:
        inicia_programa()
        main()

def main():
    processos = []

    processos.append(threading.Thread(target=lp.load))
    processos[-1].start()
    time.sleep(4)
    
    # processos.append(threading.Thread(target=ar.apiRest.run(debug=True)))
    # processos[-1].start()

    for processo in processos:
        processo.join()

if __name__ == "__main__": 
    instaled()
    #main()