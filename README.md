# SurfRidersAI
Collection of python scripts that were used to build a convolutional neural network capable of playing SurfRiders AI by itself.

I wasn't able to include the file with the actual trained neural network on this project due to it being too heavy so in order for you to test it out you have to do the following:

- run trainModel.py
- wait for the training of the model to be done
- run main.py

Sadly, I believe this neural net will only work with display similar to mine given that I used my own display to train the model. If it doesn't work on your display I suggest you get your own training. This is a bit harder as you do have to get the right zone you want to record. You can find these params in recordTraining.py.

Once that's done do the following steps:

- run recordTraining.py (You probably will need 6000 frames or more worthy of data for the bot to perform properly)
- run processData.py
- run trainModel.py
- run main.py

If you have any questions feel free to hit me up!
