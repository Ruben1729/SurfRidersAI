import numpy as np
from PIL import ImageGrab
import cv2

while(True):
	screen = np.array(ImageGrab.grab(bbox = (390, 157, 1515, 1019)))

	cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
	if cv2.waitKey(25) & 0xFF == ord('q'):
		cv2.destroyAllWindows()
		break
