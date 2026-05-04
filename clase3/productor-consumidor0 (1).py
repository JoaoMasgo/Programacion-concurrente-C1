import threading
import time

buffer = []
MAX = 3
cond = threading.Condition()

def productor():
    for i in range(10):            
        buffer.append(i)
        print(f"\033[92mProduce {i} | Buffer: {buffer}\033[0m")
        time.sleep(1)

def consumidor():
    for i in range(10):           
        item = buffer.pop(0)
        print(f"\033[91mConsume {item} | Buffer: {buffer}\033[0m")        
        time.sleep(2)

t1 = threading.Thread(target=productor)
t2 = threading.Thread(target=consumidor)

t1.start()
t2.start()

t1.join()
t2.join()