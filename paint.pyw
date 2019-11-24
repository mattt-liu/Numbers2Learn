## UI
## Matthew Liu

########## MODULES ##########
from pygame import *
import pprint
import math as Math
import random
import os

def main():
    ########## VARIABLES ##########
    windowx = 850
    windowy = 600
    screenx = 224
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
    wipeScreen = False
    
    mode = "draw"

    size = int(screenx/24)

    outputFile = open("points.txt", "w")

    drawNum = ["zero","one","two","three","four","five","six","seven","eight","nine"][random.randint(0, 9)]

    #### rects
    drawRect = Rect(drawX, drawY, screenx, screenx)
    
    ########## INIT ##########
    init()
    font.init()
    display.set_caption("NAME")
    
    screen.fill(WHITE)
    startfont = font.SysFont('arial', 25)
    text1 = startfont.render("Draw " + drawNum, True, RED)
    text2 = startfont.render("Correct!", True, BLUE)
    ##########
    screen.fill(BLACK)
    draw.rect(screen, WHITE, drawRect)

    mx, my = mouse.get_pos()
    px, py = mouse.get_pos()
    

    while running:

        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()

        
        for evt in event.get():
            if evt.type == QUIT:
                running = False
            if evt.type == KEYDOWN:
                if evt.key == K_SPACE:
                    if mode == "draw": mode = "graph"
                    if mode == "crop": running = False
                if evt.key == K_ESCAPE:
                    wipeScreen = True;

        ## draw
                
        screen.blit(text1, (int(windowx/2 - text1.get_width()/2), int(windowy/2 - drawRect.height/2-text1.get_height())))
        
        if mode == "draw":
            
            ## if clicked
            if mb[0] == 1:
                draw.circle(screen, BLACK, (mx, my), size, 0)

                dx = mx - px
                dy = my - py
                d = Math.hypot(dx, dy)
                for i in range(int(d)):
                    draw.circle(screen, BLACK, (int(px + i*dx/d), int(py + i*dy/d)), size, 0)

            if wipeScreen:
                draw.rect(screen, WHITE, drawRect)
                wipeScreen = False
            
            ## update mouse
            px, py = mx, my

        if mode == "graph":
            
            points = []

            ## take in points
            for x in range(screenx):
                ys = []
                for y in range(screeny):
                    if screen.get_at((drawX+x, drawY+y)) != (255, 255, 255):
                        ys.append(1)
                    else:
                        ys.append(0)
                points.append(ys)
            ## rotate from (y,x) to (x,y)
            rPoints = []
            for x in range(len(points)):
                p = []
                for y in range(len(points[x])):
                    p.append(points[y][x])
                rPoints.append(p)
                
            for p in rPoints:
                outputFile.write(str(p)+"\n")
            outputFile.close()
            running = False
    ##        mode = "crop"
        
    ##    if mode == "crop":

    ##        screen.fill(WHITE)
            
            ## crop columns
    ##        newPoints = []
    ##        for i in range(len(points)):
    ##            y = points[i]
    ##            if 1 in y:
    ##                newPoints.append(y)
    ##
    ##        ## repaint trimmed image ##
    ##            
    ##        for x in range(len(newPoints)):
    ##            for y in range(len(newPoints[x])):
    ##                if newPoints[x][y] == 1:
    ##                    screen.set_at((x, y), BLACK)
    ##                else:
    ##                    screen.set_at((x, y), RED)
    ##
    ##        ## crop rows
    ##        toTrim = []                    
    ##        for i in range(len(points)):
    ##            hasPoint = False
    ##            for j in range(len(points[i])):
    ##                if points[i][j] == 1:
    ##                    hasPoint = True
    ##            if not hasPoint:
    ##                toTrim.append(i)
    ##
    ##        ## trimming vertical columns @ 3:01 am 11/23
    ##
    ##        
    ##        for i in range(len(newPoints)-1,-1,-1):
    ##            for j in range(len(newPoints[i])-1,-1,-1):
    ##                if i in toTrim:
    ##                    del newPoints[i][j]
    ##        
    ##        ## repaint trimmed image ##            
    ##        for x in range(len(newPoints)):
    ##            for y in range(len(newPoints[x])):
    ##                if newPoints[x][y] == 1:
    ##                    screen.set_at((x, y), BLACK)
    ##                else:
    ##                    screen.set_at((x, y), RED)
            
            
        clock.tick(120)
        display.update()


        
    quit()
    return drawNum

if __name__ == "__main__":
    main()
