# coding:utf -8


from pymouse import PyMouse

m = PyMouse()
print m.position()#获取当前坐标的位置
m.move(1273,12)#鼠标移动到xy位置
print m.position()
m.click(1273,12)#移动并且在xy位置点击
#m.click(x,y,1|2)#移动并且在xy位置点击,左右键点击