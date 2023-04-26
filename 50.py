import threading

def even():
    for i in range(0,21,2):
        print(i)

def odd():
    for i in range(1,21,2):
        print(i)

t1=threading.Thread(target=even())
t2=threading.Thread(target=odd())

t1.start()
t2.start()
t2.join()

t1.join()

