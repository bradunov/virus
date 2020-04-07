from graphics import *


#creates a canvas of size x=600 and y=400
win = GraphWin('Virus', 600, 400)


#creates the circle in computer memory
#the circle is at x=120 y=25 with radius 20
#the name of the circle is c
c = Circle(Point(120, 25), 20)

#set the colour to orange
c.setFill('orange')

#actually draw the cirle
c.draw(win)


#wait for mouse to be clicked
win.getMouse()

#close the canvas
win.close()
