from graphics import *
import random
import textwrap
import numpy as np


def getSeeds(seed):
    seeds=[]
    temp = textwrap.wrap(seed, int(len(seed)/3))
    for i in range (0,3):
        seeds.append(int(temp[i])%256)
    return seeds
def __main__():
    win=GraphWin('Probabilistic Picture Generator',500,500,autoflush=False)
    seed = str(input("Enter an integer seed: "))
    seedList = getSeeds(seed)
    r_prev = seedList[0]
    g_prev = seedList[1]
    b_prev = seedList[2]
    coef = [-1,1]
    matrix = np.zeros((500,500,3))
    print("Generating...")
    win.update()
    for i in range(0,500):
        for j in range(0,500):
            pt = Point(i, j)
            if i == 0 & j == 0:
                r = r_prev
                g = g_prev
                b = b_prev
            elif i >= 1 & j >= 1:
                r = (matrix[i-1][j-1][0]+matrix[i-1][j][0]+matrix[i][j-1][0])/3 + (random.choice(coef))
                g = (matrix[i-1][j-1][1]+matrix[i-1][j][1]+matrix[i][j-1][1])/3 + (random.choice(coef))
                b = (matrix[i-1][j-1][2]+matrix[i-1][j][2]+matrix[i][j-1][2])/3 + (random.choice(coef))            
            elif i == 0 & j != 0:
                r = matrix[i][j-1][0]/2 + (random.choice(coef)*1)
                g = matrix[i][j-1][1]/2 + (random.choice(coef)*1)
                b = matrix[i][j-1][2]/2 + (random.choice(coef)*1)
            elif i != 0 & j == 0:
                r = matrix[i-1][j][0]/2 + (random.choice(coef)*1)
                g = matrix[i-1][j][1]/2 + (random.choice(coef)*1)
                b = matrix[i-1][j][2]/2 + (random.choice(coef)*1)
            if r <= 30:
                r = ((r_prev+matrix[i-1][j-1][0]+matrix[i-1][j][0]+matrix[i][j-1][0])/4)
            if r >= 256:
                r = 255
            if g <= 30:
                g = ((g_prev+matrix[i-1][j-1][1]+matrix[i-1][j][1]+matrix[i][j-1][1])/4)
            if g >= 256:
                g = 255
            if b <= 30:
                b = ((b_prev+matrix[i-1][j-1][2]+matrix[i-1][j][2]+matrix[i][j-1][2])/4)
            if b >= 256:
                b = 255
            color = color_rgb(int(r), int(g), int(b))
            matrix[i][j][0] = r
            matrix[i][j][1] = g 
            matrix[i][j][2] = b
            pt.setFill(color)
            pt.draw(win)
    print("Done!")
    win.getMouse()
    win.close()

