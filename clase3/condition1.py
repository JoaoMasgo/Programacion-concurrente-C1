import threading

cond = threading.Condition()
dato = None

def productor():
    global dato
    with cond:
        dato = "comida lista"
        cond.notify()

def consumidor():
    with cond:
        cond.wait()
        print("Recibi", dato)

#notify() no garantiza despertar al hilo correcto;
# por eso se usa while para verificar la condición y, 
# en casos con varios tipos de espera, puede convenir notify_all().

#Se utiliza while junto con wait() para volver a verificar la condición tras despertarse,
#  ya que el despertar no garantiza que la condición sea verdadera.