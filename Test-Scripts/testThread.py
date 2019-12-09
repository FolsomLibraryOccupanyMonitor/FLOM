import threading
import time


def threadf(name):
	print("Thread %s: starting thread",name)
	x = 0
	while(1):
		time.sleep(1)
		s = "Thread " + str(x)
		print(s)
		x = x + 1

if __name__ == "__main__":
	print("Starting Program")
	x = threading.Thread(target=threadf, args=(1,))
	x.start()
	y = 0
	while(1):
		time.sleep(2)
		s = "Main: " + str(y)
		print(s)
		y = y + 1

