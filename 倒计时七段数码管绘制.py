import turtle
import time


def drawGap():      # 绘制数码管之间的间隔
    turtle.penup()
    turtle.fd(5)


def drawLine(draw):     # 绘制单端数码管
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)


def drawDigit(digit):       # 根据数字绘制七段数码管
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.penup()
    turtle.fd(40)
    turtle.right(180)
    turtle.clear()


def daojishi():
    i = 9
    while i >= 0:
        drawDigit(i)
        i = i - 1


def main():
    turtle.setup(800,350,200,200)
    turtle.speed(3)
    turtle.pencolor("red")
    turtle.pensize(5)
    turtle.penup()
    turtle.fd(-50)
    daojishi()
    turtle.hideturtle()
    turtle.done()


main()
