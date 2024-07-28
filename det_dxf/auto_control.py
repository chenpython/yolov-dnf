import serial
import serial.tools.list_ports
import time,random


time.sleep(1)
portx="COM5"
bps=9600
timex=1
ser=serial.Serial(portx,bps,timeout=timex)

#松开按键
release=bytes.fromhex("57 AB 00 02 08 00 00 00 00 00 00 00 00 0C")

a=bytes.fromhex("57 AB 00 02 08 00 00 04 00 00 00 00 00 10")
s=bytes.fromhex("57 AB 00 02 08 00 00 16 00 00 00 00 00 22")
d=bytes.fromhex("57 AB 00 02 08 00 00 07 00 00 00 00 00 13")
f=bytes.fromhex("57 AB 00 02 08 00 00 09 00 00 00 00 00 15")
g=bytes.fromhex("57 AB 00 02 08 00 00 0A 00 00 00 00 00 16")

x=bytes.fromhex("57 AB 00 02 08 00 00 1B 00 00 00 00 00 27")
c=bytes.fromhex("57 AB 00 02 08 00 00 06 00 00 00 00 00 12")
v=bytes.fromhex("57 AB 00 02 08 00 00 19 00 00 00 00 00 25")
b=bytes.fromhex("57 AB 00 02 08 00 00 05 00 00 00 00 00 11")

q=bytes.fromhex("57 AB 00 02 08 00 00 14 00 00 00 00 00 20")
w=bytes.fromhex("57 AB 00 02 08 00 00 1A 00 00 00 00 00 26")
e=bytes.fromhex("57 AB 00 02 08 00 00 08 00 00 00 00 00 14")
r=bytes.fromhex("57 AB 00 02 08 00 00 15 00 00 00 00 00 21")
t=bytes.fromhex("57 AB 00 02 08 00 00 17 00 00 00 00 00 23")

esc=bytes.fromhex("57 AB 00 02 08 00 00 29 00 00 00 00 00 35")
F10=bytes.fromhex("57 AB 00 02 08 00 00 43 00 00 00 00 00 4F")


#数字1,2,3,4
s1=bytes.fromhex("57 AB 00 02 08 00 00 1E 00 00 00 00 00 2A")
s2=bytes.fromhex("57 AB 00 02 08 00 00 1F 00 00 00 00 00 2B")
s3=bytes.fromhex("57 AB 00 02 08 00 00 20 00 00 00 00 00 2C")
s4=bytes.fromhex("57 AB 00 02 08 00 00 21 00 00 00 00 00 2D")

#方向键：上下左右
ktop=bytes.fromhex("57 AB 00 02 08 00 00 52 00 00 00 00 00 5E")
kdown=bytes.fromhex("57 AB 00 02 08 00 00 51 00 00 00 00 00 5D")
kleft=bytes.fromhex("57 AB 00 02 08 00 00 50 00 00 00 00 00 5C")
kright=bytes.fromhex("57 AB 00 02 08 00 00 4F 00 00 00 00 00 5B")

#1,2,3,4
k1 = bytes.fromhex("57 AB 00 02 08 00 00 1E 00 00 00 00 00 2A")
k2 = bytes.fromhex("57 AB 00 02 08 00 00 1F 00 00 00 00 00 2B")
k3 = bytes.fromhex("57 AB 00 02 08 00 00 20 00 00 00 00 00 2C")
k4 = bytes.fromhex("57 AB 00 02 08 00 00 21 00 00 00 00 00 2D")



#鼠标左键
leftMouse = bytes.fromhex("57 AB 00 04 07 02 01 00 00 00 00 00 10")
#松开鼠标
mouseRelease = bytes.fromhex("57 AB 00 04 07 02 00 00 00 00 00 00 0F")


#键盘松开
def keyUp():
    ser.write(release)
    time.sleep(0.1)

#键盘按下
def keyPress(code):
    ser.write(code)
    time.sleep(0.1)
    ser.write(release)
    time.sleep(0.1)

#键盘按住不放
def keyDwon(code):
    ser.write(code)
    time.sleep(0.1)


#松开鼠标左键
def mouseUp():
    ser.write(mouseRelease)
    time.sleep(0.1)

#鼠标左键按下
def mousePress():
    ser.write(leftMouse)
    time.sleep(0.1)
    ser.write(mouseRelease)
    time.sleep(0.1)

#鼠标左键按住不放
def mouseDown():
    time.sleep(0.1)

