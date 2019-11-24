
import os
import numpy as np
import matplotlib.pyplot as pt
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from pygame import *

def main(clf):


    ## temp
    #
##    data = pd.read_csv('train.csv').values
##    clf = DecisionTreeClassifier()
##
##    xtrain = data[0:42000,1:]
##
##    train_label = data[0:42000,0]
##
##    clf.fit(xtrain,train_label)
    #
    ##    

    points = ""
    try:
        points = pd.read_csv('dPoints.csv').values
    except:
        pass    
    output = str(clf.predict([points[0]]))

    ## draw window
    screeny = 112
    screenx = screeny*4
    os.environ['SDL_VIDEO_WINDOW_POS'] = '225, 175'
    screen = display.set_mode((screenx, screeny))

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
    
    screen.fill(WHITE)
    startfont = font.SysFont('arial', 25)
    text1 = startfont.render("The number was " + output[1], True, (255,0,0))

    mx, my = mouse.get_pos()
    px, py = mouse.get_pos()
    
    screen.fill(WHITE)

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
        
        screen.blit(text1, (int(screenx/2 - text1.get_width()/2), int(screeny/2 - text1.get_height()/2)))

        for i in range(len(colors)):
            for j in range(len(colors[i])):
                c = colors[i][j]
                draw.rect(screen, (c, c, c), (j*4,i*4,4,4), 0)

        clock.tick(120)
        display.update()
    quit()
    return RETURN
    
if __name__ == "__main__":
    main()

