
import random

from array import array

class FirePlace:
    
    screenWidth=175
    screenHeight=40
    
    frameBuffer = []
    iterations = 10
    heat = 2
    
    out = None
    
    maxTemperature = 4
    symbols = [' ','.','+','*', '#']
    
    def __init__(self, frameBuffer, heat=2, iterations=10, screenWidth=175,  screenHeight=40, symbols=[' ','.','+','*', '#'], out=None):
        self.frameBuffer = frameBuffer
        self.heat = heat
        self.iterations = iterations    
        self.symbols = symbols
        self.maxTemperature = len(symbols)-1
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.out = out
        
    def run(self):
        frame = []  
        if len(self.frameBuffer)==0 :
            
            frame.append(self.ignite())
            frame.append(self.ignite())
            frame.append(self.ignite())
            frame.append(self.ignite())
            frame = self.flameOn(self.heat, frame)
            self.frameBuffer.append(self.cloneFrame(frame))
        
        for i in range(0,self.iterations):
            frame = self.burn(frame, self.heat)
            self.frameBuffer.append(self.cloneFrame(frame))

            if self.out is not None:
                self.out.printFrameCurses(frame, self.symbols)
    
    def ignite(self):
        sparks = array('H')
        for i in range(0,self.screenWidth):
            sparks.insert(i, self.maxTemperature)
        return sparks 
    
    def spark(self, context):
        contextSize = len(context) 
        spark = 0
        odds = sum(1 for x in context if x > 0)
        dice = random.randint(0,contextSize)
        
        if dice < odds : 
            spark = odds 
    
        return spark
    
    
    
    
    def cell(self, x,y,matrix):
        cell = 0
        if x>=0 and y>=0 and y<len(matrix):
            row = matrix[y]
            if x<len(row):
                cell = row[x]
        return cell
                
    
    def context(self, x,y,window, matrix):
        context = array('H')
        numOfRows = len(matrix)
        for rowInd in [y-j for j in range(0,window) if y-j >= 0 and y<numOfRows]:
            row = matrix[rowInd]
            offSet = x-window +1
            cutOff = x+window
            if offSet<0:
                offSet = 0
            if cutOff > len(row)-1:
                cutOff = len(row) -1
            for cell in row[offSet:cutOff]:
                context.append(cell)
        
        return context
    
    
    def dead(self, row):
        dead = True
        for cell in row:
            if cell > 0 :
                dead = False
                break
        return dead
            


    def flameOn(self, heat, matrix):
    
        sparks = matrix[-1]
        
        while not self.dead(sparks) and len(matrix)<self.screenHeight:   
            nextGen = array('H')
            for i in range(0,self.screenWidth):
                context = self.context(i,len(matrix)-1, heat, matrix) 
                nextGen.insert(i,self.spark(context))
            sparks = nextGen 
            matrix.append(sparks)
            
        return matrix
    
    def burn(self, frame, heat):
        frame[0] = self.ignite()
        frame[1] = self.ignite()
        frame[2] = self.ignite()
        frame[3] = self.ignite()
    
        for y in range(0,len(frame)):
            for x in range(0, len(frame[y])):
                frame[y][x] = self.spark(self.context(x,y,heat,frame))
        frame = self.flameOn(heat, frame)
        return frame
    
    
    
    def cloneFrame(self, frame):
        clone = []
        for row in frame:
            rowCopy = array('H')
            for cell in row:
                rowCopy.append(cell)
            clone.append(rowCopy)
        return clone
   
   
   
   


 
