import numpy as np
import random
import tensorflow as tf


def createTemplate():
    return tf.keras.models.Sequential([
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.15),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.15),
        tf.keras.layers.Dense(64, activation='relu'),
    ])

def prepareData(inputs: np.ndarray, labels: np.ndarray):
    classesNumbers = 10
    digitalIdx = [np.where(labels == i)[0] for i in range(classesNumbers)]
    pairs = list()
    labels = list()
    n = min([len(digitalIdx[d]) for d in range(classesNumbers)]) - 1
    for d in range(classesNumbers):
        for i in range(n):
            z1, z2 = digitalIdx[d][i], digitalIdx[d][i+1]
            pairs += [[inputs[z1] , inputs[z2]]]
            inc = random.randrange(1, classesNumbers)
            dn = (d + inc) % classesNumbers
            z1, z2 = digitalIdx[d][i], digitalIdx[dn][i]
            pairs += [[inputs[z1] , inputs[z2]]]
            labels += [1, 0]
    return np.array(pairs), np.array(labels, dtype=np.float32)

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train = x_train.as_type(np.float32)
x_test = x_test.as_type(np.float32)
x_train /= 255
x_test /= 255

input_shape = x_train.shape[1:]
train_pairs, tr_labels = prepareData(x_train, y_train)
test, test_labels = prepareData(x_test, y_test)

input_a = tf.keras.layers.Input(shape=input_shape)
encoder1 = base_network(input_a)

input_b = tf.keras.layers.Input(shape=input_shape)
encoder2 = base_network(input_b)

distance = tf.keras.layers.Lambda(lambda embedings: tf.keras.backend.abs(embedings[0] - embedings[1]))([encoder1, encoder2])

measureOfSimilarity = tf.keras.layers.Dense(1, activation='sigmoid')(distance)

