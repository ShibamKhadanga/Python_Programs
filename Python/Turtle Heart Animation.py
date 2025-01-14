# Single Color
'''
import  math
from turtle import *
def hearta(k) :
       return 15*math.sin(k)**3
def heartb(k) :
       return 12*math.cos(k)-5*\
                         math.cos(2*k)-2*\
                         math.cos(3*k)-\
                         math.cos(4+k)
speed(50000)
bgcolor("black")
for i in range(6000):
    goto(hearta(i)*20,heartb(i)*20)
    for j in range(2):
           color("cyan")
    goto(0,0)
done()
'''

# Multi Color
'''
h=0
import  math
from turtle import *
from colorsys import *
def hearta(k) :
       return 15*math.sin(k)**3
def heartb(k) :
       return 12*math.cos(k)-5*\
                         math.cos(2*k)-2*\
                         math.cos(3*k)-\
                         math.cos(4+k)
speed(50000)
bgcolor("black")
for i in range(6000):
    goto(hearta(i)*20,heartb(i)*20)
    for j in range(2):
           c=hsv_to_rgb(h,1,1)
           color(c)
           h+= 0.005
    goto(0,0)
done()

'''



# Flower Animation
'''
from turtle import *
from colorsys import *
bgcolor ('black')
tracer(100)
pensize(4)
h=0

def draw(ang, n):
       circle(5+n, 69)
       left (ang)
       circle(5+2*n, 60)

goto(0,0)

for i in range(500000):
       c = hsv_to_rgb(h,1,1)
       h+= 0.005
       color(c)
       up()
       draw(90, i)
       draw(180, i)
       down()
       draw(1/2, i-i)
       draw(180, i/2)
       draw(120, i-i)
'''

