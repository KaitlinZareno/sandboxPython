# -*- python-indent-offset: 4; -*-

# Description: Plays back a gesture on motors when pigeon detected in
# camera images.
# Author: Ian Ingram

#import cv2
import thread
import globals  #this is where the variables shared between the threads are; excepting, for now, targetDetected and captureAndRecord
from gestureFunctions import gestureController
#import detector as dt
import time
import argparse

import sys, termios, tty, os, threading, random

# global variables
keyPressed = False
qPressed = False
latch = False
num = 3

# argument handling
parser = argparse.ArgumentParser()
parser.add_argument(
    '-c',
    '--camera',
    type=int,
    default='0',
    help='Number of camera to use.'
)

parser.add_argument(
    '-v',
    '--videoname',
    type=str,
    default='defaultOutputVideo',
    help='Name for file to save video to.'
)

#args = parser.parse_args()
# end argument handling

#targetDetected = False

#CAMERA_PORT = args.camera
#MOVIES_SAVE_FOLDER = 'linkToMovies_DetectionBasedGestureSwitching/' 
#OUTPUT_VIDEO_NAME =  MOVIES_SAVE_FOLDER + args.videoname + '.avi'
#OUTPUT_LOGFILE_NAME = MOVIES_SAVE_FOLDER + args.videoname + '.txt'

#cap = cv2.VideoCapture(CAMERA_PORT)
#if (cap.isOpened() == False): 
    #print("Unable to read camera feed")
#ret = cap.set(3,1920);
#ret = cap.set(4,1080);
    
#ret, frame = cap.read()

def captureAndRecord():
    global cap
    global frame

    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    #print(int(cap.get(5)))
    
    # Define the codec and create VideoWriter object.
    frameRate = 30 #15
    #out = cv2.VideoWriter(OUTPUT_VIDEO_NAME,cv2.cv.CV_FOURCC(*'MJPG'), frameRate, (frame_width,frame_height))

   # frame_Smaller = cv2.resize(frame, (640, 360))
    #cv2.imshow('frame',frame_Smaller)
    #cv2.moveWindow('frame', 20,20)
            
    while(True):
        #ret, frame = cap.read()
 
        if ret == True: 
     
            # Write the frame into the file 'output.avi'
            #out.write(frame)
           # frame_Smaller = cv2.resize(frame, (640, 360))
            #cv2.imshow('frame',frame_Smaller)
            #k = cv2.waitKey(1) & 0xff
            if k == 27:  # ESC to quit
                break
        else:
            break 
 
    # When everything done, release the video capture and video write objects
   # cap.release()
    #out.release()
 
    # Closes all the frames
    #cv2.destroyAllWindows() 


def targetDetect():
    #logFile = open(OUTPUT_LOGFILE_NAME,'w')

    global targetDetected

    #targetDetected = True

    #global frame
   # dt.initialize()
    #programStartTime = time.time()
    
    #while(1):
       # start = time.time() # want to time each cycle. starting stopwatch.
        
        #file = "test_image.png"
        #cv2.imwrite(file, frame)
        #vote, target_label = dt.detect('test_image.png')
        #if vote == True:
           # targetDetected = True
           # detectionTime = time.time() - programStartTime
           # logFile.write('Detection: ' + target_label + ' at ' + ('%.2f' % detectionTime) + '\n') 
        #else:
          #  targetDetected = False

        #print(target_label + ' is present.\n')
        
        #end = time.time()
        #print('Elapsed Time for Target Detector: ' + str(end - start)) # print out how long this detection cycle took
                            
        #print('********')
    #logFile.close()

def updateGesture():

# PLUG INTO PIN 13

    global targetDetected
    global latch
    global keyPressed
    global qPressed
    global num

    targetDetected = True

    startFrame = globals.frameCounter
    lengthReactionGesture = 190  #IMPORTANT: THIS HAS TO MATCH OR
                                 #THINGS WON'T WORK AS EXPECTED --> potential bug...??

    while(1):
        if targetDetected == True:
#and latch == False: # latch starts gesture updating
           # latch = True 
            startFrame = globals.frameCounter
            globals.newGesture= 0 #random.randint(0,2) # = 0
            #globals.newGesture= 0 #random.randint(0,2) # = 0
	    if keyPressed == True:
		if num == 0: globals.newGesture = 0
		if num == 1: globals.newGesture = 1
		if num == 2: globals.newGesture = 2

	    
	    else: 
		globals.newGesture= 0 #random.randint(0,2) # = 0
	


        elapsedFrames = globals.frameCounter - startFrame

        if elapsedFrames >= lengthReactionGesture:
            #latch = False
            globals.newGesture = 0 #random.randint(0,2)
	    

	if qPressed == True:
	    exit(0)

# 1 : once gesture 0 is done playing, 1 will play

# COMMENTED CODE INCREMENTS TO NEXT GESTURE WHEN TARGET DETECTED
#        if targetDetected == True and latch == False:
#            latch = True
#            #print "incrementing to next gesture"
#            if(globals.currentGesture < 2):
#                globals.newGesture = globals.currentGesture + 1
#            else:
#                globals.newGesture = 0
#        elif targetDetected == False and latch == True:
#            latch = False



################################################################################################
#Key Pressed Implementation 

# maybe can have keyPressed global variable that if key pressed, can run through 

button_delay = 0.2

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
    global keyPressed
    #global latch
    global qPressed
    global num

    while True:
        char = getch()
 
        if (char == "q"):
            print("Quit!")
	    qPressed = True

            exit(0)
 
# if 0 is pressed, gesture 0 will play 
#elapsed frames is reset to 0

        if (char == "0"):
	    #latch = True
	    keyPressed = True
	    num = 0
	    #startFrame = globals.frameCounter
           # globals.newGesture = 0
            print("Gesture = 0")
            time.sleep(button_delay)
 
        elif (char == "1"):
	   # latch = True
	    keyPressed = True
 	   # startFrame = globals.frameCounter
	    #globals.newGesture = 1
	    num = 1
	   # count = gesture
            print("Gesture = 1")
            time.sleep(button_delay)
 
 
        elif (char == "2"):
	    #latch = True
	    keyPressed = True
 	    #startFrame = globals.frameCounter
	    #globals.newGesture = 2
	    num = 2
	    #count = gesture
            print("Gesture = 2")
            time.sleep(button_delay)


################################################################################################
                
def main():
    try:
       # thread.start_new_thread(captureAndRecord, () )
       # thread.start_new_thread(targetDetect, () )
        thread.start_new_thread(updateGesture, () )
        thread.start_new_thread(gestureController, () )

	thread.start_new_thread(keys, () )

# cam maybe create thread in gestureFunctions.py and import it like gestureController() was imported
# create function in gestureFunctions due to main overlap with gesture switching
# or update in updateGesture()
    except:
        print "Error: unable to start thread"
        
    while 1:
        pass

if __name__ == "__main__":  
    main()  
