from itertools import cycle
from threading import Event, Lock, Thread

lock = Lock()
event = Event()  # False
count = 0


def waiting_for():
    print("Comenzamos los depositos y balances...")
    # in cycle(r'-\|/-'), r is for raw string
    for c in cycle(r'-\|/-'):
        print(c, end="\r", flush=True)  # \r es para que se imprima en la
        if event.wait(0.1):
            break
    print("El balance final es:", count)


def deposit():
    global count

    for x in range(10_000_000):
        lock.acquire()
        count += 1
        lock.release()


def withdraw():
    global count

    for x in range(10_000_000):
        lock.acquire()
        count -= 1
        lock.release()


t1 = Thread(target=deposit)
t2 = Thread(target=withdraw)
t3 = Thread(target=waiting_for)

t1.start()
t2.start()
t3.start()
t1.join()
t2.join()

event.set()  # Verdadero
t3.join()
