import threading
def print_numbers():
    for i in range(1,6):
        print(threading.current_thread().name,i)

thread1=threading.Thread(target=print_numbers,name='Thread-1')
thread1.start()
thread1.join()
thread2=threading.Thread(target=print_numbers,name='Thread-2')
thread2.start()

thread2.join()
print("Mutltithreading is completed")