#向上移动
def go_top():
    ser.write(ktop)
    time.sleep(0.1)

#向下移动
def go_down():
    ser.write(kdown)
    time.sleep(0.1)

#向左移动
def go_left():
    ser.write(kleft)
    time.sleep(0.1)

#向右移动
def go_right():
    ser.write(kright)
    time.sleep(0.1)

#移动鼠标
def mousemove(x,y):
    i=str(int(x*4096/1920))
    j=str(int(y*4096/1080))
    #print(i)  #213
    #print(j)  #379
    aliast=[]
    bliast=[]
    a=(hex((eval(i))))
    b=(hex((eval(j))))
    #print(a)   #0xd5
    #print(b)   #0x17b
    if len(a)==3: #三位变五位
        for i in a:
            aliast.append(i)
        a1="0x00"+str(aliast[2])
        #print(a1)
    if len(a)==4:#四位变五位
        for i in a:
            aliast.append(i)
        a1="0x0"+str(aliast[2])+str(aliast[3])
        #print(a1)    #0x0d5
    if len(a)==5:
        a1=a
        #print(a1)
    if len(b) == 3:  # 三位变五位
        for i in b:
            bliast.append(i)
        b1 = "0x00" + str(aliast[2])
        #print(b1)
    if len(b) == 4:  # 四位变五位
        for i in b:
            bliast.append(i)
        b1 = "0x0" + str(bliast[2]) + str(bliast[3])
        #print(b)      #0x17b
    if len(b) == 5:
        b1 = b
        #print(b1)
    aa=[]
    bb=[]
    for i in a1:
        aa.append(i)
    for j in b1:
        bb.append(j)
    #print(aa)        #['0', 'x', '0', 'd', '5']
    #print(bb)        #['0', 'x', '1', '7', 'b']
    int(aa[3]+aa[4],16)+int(aa[0]+aa[2],16)+int(bb[3]+bb[4],16)+int(bb[0]+bb[2],16)+15
    hex(int(aa[3]+aa[4],16)+int(aa[0]+aa[2],16)+int(bb[3]+bb[4],16)+int(bb[0]+bb[2],16)+15)
    cc=[]
    for i in hex(int(aa[3]+aa[4],16)+int(aa[0]+aa[2],16)+int(bb[3]+bb[4],16)+int(bb[0]+bb[2],16)+15):
        cc.append(i)
        #print(cc)
    #if len(hex(int(aa[3]+aa[4],16)+int(aa[0]+aa[2],16)+int(bb[3]+bb[4],16)+int(bb[0]+bb[2],16)+15))>4:
        #print("失败了",x,y)
    if len(cc) == 4:
        move="57 AB 00 04 07 02 00 "+aa[3]+aa[4]+" "+aa[0]+aa[2]+' '+bb[3]+bb[4]+' '+bb[0]+bb[2]+' '+'00'+' '+cc[2]+cc[3]
    else:
        move="57 AB 00 04 07 02 00 "+aa[3]+aa[4]+" "+aa[0]+aa[2]+' '+bb[3]+bb[4]+' '+bb[0]+bb[2]+' '+'00'+' '+cc[3]+cc[4]
    #print(int(aa[3]+aa[4],16)+int(aa[0]+aa[2],16)+int(bb[3]+bb[4],16)+int(bb[0]+bb[2],16)+15)
    #print(aa[3]+aa[4]+aa[0]+aa[2]+bb[3]+bb[4]+bb[0]+bb[2])
    #print(hex(int(aa[3]+aa[4],16)+int(aa[0]+aa[2],16)+int(bb[3]+bb[4],16)+int(bb[0]+bb[2],16)+15))
    #print(move)
    chuankou=bytes.fromhex(move)
    #songkai=bytes.fromhex("57 AB 00 02 08 00 00 00 00 00 00 00 00 0C")
    ser.write(chuankou)
    time.sleep(0)
    ser.write(release)

keyUp()
#mousemove(410,390)
#mousemove(410,300)

def random_skill():
    num = random.randint(1,8)
    if  num == 1:
        keyPress(a)
    elif num == 2:
        keyPress(s)
    elif num == 3:
        keyPress(d)
    elif num == 4:
        keyPress(f)
    elif num == 5:
        keyPress(q)
    elif num == 6:
        keyPress(w)
    elif num == 7:
        keyPress(e)
    elif num == 8:
        keyPress(r)

