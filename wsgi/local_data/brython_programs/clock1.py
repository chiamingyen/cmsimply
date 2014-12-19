import time
import math
import datetime
from browser import timer

canvas = doc["plotarea"]
context = canvas.getContext("2d")
scale = 4
FONT_HEIGHT = 20
MARGIN = 100
HAND_TRUNCATION = canvas.width/(25*scale)
HOUR_HAND_TRUNCATION = canvas.width/(10*scale)
NUMERAL_SPACING = 20
RADIUS = canvas.width/scale - MARGIN
HAND_RADIUS = RADIUS + NUMERAL_SPACING

# Functions

def drawCircle():
    context.beginPath()
    context.arc(canvas.width/scale, canvas.height/scale,
               RADIUS, 0, math.pi*2, True)
    context.stroke()

   
def drawNumerals():
    numerals = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ]
    angle = 0
    numeralWidth = 0
    for numeral in numerals:
        angle = (math.pi/6)*(numeral-3)
        numeralWidth = context.measureText(numeral).width
        context.fillText(numeral, 
                            canvas.width/scale  + math.cos(angle)*(HAND_RADIUS) - numeralWidth/scale,
                            canvas.height/scale + math.sin(angle)*(HAND_RADIUS) + FONT_HEIGHT/scale)

def drawCenter():
    context.beginPath()
    context.arc(canvas.width/scale, canvas.height/scale, 5, 0, math.pi*2, True)
    context.fill()

def drawHand(loc, isHour):
    angle = (math.pi*2) * (loc/60) - math.pi/2
    if isHour:
        handRadius = RADIUS - HAND_TRUNCATION-HOUR_HAND_TRUNCATION
    else:
        handRadius = RADIUS - HAND_TRUNCATION
    context.moveTo(canvas.width/scale, canvas.height/scale)
    context.lineTo(canvas.width/scale  + math.cos(angle)*handRadius, 
                        canvas.height/scale + math.sin(angle)*handRadius)
    context.stroke()

def drawHands():
    now = datetime.datetime.now()
    day = now.day
    hour = now.hour%12 + now.minute/60
    minute = now.minute
    second = now.second+now.microsecond/1000000
    drawHand(hour*5 + (minute/60)*5, True)
    drawHand(minute, False)
    drawHand(second, False)

def drawClock():
   context.clearRect(0,0,canvas.width,canvas.height)
   drawCircle()
   drawCenter()
   drawHands()
   drawNumerals()

# Initialization

loop = timer.set_interval(drawClock, 1000)
