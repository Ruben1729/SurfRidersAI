import numpy as np
from PIL import ImageGrab
import cv2

def cap_screen():
	screen = np.array(ImageGrab.grab(bbox = (390, 157, 1515, 1019)))
	return cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)



while(True):

	cv2.imshow('window', cap_screen())
	if cv2.waitKey(25) & 0xFF == ord('q'):
		cv2.destroyAllWindows()
		break