import threading
import time

dato = 0

lectores_activos = 0;
escribiendo = False;

cond = threading.Condition();

def lector(id) :
    global lectores_activos;

    with cond:
        while escribiendo:
            cond.wait();

        lectores_activos += 1;

    print(f"Lector {id} lee dato = {dato}")

    time.sleep(0.5);

    with cond:
        lectores_activos -= 1;
    
        if lectores_activos == 0:
            cond.notify_all();


