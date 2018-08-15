import sys, termios, tty, os, time, threading


button_delay = 0.2
gesture = 0
qPressed = False # capitalize in python!
count = 0


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
 
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
 

def keys():
    global gesture
    global qPressed
    global count

    while True:
        char = getch()
 
        if (char == "q"):
            print("Quit!")
	    qPressed = True
            exit(0)
 
        if (char == "0"):
	    gesture = 0
            count = gesture
            print("Gesture = 0")
            time.sleep(button_delay)
 
        elif (char == "1"):
	    gesture = 1
	    count = gesture
            print("Gesture = 1")
            time.sleep(button_delay)
 
 
        elif (char == "2"):
	    gesture = 2
	    count = gesture
            print("Gesture = 2")
            time.sleep(button_delay)


def counter():
    global qPressed
    global count

    while (count < 50 and qPressed != True):
	print("count: " + str(count))
	count +=1 
	time.sleep(1)



#if __name__ == "__main__":
	    

keyboard = threading.Thread(target = keys)
counter = threading.Thread(target = counter)

keyboard.start()
counter.start()

keyboard.join()
counter.join()
 




