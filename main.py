import numpy as np
import time
import os

from keyListener import keyListener, processKeys
from pynput.keyboard import Key, Controller

import cv2
from screen import processFrame
from PIL import ImageGrab

from fileManager import loadTrainingData

from alexnet import alexnet, alexnet2, customnet

WIDTH = 80
HEIGHT = 60
LR = 1e-3
EPOCHS = 8
MODELNAME = 'surfrider-{}-{}-{}-epochs'.format(LR, 'customnet', EPOCHS)

model = customnet(WIDTH, HEIGHT, LR)
model.load(MODELNAME)

keyboard = Controller()

# Countdown
print('Beginning Countdown...')

for i in list(range(4))[::-1]:
	print(i+1)
	time.sleep(1)

print('Countdown Finished...')

#main function
def main():
	paused = False
	lastTime = time.time();
	while(True):
		if not paused:
			screen = np.array(ImageGrab.grab(bbox = (200, 400, 1500, 1100)))
			screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
			screen = cv2.resize(screen, (80, 60))

			print('Frame took {} seconds'.format(time.time()-lastTime))
			lastTime = time.time()
			print('============================================')
			prediction = model.predict([screen.reshape(WIDTH,HEIGHT,1)])[0]
			print(prediction)

			threshHold = .75

			if prediction[0] > threshHold:
				keyboard.press('w')
				keyboard.release('w')
			elif prediction[1] > threshHold:
				keyboard.press('s')
				keyboard.release('s')

		keys = keyListener()
		if 'P' in keys:
			if paused:
				paused = False
				time.sleep(1)
			else:
				paused = True
				keyboard.release('s')
				keyboard.release('w')
				time.sleep(1)

		if cv2.waitKey(25) & 0xFF == ord('q'):
			cv2.destroyAllWindows()
			break

main()