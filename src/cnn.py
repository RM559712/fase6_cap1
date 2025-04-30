# -*- coding: utf-8 -*-
# Imports
import os
import tensorflow as tf
import numpy as np
import seaborn as sns
from tensorflow.keras import Sequential, layers, callbacks
from tensorflow.keras.layers import Rescaling
from tensorflow.keras.preprocessing import image_dataset_from_directory
from tensorflow.keras.callbacks import EarlyStopping

# Caminhos locais (modifique conforme necessário)
train_dir = './data/images/'
test_dir = './data/tests/'

# Semente para reprodutibilidade
tf.random.set_seed(42)

# Carregamento do dataset com divisão automática treino/validação
train_dataset = image_dataset_from_directory(
    train_dir,
    validation_split=0.2,
    subset="training",
    seed=42,
    image_size=(32, 32),
    batch_size=32
)

validation_dataset = image_dataset_from_directory(
    train_dir,
    validation_split=0.2,
    subset="validation",
    seed=42,
    image_size=(32, 32),
    batch_size=32
)

# Dataset de teste com rótulos
test_dataset = image_dataset_from_directory(
    test_dir,
    image_size=(32, 32),
    batch_size=32,
    shuffle=False,
    label_mode='int'
)

# Normalização
normalization_layer = Rescaling(1./255)

train_dataset = train_dataset.map(lambda x, y: (normalization_layer(x), y))
validation_dataset = validation_dataset.map(lambda x, y: (normalization_layer(x), y))
test_dataset = test_dataset.map(lambda x, y: (normalization_layer(x), y))

# Definir modelo CNN
model = Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(2, activation='softmax')  # Ajuste conforme número de classes
])

# Compilar o modelo
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# EarlyStopping para evitar overfitting
es = EarlyStopping(
    monitor='val_accuracy',
    patience=5,
    restore_best_weights=True
)

# Resumo do modelo
model.summary()

# Treinamento
model.fit(
    train_dataset,
    validation_data=validation_dataset,
    epochs=50,
    callbacks=[es]
)

# Avaliação no dataset de teste
test_loss, test_acc = model.evaluate(test_dataset)
print("Test Loss:", test_loss)
print("Test Accuracy:", test_acc)