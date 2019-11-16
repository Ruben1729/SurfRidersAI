import numpy as np
import time
import os

from getKeys import keyListener
from getKeys import processKeys

import cv2
# from screen import cap_screen
from screen import processFrame
from PIL import ImageGrab


# Loading Files
print('Loading Training Data...')

fileName = 'training_data.npy'

if os.path.isfile(fileName):
	print('FILEMANAGER: File Exists.')
	print('FILEMANAGER: Loading data...')
	np_load_old = np.load
	np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)
	trainingData = list(np.load(fileName))
	np.load = np_load_old
else:
	print('FILEMANAGER: File Does Not Exist.')
	print('FILEMANAGER: Starting Fresh...')
	trainingData = []

# Countdown
print('Beginning Countdown...')

for i in list(range(4))[::-1]:
	print(i+1)
	time.sleep(1)

print('Countdown Finished...')

# Main
lastTime = time.time();
while(True):
	screen = np.array(ImageGrab.grab(bbox = (200, 400, 1500, 1100)))
	screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
	screen = cv2.resize(screen, (80, 60))

	keys = keyListener()
	output = processKeys(keys)
	trainingData.append([screen, output])
	# new_screen = processFrame(screen)

	print('Frame took {} seconds'.format(time.time()-lastTime))

	lastTime = time.time()
	# cv2.imshow('window', new_screen)

	if cv2.waitKey(25) & 0xFF == ord('q'):
		cv2.destroyAllWindows()
		break

	if len(trainingData) % 500 == 0:
		print(len(trainingData))
		np.save(fileName, trainingData)