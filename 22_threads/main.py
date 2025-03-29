from time import sleep

print("Main thread started")


def function1():
    print("Function 1 started")
    sleep(2)  # Main thread will be blocked for 2 seconds


def function2():
    print("Function 2 started")
    sleep(4)  # Main thread will be blocked for 3 seconds


function1()
function2()

# esto hace que no avance hasta q finalizen
# thread1.join()

print("Both functions have finished")
