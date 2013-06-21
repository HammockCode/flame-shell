
import curses

def normalize(val, floor, ceil):
    result = val
    if result < floor:
        result = floor
    elif result > ceil:
        result = ceil
    return result       


def clearScreen():
    curtain = "\n"
    for x in range(0,50):
        curtain = curtain + "\n"
        print curtain
    
    
def toString(row, symbols):
    result = ''
    for s in [symbol(x, symbols) for x in row]:
        result = result + s
        
    return result
    
def symbol(x, symbols):
	return symbols[normalize(x, 0, len(symbols)-1)]    


class FlamesOut:
	
	stdscr = None
	maxX = 150
	maxY = 40	    
	    
	def printFrame(self, frame, symbols):
	    clearScreen()
	    out = ''
	    i = len(frame)
	    while i>=0:
	        i = i-1
	        row = frame[i]
	        out = out + toString(row, symbols) + "\n"
	    print out
	
	def printFrameCurses(self, frame, symbols):
		for y in range(0, len(frame)):
			row = frame[y]
			for x in range(0, len(row)):
				c = symbol(row[x], symbols)
				self.setChar(x,y,c)	
		self.stdscr.refresh()

				
	def setChar(self, x,y,c):
	    self.stdscr.addstr(self.maxY-y,x,c, curses.color_pair(1))
	
	def initCurses(self):
	    self.stdscr = curses.initscr()
	    
	    dim = self.stdscr.getmaxyx()
	    self.maxX = dim[1] - 1
	    self.maxY = dim[0] - 1
	    
	    curses.start_color()
	    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
	
	def endCurses(self):
	    curses.nocbreak()
	    self.stdscr.keypad(0)
	    curses.echo()
	    curses.endwin()
		    
	    
