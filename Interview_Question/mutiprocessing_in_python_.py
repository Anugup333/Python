import multiprocessing
import time

def calculate_square(numbers):
    for n in numbers:
        time.sleep(1)
        print(f"Square: {n * n}")

def calculate_cube(numbers):
    for n in numbers:
        time.sleep(1)
        print(f"Cube: {n * n * n}")

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    
    # Creating processes
    process1 = multiprocessing.Process(target=calculate_square, args=(numbers,))
    process2 = multiprocessing.Process(target=calculate_cube, args=(numbers,))
    
    # Starting processes
    process1.start()
    process2.start()
    
    # Wait for processes to finish
    process1.join()
    process2.join()
    
    print("Both processes finished execution")
