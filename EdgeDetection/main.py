import pygame

def drawEdges(picture):
    for x in range(picture.length - 1):
        for y in range(picture.height - 1):
            pixelSum = getRed(pixel) + getGreen(pixel) + getBlue(pixel)
            nextPixel = getPixel(picture, x+1, y+1)
            nextPixelSum = getRed(nextPixel)+ getGreen(nextPixel) + getBlue(nextPixel)
            diff = abs(nextPixelSum-pixelSum)
            newColor = makeColor(diff,diff,diff)
            setColor(pixel, newColor)
