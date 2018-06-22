#PythonDraw.py
#绘制python蟒蛇

import turtle

#设置画布窗体的宽度、高度、起始屏幕坐标
turtle.setup(650,350,200,200)
#抬起画笔，移动画笔起始点位置
turtle.penup()
#反向（向西）直线移动250像素
turtle.fd(-250)
#放下画笔，开始绘制
turtle.pendown()
#设置画笔宽度为25像素
turtle.pensize(25)
#设置画笔颜色
turtle.pencolor("gold")
#改变行进方向，将海龟方向转到-40度方向
turtle.seth(-40)
for i in range(4):
    #控制海龟走曲线，圆心在海龟当前位置右侧40，半径40，绘制弧度80
    turtle.circle(40,80)
    #控制海龟走曲线，圆心在海龟当前位置左侧40，半径40，绘制弧度80
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40 * 2/3)
turtle.done()
