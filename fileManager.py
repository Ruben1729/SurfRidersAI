import numpy as np
import os

fileName = 'training_data.npy'

if os.path.isfile(fileName):
	print('FILEMANAGER: File Exists.')
	print('FILEMANAGER: Loading data...')
	trainingData = list(np.load(fileName))
else:
	print('FILEMANAGER: File Does Not Exist.')
	print('FILEMANAGER: Starting Fresh...')
	trainingData = []