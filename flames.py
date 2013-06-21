#!/usr/bin/python

from fireplace import FirePlace
from time import sleep

from flamesOut import FlamesOut

import argparse

heat = 2
symbols = [' ','.','+','*', '#']

argparser = argparse.ArgumentParser()
argparser.add_argument("iterations", help="Number of iterations", type=int)

args = argparser.parse_args()

frameBuffer = []

try:
    out = FlamesOut()
    out.initCurses()
    
    #symbols = list(";D):- ") # smilies
    #symbols = list("Marko ") # my name
    #symbols = list("Lol:) ") # Lol
    #symbols = list("()[]{} ") # parentheses
    #symbols = list("()[]{}/#;:* ") # programming syntax
    #symbols.reverse()
    
    fire = FirePlace(frameBuffer, heat, args.iterations, out.maxX, out.maxY, symbols, out)
    fire.run()
    
    while True:
        for frame in frameBuffer[1:-1]:
            out.printFrameCurses(frame, symbols)
            sleep(0.1)

finally:        
    out.endCurses()
