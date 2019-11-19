import numpy as np
from alexnet import alexnet2, alexnet, customnet

WIDTH = 80
HEIGHT = 60
LR = 1e-3
EPOCHS = 8
MODELNAME = 'surfrider-{}-{}-{}-epochs'.format(LR, 'customnet', EPOCHS)

model = customnet(WIDTH, HEIGHT, LR)
trainData = np.load('training_data_v2.npy', allow_pickle=True)

train = trainData[:-500]
test = trainData[-500:]

X = np.array([i[0] for i in train]).reshape(-1,WIDTH,HEIGHT,1)
Y = [i[1] for i in train]

test_x = np.array([i[0] for i in test]).reshape(-1,WIDTH,HEIGHT,1)
test_y = [i[1] for i in test]

model.fit({'input': X}, {'targets': Y}, n_epoch=1, validation_set=({'input': test_x}, {'targets': test_y}), 
    snapshot_step=2500, show_metric=True, run_id=MODELNAME)

# tensorboard --logdir=foo:C:/Users/Ruben/OneDrive/Desktop/Github/SurfRidersAI/log

model.save(MODELNAME)