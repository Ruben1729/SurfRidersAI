import numpy as np
from PIL import ImageGrab
import cv2

def cap_screen():#610, 357, 1350, 1019
	screen = np.array(ImageGrab.grab(bbox = (1100, 636, 1303, 813)))
	return processed_screen

def processFrame(original_frame):
	processed_frame = cv2.cvtColor(original_frame, cv2.COLOR_BGR2GRAY)
	processed_frame = cv2.Canny(processed_frame, threshold1 = 200, threshold2 = 300)
	processed_frame = cv2.GaussianBlur(processed_frame, (5, 5), 0)
	return processed_frame

def drawLines(img, lines):
	try:
		for line in lines:
			coords = line[0]
			cv2.line(img, (coords[0], coords[1]), (coords[2], coords[3]), [255, 255, 255], 3)
	except:
		pass