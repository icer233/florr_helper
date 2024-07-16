from time import  sleep
import random
import datetime
import pyautogui
from PIL import ImageGrab,Image
from pynput.keyboard import Key,Controller
import tkinter
from tkinter import messagebox
import threading
import sys
import cv2
keyboard=Controller()
pyautogui.PAUSE = 0.01
AFK_common=Image.open("AFK_common.png")
AFK_unusual=Image.open("AFK_unusual.png")
AFK_rare=Image.open("AFK_rare.png")
AFK_epic=Image.open("AFK_epic.png")
AFK_legendary=Image.open("AFK_legendary.png") 
AFK_mythic=Image.open("AFK_mythic.png")
AFK_ultra=Image.open("AFK_ultra.png")
AFK_super=Image.open("AFK_super.png")
SPAWN_ultra=Image.open("Uspawn.png")
SPAWN_super=Image.open("Sspawn.png")
DF_ultra=Image.open("Udefeated.png")
DF_super=Image.open("Sdefeated.png")
sleep(2)
cnt=0
Ualive=False
Salive=False
autoatk=False
autoafk=False
yinyang=False
yy_using=False
UScheck=False
def tg_atk():
    global autoatk
    if autoatk==True:
        autoatk=False
        messagebox.showinfo(title='提示', message='自动攻击已关闭')
    else:
        autoatk=True
        messagebox.showinfo(title='提示', message='自动攻击已开启')
def tg_UScheck():
    global UScheck
    if UScheck==True:
        UScheck=False
        messagebox.showinfo(title='提示', message='US怪刷新提示已关闭')
    else:
        UScheck=True
        messagebox.showinfo(title='提示', message='US怪刷新提示已开启')
def tg_afk():
    global autoafk
    if autoafk==True:
        autoafk=False
        messagebox.showinfo(title='提示', message='auto afk 已关闭')
    else:
        autoafk=True
        messagebox.showinfo(title='可能有封号风险', message='auto afk 已开启')
def tg_yinyang():
    global yinyang
    global yy_using
    if yinyang==True:
        yinyang=False
        yy_using=False
    else:
        yinyang=True
def tg_yusing():
    global yy_using
    if yy_using==True:
        yy_using=False
    else:
        yy_using=True
def reset_alive():
    global Ualive
    global Salive
    Ualive=False
    Salive=False
def qt():
    sys.exit()
win=tkinter.Tk()
win.geometry('275x220')
win.title('florr helper')
print('start')
b1=tkinter.Button(win,text="开关自动攻击（按住空格键）",command=tg_atk)
b2=tkinter.Button(win,text="开关U/S提示",command=tg_UScheck)
b3=tkinter.Button(win,text="重置U/S存活状态（重置到死亡）",command=reset_alive)
b5=tkinter.Button(win,text="开关自动点击afk check（默认关闭）",command=tg_afk)
b6=tkinter.Button(win,text="开关自动阴阳,10槽填0,不填是1",command=tg_yinyang)
def validate_digit(i):
    global yinyang
    if i.isdigit() or i == "" and i.len()<=1:
        return True
    else:
        return False
lb1=tkinter.Label(win,text="洛谷553792 U/S生成识别不准确在改进\n据说auto afk有封号风险，慎用")
validate = win.register(validate_digit)
et1=tkinter.Entry(win, width=5, validate="key", validatecommand=(validate, "%S"))
b1.pack()
b2.pack()
b3.pack()
b5.pack()
b6.pack()
et1.pack()
lb1.pack()

def rdm():
    return random.randint(-10,10)

def jtl():
    sleep(random.uniform(0.3,0.8))

