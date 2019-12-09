import threading
import time
import datetime

def threadf(name):
    hours = []
    while(True):
        time.sleep(15)
        now = datetime.datetime.now()
        if (len(hours) == 0):
            hours.append(now)
            print(now.hour)
        elif (now.hour != hours[-1].hour):
            hours.append(now)
            print(now.hour)


if __name__ == "__main__":
    print("Starting Program")
    x = threading.Thread(target=threadf, args=(1,))
    x.start()