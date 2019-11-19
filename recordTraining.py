import numpy as np
import time
import os

from keyListener import keyListener, processKeys
from pynput.keyboard import Key, Controller

import cv2
# from screen import cap_screen
from screen import processFrame
from PIL import ImageGrab

from fileManager import loadTrainingData

# Countdown
print('Beginning Countdown...')

for i in list(range(4))[::-1]:
	print(i+1)
	time.sleep(1)

print('Countdown Finished...')

def recordTrainingData():
	# Loading Files
	fileName = 'training_data.npy'
	trainingData = loadTrainingData(fileName)

	# Loop
	lastTime = time.time();
	while(True):
		screen = np.array(ImageGrab.grab(bbox = (200, 400, 1500, 1100)))
		screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
		screen = cv2.resize(screen, (80, 60))

		# Process Keys
		keys = keyListener()
		output = processKeys(keys)
		trainingData.append([screen, output])
		print(len(trainingData))
		print('Frame took {} seconds'.format(time.time()-lastTime))

		lastTime = time.time()

		if cv2.waitKey(25) & 0xFF == ord('q'):
			cv2.destroyAllWindows()
			break

		if len(trainingData) % 500 == 0:
			print('You have {} frames in your training data'.format(len(trainingData)))
			np.save(fileName, trainingData)

recordTrainingData()