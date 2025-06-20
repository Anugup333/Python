import threading
import time

def print_numbers():
    for i in range(1,6):
        print(f"Number: {i}")
        time.sleep(1)
        
def print_letters():
    for i in "abcde":
        print(f"Letters {i}")
        time.sleep(1)

thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# start Thread
thread1.start()
thread2.start()

# wait for both threads to finish

thread1.join()
thread2.join()

print("Both threads Finnished execution ")