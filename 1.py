# -*- encoding: utf-8 -*-
'''
@File    :   练习.py
@Time    :   2022/06/11 19:39:08
@Author  :   2096779623 
@Contact :   admin@utermux.dev
@License :   MIT
'''

import turtle as te#导入海龟模块，te作为别名
mypen = te.Pen()#设置画笔
#te.hideturtle()隐藏画笔
mypen.pensize(15)#设置画笔大小
mypen.pencolor("gold")#设置画笔颜色为金色
mypen.forward(50)#向右走50个像素
mypen.pencolor("red")#设置画笔颜色为红色
mypen.forward(200)#继续向右走200个像素
mypen.pencolor("gold")#设置画笔颜色为金色
mypen.forward(50)#继续向右走50个像素
te.done()#收起画笔
