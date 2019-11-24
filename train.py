import numpy as np
import matplotlib.pyplot as pt
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

def main():
    
    data = pd.read_csv('train.csv').values
    clf = DecisionTreeClassifier()

    # Training data for half of the rows and all the columns except the first
    xtrain = data[0:42000,1:]

    train_label = data[0:42000,0]

    clf.fit(xtrain,train_label)

    # testing data
##
##    print("DATA")
##    print(data[0])
##    print(len(data[0]))
    points = pd.read_csv('dPoints.csv').values
    newPoints = pd.read_csv('dPoints.csv').values


    ## convert to rgb val
    for i in range(len(points)):
        for j in range(len(points[i])):
            if points[i][j] == 1:
                newPoints[i][j] = 255
    

##    actual_label = data[21000:,0]
##    p = clf.predict(xtest)
##    count = 0 
##    for i in range(21000):
##        if p[i]==actual_label[i]:
##            count+=1
##        else:
##            0
##    print("Accuracy = ", (count/21000*100),"%")


    d=newPoints[0]
    d.shape=(28,28)
    
    print(clf.predict([newPoints[0]]))

    
    pt.imshow(255-d,cmap='gray')
    pt.show()


if __name__ == "__main__":
    main()

