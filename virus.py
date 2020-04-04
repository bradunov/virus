from graphics import *
import random


# https://www.pas.rochester.edu/~rsarkis/csc161/python/pip-graphics.html

# sizex = 1550
# sizey = 1050
# nodes = 100
# rad = 25

scale = 12

sizex = 200 * scale
sizey = 100 * scale
rad = 1 * scale
nodes = 100
sim_time = 500

# Time of recovery (in simulation units)
recovery = 75

# Size of a quarantine box
box_size = 100
#box_size = 10000

# Quarantine for everyone stops in this time
stop_box = 100

# Initial probability of having the virus
start_prob = 1/10

# Initial probability of not being quarantined
#not_quarantined_prob = 4/10
not_quarantined_prob = 0


dx = sizex / 100
dy = sizey / 100

win = GraphWin('Virus', sizex, sizey + 200)


points = []
cir = []
movex = []
movey = []
virus = []
virus_time = []
box_sizes = []

for i in range(nodes):
    pt = Point(random.randrange(sizex), random.randrange(sizey))
    points.append(pt)
    c = Circle(pt, rad)

    if (random.random() < start_prob):
        c.setFill('red')
        virus.append(1)
        virus_time.append(0)
    else:
        c.setFill('green')
        virus.append(0)
        virus_time.append(-1)
    c.draw(win)
    cir.append(c)

    dir = random.choice([-1, 1])
    movex.append(dx * dir)
    dir = random.choice([-1, 1])
    movey.append(dy * dir)

    if (random.random() < not_quarantined_prob):
        # No movement limit
        box_sizes.append(10000)
    else:
        box_sizes.append(box_size)





for i in range(0, sim_time):
# Simulation time: 0 - 1000s

    if i == stop_box:
        for j in range(0, len(box_sizes)):
            box_sizes[j] = 10000

    cnt_vir = 0
    cnt_cur = 0
    cnt_healt = 0
    for c in range(nodes):
        # For each node c:

        if virus[c] == 1:
            cnt_vir = cnt_vir + 1
        elif virus[c] == 2:
            cnt_cur = cnt_cur + 1
        elif virus[c] == 0:
            cnt_healt = cnt_healt + 1

        if virus[c] == 1 and i - virus_time[c] > recovery:
            virus[c] = 2
            cir[c].setFill('yellow')

        # Moves one node - node cir[c]
        point = cir[c].getCenter()
        if (point.getX() > sizex or point.getX() > points[c].getX() + box_sizes[c]):
            movex[c] = -dx
        if (point.getX() < 0 or point.getX() < points[c].getX() - box_sizes[c]):
            movex[c] = dx
        if (point.getY() > sizey or point.getY() > points[c].getY() + box_sizes[c]):
            movey[c] = -dy
        if (point.getY() < 0 or point.getY() < points[c].getY() - box_sizes[c]):
            movey[c] = dy
        cir[c].move(movex[c], movey[c])

        for d in range(nodes):
            # For each other point d, check if c and d touch
            point2 = cir[d].getCenter()

            close_enough = pow(point.getX() - point2.getX(), 2) + pow(point.getY() - point2.getY(), 2) < pow(2 * rad, 2)
            c_has_virus = (virus[c] == 1)
            d_hasnt_virus = (virus[d] == 0)
            if (close_enough and c_has_virus and d_hasnt_virus):
                virus[d] = 1
                cir[d].setFill('red')
                virus_time[d] = i
                


    dr = sizex / sim_time
    r = Rectangle(Point(i*dr, sizey + 200), Point((i+1) * dr, sizey + 200 * (1 - 0.8 * cnt_vir / nodes)))
    r.setFill('red')
    r.draw(win)
    r = Rectangle(Point(i*dr, sizey + 200 * (1 - 0.8 * cnt_vir / nodes)), 
            Point((i+1) * dr, sizey + 200 * (1 - 0.8 * (cnt_vir + cnt_cur)/ nodes)))
    r.setFill('yellow')
    r.draw(win)
    r = Rectangle(Point(i*dr, sizey + 200 * (1 - 0.8 * (cnt_vir + cnt_cur)/ nodes)), 
            Point((i+1) * dr, sizey + 200 * (1 - 0.8 * (cnt_vir + cnt_cur + cnt_healt)/ nodes)))
    r.setFill('green')
    r.draw(win)


    #time.sleep(0.01)


win.getMouse()
win.close()


