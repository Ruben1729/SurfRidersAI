import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle
import cv2

np_load_old = np.load
np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)
trainData = np.load('training_data.npy')
np.load = np_load_old

print(len(trainData))

df = pd.DataFrame(trainData)
print(df.head())
print(Counter(df[1].apply(str)))

up = []
down = []
straight = []

shuffle(trainData)

for data in trainData:
	img = data[0]
	choice = data[1]

	if choice == [1,0]:
		up.append([img, choice])
	elif choice == [0,1]:
		down.append([img, choice])
	elif choice == [0,0]:
		straight.append([img, choice])
	else:
		print('No Match.')

straight = straight[:len(up)][:len(down)]
up = up[:len(straight)]
down = down[:len(down)]

finalData = straight + up + down

shuffle(finalData)
print(len(finalData))
np.save('training_data_v2.npy', finalData)