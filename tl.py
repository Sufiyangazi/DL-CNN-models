# -*- coding: utf-8 -*-
"""TL.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wHFI1HBUbbE-WnT5-cl_bcKVb7RS_0b6
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
import os

url = 'https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip'
zip_path = tf.keras.utils.get_file('cats_and_dogs',origin=url,extract=True)
file_path = os.path.join(os.path.dirname(zip_path),'cats_and_dogs_filtered')

train_dir = os.path.join(file_path,'train')
validation_dir = os.path.join(file_path,'validation')

train_dataset = tf.keras.utils.image_dataset_from_directory(train_dir,
                                                            shuffle=True,
                                                            batch_size=32,
                                                            image_size=(160,160))

validation_dataset = tf.keras.utils.image_dataset_from_directory(validation_dir,
                                                                 shuffle=True,
                                                                 batch_size=32,
                                                                 image_size=(160,160))

class_names = train_dataset.class_names
plt.figure(figsize=(15,15))
for image,labels in train_dataset.take(1):
  for i in range(20):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(image[i].numpy().astype('uint8'))
    plt.title(class_names[labels[i]])

"""- Check the number of batches
- divide the validation_dataset into test_dataset and validation set
- here we are taking 1/5th of data from the validation_dataset
- And update the validation dataset
"""

val_batches = tf.data.experimental.cardinality(validation_dataset)
test_dataset = validation_dataset.take(val_batches // 5)
validation_dataset = validation_dataset.skip(val_batches // 5)

"""- insted of writing tf.data.experimental.cardinality(validaton_dataset)
- you can simply get above answers by  using this codes:
- print('Number of validation batches',len(validation_dataset))
- print('Number of test batches',len(test_dataset))
"""

print('Number of validation batches : %d' % tf.data.experimental.cardinality(validation_dataset))
print('Number of test batches : %d' % tf.data.experimental.cardinality(test_dataset))

"""Configure the dataset for the performance"""

autotune = tf.data.AUTOTUNE

train_dataset = train_dataset.prefetch(buffer_size=autotune)
validation_dataset = validation_dataset.prefetch(buffer_size=autotune)
test_dataset = test_dataset.prefetch(buffer_size=autotune)

"""**Data Agumentation**
- use when image dataset is not large
- it will take the images at all posiblites to train the model [ex:rotation,flipping,cutting ect,]
"""

data_augmentation = tf.keras.Sequential([
    tf.keras.layers.RandomFlip('horizontal'),
    tf.keras.layers.RandomRotation(0.2)
])

"""repetedly apply the same layers to see the results"""

for image,_ in train_dataset.take(1):
  plt.figure(figsize=(15,15))
  first_image = image[0]
  for i in range(20):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    augmented_image = data_augmentation(tf.expand_dims(first_image,0))
    plt.imshow(augmented_image[0] / 255)

"""Rescale the pixel values"""

preprocess_input = tf.keras.applications.mobilenet_v2.preprocess_input

"""N"""

rescale = tf.keras.layers.Rescaling(1./127.5,offset=-1)

"""Create the base model from the pre-trained model MobileNet V2"""

img_shape = (160,160) + (3,)
base_model = tf.keras.applications.MobileNetV2(input_shape=img_shape,
                                               include_top=False,
                                               weights='imagenet')

image_batch,label_batch = next(iter(train_dataset))
feature_batch = base_model(image_batch)
print(feature_batch.shape)

base_model.trainable = False

base_model.summary()

global_average_layer = tf.keras.layers.GlobalAveragePooling2D()
feature_batch_average = global_average_layer(feature_batch)
print(feature_batch_average.shape)

prediction_layer = tf.keras.layers.Dense(1)
prediction_batch =prediction_layer(feature_batch_average)
print(prediction_batch.shape)

inputs = tf.keras.Input(shape=(160, 160, 3))
x = data_augmentation(inputs)
x = preprocess_input(x)
x = base_model(x, training=False)
x = global_average_layer(x)
x = tf.keras.layers.Dropout(0.2)(x)
outputs = prediction_layer(x)
model = tf.keras.Model(inputs, outputs)

model.summary()

len(model.trainable_variables)

tf.keras.utils.plot_model(model,show_shapes=True)

"""**Compile the model**"""

base_learning_rate = 0.0001
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=base_learning_rate),
              loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
              metrics=[tf.keras.metrics.BinaryAccuracy(threshold=0,name='accuracy')])

"""**Train the model**"""

intial_epochs = 10
loss0,accuracy0 = model.evaluate(validation_dataset)

print("initial loss: {:.2f}".format(loss0))
print("initial accuracy: {:.2f}".format(accuracy0))

history = model.fit(train_dataset,
                    epochs=intial_epochs,
                    validation_data=validation_dataset)

"""**Learning Curves**"""

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']

plt.figure(figsize=(8,8))
plt.subplot(2,1,1)
plt.plot(acc,label='Training Accuracy')
plt.plot(val_acc,label='Validation Accuracy')
plt.legend(loc='lower right')
plt.ylabel('Accuracy')
plt.ylim([min(plt.ylim()),1])
plt.title('Training and validation accuracy')

plt.subplot(2,1,2)
plt.plot(loss,label='Training Loss')
plt.plot(val_loss,label='Validation Loss')
plt.legend(loc='upper right')
plt.ylabel('Cross Entropy')
plt.ylim([0,1.0])
plt.title('Training and Validation Loss')
plt.xlabel('epoch')
plt.show()

"""**Fine Tuning the model**"""

# check how many layers are in the base model
print('The layers in the base are',len(base_model.layers))

# Fine tune from this layer
fine_tune = 100

# Freeze all the layers
for layer in base_model.layers[:fine_tune]:
  layer.trainable = False

"""**Compile the model**"""

model.compile(loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
              optimizer = tf.keras.optimizers.RMSprop(learning_rate=base_learning_rate/10),
              metrics=[tf.keras.metrics.BinaryAccuracy(threshold=0, name='accuracy')])

model.summary()

len(model.trainable_variables)

fine_tune_epochs = 10
total_epochs =  intial_epochs + fine_tune_epochs

history_fine = model.fit(train_dataset,
                         epochs=total_epochs,
                         initial_epoch=history.epoch[-1],
                         validation_data=validation_dataset)

acc +=history_fine.history['accuracy']
val_acc +=history_fine.history['val_accuracy']
loss += history_fine.history['loss']
val_loss += history_fine.history['val_loss']

plt.figure(figsize=(8, 8))
plt.subplot(2, 1, 1)
plt.plot(acc, label='Training Accuracy')
plt.plot(val_acc, label='Validation Accuracy')
plt.ylim([0.8, 1])
plt.plot([intial_epochs-1,intial_epochs-1],
          plt.ylim(), label='Start Fine Tuning')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(2, 1, 2)
plt.plot(loss, label='Training Loss')
plt.plot(val_loss, label='Validation Loss')
plt.ylim([0, 1.0])
plt.plot([intial_epochs-1,intial_epochs-1],
         plt.ylim(), label='Start Fine Tuning')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.xlabel('epoch')
plt.show()

"""**Model Evaluation and Prediction**"""

loss,accuracy = model.evaluate(test_dataset)
print('Test ccuracy',accuracy)

"""**Predictions**"""

# Taka a batch of images from the test data
image_batch,lael_batch = test_dataset.as_numpy_iterator().next()
predictions = model.predict_on_batch(image_batch).flatten()

# Apply sigmoid since our model returns logits
predictions = tf.nn.sigmoid(predictions)
predictions = tf.where(predictions < 0.5,0,1)

print('predictions:\n',predictions.numpy())
print('Labels:\n',label_batch)

plt.figure(figsize=(10,10))
for i in range(20):
  plt.subplot(5,5,i+1)
  plt.xticks([])
  plt.yticks([])
  plt.imshow(image_batch[i].astype('uint8'))
  plt.title(class_names[predictions[i]])

