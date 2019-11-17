import numpy as np
import os

def loadTrainingData(fileName = 'training_data.npy'):
	print('Loading Training Data...')
	if os.path.isfile(fileName):
		print('FILEMANAGER: File Exists.')
		print('FILEMANAGER: Loading data...')
		trainingData = list(np.load(fileName, allow_pickle=True))
	else:
		print('FILEMANAGER: File Does Not Exist.')
		print('FILEMANAGER: Starting Fresh...')
		trainingData = []
	return trainingData