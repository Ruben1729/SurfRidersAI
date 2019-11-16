import win32api as wapi
import time

keyList = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'APS$/\\":
	keyList.append(char)

# Listens for key presses
def keyListener():
	keys = []
	for key in keyList:
		if wapi.GetAsyncKeyState(ord(key)):
			keys.append(key)
	return keys

# We only care about [W,S]
def processKeys(keys):
	output = [0, 0]

	if 'W' in keys:
		output[0] = 1
	elif 'S' in keys:
		output[1] = 1

	return output