def some_task():
    global cnt
    global Ualive
    global Salive
    global autoatk
    global UScheck
    sleep(0.2)
    if autoatk:
        keyboard.press(Key.space)
    if((random.randint(0,4)==0) or (cnt==9)):
        cnt=0
    else:
        cnt=cnt+1
    if autoafk:
        msg=pyautogui.locateOnScreen(AFK_common,grayscale=False,confidence=0.72)
        if msg!=None:
            jtl()
            print(datetime.datetime.now().strftime('%H:%M:%S'),":Common AFK Check")
            x,y,w,h=msg
            x+=rdm()
            y+=rdm()
            w+=rdm()
            h+=rdm()
            pyautogui.click(x+w/2,y+h/2,button='left')
            jtl()
            pyautogui.click(x+w/2,y+h/2,button='left')
            jtl()
        msg=pyautogui.locateOnScreen(AFK_unusual,grayscale=False,confidence=0.72)
        if msg!=None:
            jtl()
            print(datetime.datetime.now().strftime('%H:%M:%S'),":Unusual AFK Check")
            x,y,w,h=msg
            x+=rdm()
            y+=rdm()
            w+=rdm()
            h+=rdm()
            pyautogui.click(x+w/2,y+h/2,button='left')
            jtl()
            pyautogui.click(x+w/2,y+h/2,button='left')
            jtl()
        msg=pyautogui.locateOnScreen(AFK_rare,grayscale=False,confidence=0.72)
        if msg!=None:
            jtl()
            print(datetime.datetime.now().strftime('%H:%M:%S'),":Rare AFK Check")
            x,y,w,h=msg
            x+=rdm()
            y+=rdm()
            w+=rdm()
            h+=rdm()
            pyautogui.click(x+w/2,y+h/2,button='left')
            jtl()
            pyautogui.click(x+w/2,y+h/2,button='left')
            jtl()
        msg=pyautogui.locateOnScreen(AFK_epic,grayscale=False,confidence=0.72)
        if msg!=None:
            jtl()
            print(datetime.datetime.now().strftime('%H:%M:%S'),":Epic AFK Check")
            x,y,w,h=msg
            x+=rdm()
            y+=rdm()
            w+=rdm()
            h+=rdm()
            pyautogui.click(x+w/2,y+h/2,button='left')
            jtl()
            pyautogui.click(x+w/2,y+h/2,button='left')
            jtl()
        msg=pyautogui.locateOnScreen(AFK_legendary,grayscale=False,confidence=0.72)
        if msg!=None:
            jtl()
            print(datetime.datetime.now().strftime('%H:%M:%S'),":Legendary AFK Check")
            x,y,w,h=msg
            x+=rdm()
            y+=rdm()
            w+=rdm()
            h+=rdm()
            pyautogui.click(x+w/2,y+h/2,button='left')
            jtl()
            pyautogui.click(x+w/2,y+h/2,button='left')
            jtl()
        msg=pyautogui.locateOnScreen(AFK_mythic,grayscale=False,confidence=0.72)
        if msg!=None:
            jtl()
            print(datetime.datetime.now().strftime('%H:%M:%S'),":Mythic AFK Check")
            x,y,w,h=msg
            x+=rdm()
            y+=rdm()
            w+=rdm()
            h+=rdm()
            pyautogui.click(x+w/2,y+h/2,button='left')
            jtl()
            pyautogui.click(x+w/2,y+h/2,button='left')
            jtl()
        msg=pyautogui.locateOnScreen(AFK_ultra,grayscale=False,confidence=0.72)
        if msg!=None:
            jtl()
            print(datetime.datetime.now().strftime('%H:%M:%S'),":Ultra AFK Check")
            x,y,w,h=msg
            x+=rdm()
            y+=rdm()
            w+=rdm()
            h+=rdm()
            pyautogui.click(x+w/2,y+h/2,button='left')
            jtl()
            pyautogui.click(x+w/2,y+h/2,button='left')
            jtl()
        msg=pyautogui.locateOnScreen(AFK_super,grayscale=False,confidence=0.72)
        if msg!=None:
            jtl()
            print(datetime.datetime.now().strftime('%H:%M:%S'),":Super AFK Check")
            x,y,w,h=msg
            x+=rdm()
            y+=rdm()
            w+=rdm()
            h+=rdm()
            pyautogui.click(x+w/2,y+h/2,button='left')
            jtl()
            pyautogui.click(x+w/2,y+h/2,button='left')
            jtl()
    msg=pyautogui.locateOnScreen(SPAWN_ultra,grayscale=False,confidence=0.62)
    if msg!=None and UScheck==True and Ualive==False:
        print(datetime.datetime.now().strftime('%H:%M:%S'),":Ultra spawn")
        messagebox.showinfo(title='Ultra spawn', message='Ultra spawn')
        Ualive=True
    msg=pyautogui.locateOnScreen(DF_ultra,grayscale=False,confidence=0.62)
    if msg!=None and UScheck==True and Ualive==True:
        print(datetime.datetime.now().strftime('%H:%M:%S'),":Ultra died")
        Ualive=False
    msg=pyautogui.locateOnScreen(SPAWN_super,grayscale=False,confidence=0.62)
    if msg!=None and UScheck==True and Salive==False:
        print(datetime.datetime.now().strftime('%H:%M:%S'),":Super spawn")
        messagebox.showinfo(title='Super spawn', message='Super spawn')
        Salive=True
    msg=pyautogui.locateOnScreen(DF_super,grayscale=False,confidence=0.62)
    if msg!=None and UScheck==True and Salive==True:
        print(datetime.datetime.now().strftime('%H:%M:%S'),":Super died")
        Salive=False
    some_task()
def yinyang_task():
    global yinyang
    global et1
    while True:
        if yinyang:
            et1.config(state='readonly')
            if et1.get()=='' or int(et1.get())>=9:
                k='1'
            else:
                k=str(et1.get())
            pyautogui.keyDown(k)
            sleep(random.uniform(0.02,0.3))
            pyautogui.keyUp(k)
            sleep(random.uniform(0.02,0.3))
        else:
            et1.config(state='normal')
        
        
win.wm_attributes("-topmost", True)
thread = threading.Thread(target=some_task)
thread.daemon = True
thread.start()
tr2=threading.Thread(target=yinyang_task)
tr2.deamon=True
tr2.start()


win.mainloop()
sys.exit()
