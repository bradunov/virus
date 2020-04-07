from graphics import *


#creates a canvas of size x=600 and y=400
win = GraphWin('Virus', 600, 400)


#creates a new circle in the computer memory
#the circle is at x=120 y=25 with radius 20
#the name of the circle is c
c = Circle(Point(120, 25), 20)


#creates a new circle, second circle in the computer memory
#the circle is at x=120 y=205 with radius 20
#the name of the new circle is c2
#WARNING: if you name the new circle c, as the old one,
#the computer will forget about the old circle
#as it can remember only one circle with the same name
c2 = Circle(Point(120, 205), 20)

#set the colour of circle c to orange
c.setFill('orange')

#set the colour of circle c2 to green
c2.setFill('green')

#actually draw the cirle c
c.draw(win)

#actually draw the cirle c2
c2.draw(win)

#wait for mouse to be clicked
win.getMouse()

#close the canvas
win.close()
