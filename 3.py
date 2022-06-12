# -*- encoding: utf-8 -*-
'''
@File:   3.py
@Time:   2022/06/12 19:53:53
@Author  :   2096779623 
@Mail:   admin@utermux.dev
@License :   MIT
'''


import turtle as te#导入海龟模块，te作为别名
mypen = te.Pen()#设置画笔
#te.bgpic("b.gif")设置图片
mypen.forward(-105)#向左走105个像素
mypen.pencolor("black")#设置画笔颜色：黑色
mypen.pensize(5)#设置画笔大小：5
mypen.forward(70)#向右走70个像素
mypen.pencolor("gold")#设置画笔颜色：金色
mypen.forward(70)#向右走70个像素
mypen.pencolor("black")#设置画笔颜色：黑色
mypen.pensize(5)#设置画笔大小：5


mypen.pensize(50)#设置画笔大小：50
mypen.pencolor("black")#设置画笔颜色：黑色
mypen.forward(-210)#向左走210个像素


mypen.pensize(40)#设置画笔大小：40
mypen.pencolor("gray")#设置画笔颜色：灰色
mypen.forward(210)#向右走210个像素

mypen.pensize(30)#设置画笔大小：30
mypen.pencolor("red")#设置画笔颜色：红色
mypen.forward(-210)#向左走210个像素

mypen.pensize(20)#设置画笔大小：20
mypen.pencolor("pink")#设置画笔颜色：粉色
mypen.forward(210)#向右走210个像素

mypen.pensize(10)#设置画笔大小：10
mypen.pencolor("white")#设置画笔颜色：白色
mypen.forward(-210)#向左走210个像素

te.hideturtle()#隐藏画笔
te.done()#结束绘画

