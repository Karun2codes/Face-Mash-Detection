# train.py

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from model import build_model

# -------------------------------
# 1. LOAD DATA
# -------------------------------
datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2
)

train_data = datagen.flow_from_directory(
    'Dataset/',
    target_size=(128,128),
    batch_size=32,
    class_mode='binary',
    subset='training'
)

val_data = datagen.flow_from_directory(
    'Dataset/',
    target_size=(128,128),
    batch_size=32,
    class_mode='binary',
    subset='validation'
)

# -------------------------------
# 2. BUILD MODEL
# -------------------------------
model = build_model()

# -------------------------------
# 3. COMPILE
# -------------------------------
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# -------------------------------
# 4. TRAIN
# -------------------------------
model.fit(
    train_data,
    validation_data=val_data,
    epochs=10
)

# -------------------------------
# 5. SAVE MODEL
# -------------------------------
model.save("mask_model.h5")

print("✅ Model saved as mask_model.h5")