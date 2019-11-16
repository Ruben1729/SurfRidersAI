import numpy as np
from alexnet import alexnet

WIDTH = 80
HEIGHT = 60
LR = 1e-3
EPOCHS = 8
MODELNAME = 'surfrider-{}-{}-{}-epochs'.format(LR, 'alexnet', EPOCHS)

model = alexnet(WIDTH, HEIGHT, LR)

np_load_old = np.load
np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)
trainData = np.load('training_data.npy')
np.load = np_load_old

train = trainData[:-100]
test = trainData[-100:]

X = np.array([i[0] for i in train]).reshape(-1,WIDTH,HEIGHT,1)
Y = [i[1] for i in train]

test_x = np.array([i[0] for i in test]).reshape(-1,WIDTH,HEIGHT,1)
test_y = [i[1] for i in test]

model.fit({'input': X}, {'targets': Y}, n_epoch=1, validation_set=({'input': test_x}, {'targets': test_y}), 
    snapshot_step=2500, show_metric=True, run_id=MODELNAME)

# tensorboard --logdir=foo:C:/Users/Ruben/OneDrive/Desktop/Github/SurfRidersAI/log

model.save(MODELNAME)