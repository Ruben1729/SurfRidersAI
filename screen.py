import numpy as np
from PIL import ImageGrab
import cv2

while(True):
	printscreen_pil = ImageGrab.grab(bbox = (390, 157, 1515, 1019))

	cv2.imshow('window', np.array(printscreen_pil))
	if cv2.waitKey(25) & 0xFF == ord('q'):
		cv2.destroyAllWindows()
		break
