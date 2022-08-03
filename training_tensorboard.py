import tensorflow.keras.callbacks

print('Setting UP')
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from sklearn.model_selection import train_test_split
from utlis_tensorboard import *

#### STEP 1 - INITIALIZE DATA
path = 'DataCollected'
data = importDataInfo(path)
print(data.head())

#### STEP 2 - VISUALIZE AND BALANCE DATA
data = balanceData(data,display=True)

#### STEP 3 - PREPARE FOR PROCESSING
imagesPath, steerings = loadData(path,data)
# print('No of Path Created for Images ',len(imagesPath),len(steerings))
# cv2.imshow('Test Image',cv2.imread(imagesPath[5]))
# cv2.waitKey(0)

#### STEP 4 - SPLIT FOR TRAINING AND VALIDATION
xTrain, xVal, yTrain, yVal = train_test_split(imagesPath, steerings,
                                              test_size=0.2,random_state=10)
print('Total Training Images: ',len(xTrain))
print('Total Validation Images: ',len(xVal))

#### STEP 5 - AUGMENT DATA

#### STEP 6 - PREPROCESS

#### STEP 7 - CREATE MODEL
model = createModel()

tb_callback = tensorflow.keras.callbacks.TensorBoard('./logs30_500_001(2)', update_freq=1)

#checkpoint_filepath = './tmp/checkpoint'
#model_checkpoint_callback = tensorflow.keras.callbacks.ModelCheckpoint(
        #filepath=checkpoint_filepath,
        #save_weights_only=True,
        #monitor='val_loss',
        #mode='max',
        #save_best_only=True)

csv_logger = tensorflow.keras.callbacks.CSVLogger('traininglog30_500_001(2).log')

#### STEP 8 - TRAINNING
#model.load_weights(checkpoint_filepath)
history = model.fit(dataGen(xTrain, yTrain, 100, 1),
                                  steps_per_epoch=500,
                                  epochs=30,
                                  validation_data=dataGen(xVal, yVal, 50, 0),
                                  validation_steps=60,
                                  callbacks=[tb_callback, csv_logger])



#### STEP 9 - SAVE THE MODEL
model.save('model30_500_001(2).h5')
print('Model Saved')

#### STEP 10 - PLOT THE RESULTS
