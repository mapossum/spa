import time

def countdown():
    for i in range(10, 0, -1):
        print(i)
        time.sleep(1)

    print("Blastoff!")
  
countdown()
