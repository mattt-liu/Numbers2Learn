
import os
import numpy as np
import matplotlib.pyplot as pt
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from pygame import *
import keras
from keras.models import Sequential
from keras.layers import Dense


def main(classifier, sc_X, X_train, num):

# TEMP ############## TEMP


##    classifier = Sequential()
##
##    # Adding the input layer and the first hidden layer
##    classifier.add(Dense(activation = 'relu', input_dim = 784, units = 392, kernel_initializer = "uniform"))
##
##    # Adding the second hidden layer
##    classifier.add(Dense(activation = 'relu', units = 397, kernel_initializer = "uniform"))
##
##    # Adding the output layer
##    classifier.add(Dense(activation = 'softmax', units = 10, kernel_initializer = "uniform"))
##
##    # Compiling the ANN
##    classifier.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
##
##    # Fitting the ANN to the training set
##    classifier.fit(X_train, y, epochs = 1)
# TEMP    ########### TEMP

    points = ""
    y_pred = []
    try:
        X_train = sc_X.fit_transform(X_train)
        X_test = sc_X.transform(pd.read_csv('dPoints.csv').values)
        y_pred = classifier.predict(X_test)
        points = pd.read_csv('dPoints.csv').values
    except:
        pass

    ## finds max confidence
    for i in range(len(y_pred[0])):
        line = y_pred[0][i]
##    print(sum(y_pred[0]))

    maxV = round(max(y_pred[0]), 5)
    output = maxV
    for i in range(len(y_pred[0])):
        if maxV == round(y_pred[0][i], 5):
            output = i
    
    
    ## draw window
    windowx = 850
    windowy = 600
    screenx = 112
    screeny = screenx
    drawX = int(windowx/2 - screenx/2)
    drawY = int(windowy/2 - screeny/2)
    os.environ['SDL_VIDEO_WINDOW_POS'] = '225, 175'
    screen = display.set_mode((windowx, windowy))

    clock = time.Clock()

    WHITE  = (255, 255, 255)
    RED    = (255,   0,   0)
    ORANGE = (255, 125,   0)
    YELLOW = (255, 255,   0)
    GREEN  = (  0, 255,   0)
    CYAN   = (  0, 255, 255)
    BLUE   = (  0,   0, 255)
    VIOLET = (255,   0, 255)
    BLACK  = (  0,   0,   0)

    running = True
    RETURN = True

    ## init
    init()
    font.init()
    display.set_caption("Result")
    
    screen.fill(BLACK)
    startfont = font.SysFont('arial', 25)
    
    #### rects
    drawRect = Rect(drawX, drawY, screenx, screenx)

##    msg = "The number was " + str(output)
    msg = "Incorrect. The number was " + num + "("+str(output)+")"
    nums = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    if (num == nums[output]):
        msg = "Correct"
    text1 = startfont.render(msg, True, (255,0,0))
    
    mx, my = mouse.get_pos()
    px, py = mouse.get_pos()

    ## get shade of each pixel
    colors = []
    cs = []
    for i in range(len(points[0])):
        x = int((i+1)/28)
        y = (i+1)%28
        c = 255-int(points[0][i])
        cs.append(c)
        if y == 0:
            colors.append(cs)
            cs = []

    ####    
    while running:
        
        for evt in event.get():
            if evt.type == QUIT:
                running = False
            if evt.type == KEYDOWN:
                if evt.key == K_SPACE:
                    running = False
                if evt.key == K_ESCAPE:
                    running = False
                    RETURN = False
                
        screen.blit(text1, (int(windowx/2 - text1.get_width()/2), int(windowy/2 - drawRect.height/2-text1.get_height())))

        ## draw image
        for i in range(len(colors)):
            for j in range(len(colors[i])):
                c = colors[i][j]
                draw.rect(screen, (c, c, c), (drawX+j*4, drawY+i*4,4,4), 0)

        clock.tick(120)
        display.update()
    quit()
    return RETURN

if __name__ == "__main__":
    main()
