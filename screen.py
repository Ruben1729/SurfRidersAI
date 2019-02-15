import numpy as np
from PIL import ImageGrab
import cv2

def cap_screen():#610, 357, 1350, 1019
	screen = np.array(ImageGrab.grab(bbox = (1100, 636, 1303, 813)))
	processed_screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)#makes it easier to manipulate data
	return processed_screen
	#813px down is the main white line
	#168px from top reg to bottom top
	#80px of distance between top and bottom
	#89px of distance between top to top