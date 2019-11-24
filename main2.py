
## UI
## Matthew Liu

import os
import numpy as np
import matplotlib.pyplot as pt
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from pygame import *
import convert, degrade, paint, ANN

def main2():
    print("\n\n...LOADING...\n\n")
    # Import the dataset
    dataset = pd.read_csv('train.csv')

    X = dataset.iloc[:,1:].values
    y = dataset.iloc[:,0].values

    from keras.utils import to_categorical
    y = to_categorical(y)

    # Feature Scaling
    from sklearn.preprocessing import StandardScaler
    sc_X = StandardScaler()
    X_train = sc_X.fit_transform(X)


    # Making the ANN

    # Importing Keras libraries and packages
    import keras
    from keras.models import Sequential
    from keras.layers import Dense

    # Initializing the ANN
    classifier = Sequential()

    # Adding the input layer and the first hidden layer
    classifier.add(Dense(activation = 'relu', input_dim = 784, units = 392, kernel_initializer = "uniform"))

    # Adding the second hidden layer
    classifier.add(Dense(activation = 'relu', units = 397, kernel_initializer = "uniform"))

    # Adding the output layer
    classifier.add(Dense(activation = 'softmax', units = 10, kernel_initializer = "uniform"))

    # Compiling the ANN
    classifier.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

    # Fitting the ANN to the training set
    classifier.fit(X_train, y, epochs = 5)

    return classifier, sc_X, X_train


running = True


if __name__ == "__main__":
    clf, sc_X, X_train = main2()
    while running:
        num = paint.main()
        degrade.main()
        convert.main()
        running = ANN.main(clf, sc_X, X_train, num)
        
