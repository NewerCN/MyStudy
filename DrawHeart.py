import turtle as t


#设置画布
t.screensize(400,300,"deepskyblue")


#设置画笔宽度、颜色、速度
t.pensize(2)
t.color("deeppink","deeppink")
t.speed(1)

t.begin_fill()
#绘制左半边
t.left(135)
t.fd(200)
t.circle(-100,180)

#绘制右半边
t.left(90)
t.circle(-100,180)
t.fd(200)

t.end_fill()

t.penup()
t.hideturtle()

#输出文本
s1 = "I Love You,夏然然"
s2 = "By 边旭东"
t.goto(0,-100)
t.color("deeppink","deeppink")
t.write(s1,font = ('微软雅黑',25,"bold"),align = "center")
t.goto(185,-150)
t.write(s2,font = ('微软雅黑',20),align = "right")


t.done()
