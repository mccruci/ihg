from . import connessione
import time
import multiprocessing

"""
1- connessione ai device
2- start ciclo
3- acquisizione dati
4- elaborazione dati
5- riprendo il punto 2 
"""
if __name__ == '__main__':

    NUM_WORKERS = 4
    start_time = time.time()

    #PUNTO 1
    #listaIP = connessione.findIp()
    device = []
    for ip in connessione.findIp():
        d = connessione.Connessione(ip)
        d.connectKinseiClient()
        device.append(d)

    #PUNTO 2
    with multiprocessing.Pool(processes=NUM_WORKERS) as pool:
        with True:
            #PUNTO 3
            results = pool.map_async(connessione.acquisizione, device)
            results.wait()

    end_time = time.time()

    print("Time for MultiProcessing: %ssecs" % (end_time - start_time))




