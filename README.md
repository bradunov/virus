# virus

Learn to code with COVID-19

This is a set of lessons. Each lesson will teach you one more coding example. At the end, we will present you with a full blown simulation of a (COVID-19) virus outbreak and how different actions can affect it. 

We will start with instructions on how to set your computer up, then go over the introductory lessons and finally explain the virus simulation. 




## Setup

In this course, we will be using Python programming language. 
In order to follow our course, you will need first to install Python on your computer. 
If you use Windows, try following this [link](https://docs.microsoft.com/en-us/windows/python/beginners) to set up Python on Windows. 

You will also need to install the graphics module that allows you to draw on a screen. Open a shell or a VS Code terminal, as described in the previous tutorial, and type:
> python -m pip install --user http://bit.ly/csc161graphics

This [link] (https://www.pas.rochester.edu/~rsarkis/csc161/python/pip-graphics.html) has instructions but you shouldn't need them. 

Now, you should be ready to go. 





## Introductory lessons



### The first lesson
In the first lesson we will try to make a coloured circle. The code for the lesson is [here](https://github.com/bradunov/virus/blob/master/lesson1.py). Download the file on your computer and open it using VSCode (which you have downloaded as described in the basic instructions above). 

For now, ignore
> from graphics import *

This is used to tell the program that we will draw. 

We will use command Graphwin to create a canvas (a window) in which we will draw.
It will be 600 pixels tall and 400 wide.
One pixel is one dot on the screen.
Then we make a circle using command `Circle(Point(120, 25), 20)`.
It has two parameters.
Parameters describe how a command should behave.
The first parameter is a point where the circle should be placed.
The point is created using Point command, which also has two parameters, X and Y coordinate.
In this case, we create `Point(120,25)`, which is a point at X=120 and Y=25.
The second parameter of the circle command is the radius. It is 20 in this case. 
We give the circle name c by using an assignment command. 
> c = Circle(Point(120, 25), 20)

From now on we will refer to this circle as c.

We then color it in orange by using a command setFill('orange').
We call
> c.setFill('orange')

to tell that the colouring should be applied on our circle c.

So far, the circle is described but not yet drawn on the screen.
Finally, we have to tell the program to actually draw the circle.
We use this using command 
> c.draw(win)

After this, the circle can be seen!

At the end of the program, we use a trick. We say:
> win.getMouse()

This prevents our program from finishing immediately (and destroying our lovely circle).
Instead, we wait for a mouse to be pressed.
Once that is done, we close the canvas.
And that is it!







### The second lesson 

In the second lesson we will make two coloured circles.





### The third lesson

In the third lesson we shall forget about the
second circle and make the first one move.



### Lesson four

Now we'll make two circles move.



### Lesson five

This time we'll make two circles crash
