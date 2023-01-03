import time

def messageloop(counter):
    print(f"Sending message number {counter}.")


if __name__=="__main__":
    counter =1
    while True:
        messageloop(counter)
        counter += 1
        time.sleep(2)