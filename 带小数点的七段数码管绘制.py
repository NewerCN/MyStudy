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
    turtle.left(180)
    turtle.fd(20)


def drawpoint():
    drawLine(False)
    drawLine(False)
    turtle.fd(19)
    turtle.pendown()
    turtle.fd(2)
    turtle.penup()
    turtle.fd(19)
    turtle.right(90)
    drawLine(False)
    turtle.left(90)
    drawLine(False)
    drawLine(False)
    drawLine(False)
    turtle.penup()
    turtle.left(180)
    turtle.fd(20)


def drawDate(date):     # date为日期，格式为 '%Y.%m.%d'
    turtle.pencolor("red")
    for i in date:
        if i == '.':
            drawpoint()
        else:
            drawDigit(eval(i))


def main():
    turtle.setup(900,350,200,200)
    turtle.speed(5)
    turtle.penup()
    turtle.fd(-350)
    turtle.pensize(5)
    drawDate(time.strftime("%Y.%m.%d",time.gmtime()))
    turtle.hideturtle()
    turtle.done()


main()
