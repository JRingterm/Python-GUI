from tkinter import *
import math
import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import Spinbox
from tkinter import Menu
from tkinter import scrolledtext
from tkinter import messagebox as msg

a= Tk()
a.title("2019년")
a.geometry('530x400')

#종료하는 함수
def _quit():
    answer=msg.askyesno("종료","다이어리 달력을 종료하시겠습니까?")
    if answer == True:
        a.quit()
        a.destroy()
        exit()

#달력 설명 함수
def _explain():
    msg.showinfo('다이어리 달력 도움말',' 1.탭에서 달(month)을 선택할 수 있습니다.\n 2.일(day)에 해당하는 버튼을 누르면 일정을 입력하실 수 있습니  다.\n 3.종료를 원하신다면, 왼쪽상단 Menu에서 Quit을 눌러주세요.')

#메뉴바 생성
menu_bar = Menu(a)
a.config(menu=menu_bar)

#메뉴바 메뉴생성
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Explain", command=_explain)
file_menu.add_separator()
file_menu.add_command(label="Quit", command=_quit)
menu_bar.add_cascade(label="Menu", menu=file_menu)

#1월부터 12월까지의 달을 나타내는 탭==========================================
tabControl=ttk.Notebook(a)

Jan = ttk.Frame(tabControl)
tabControl.add(Jan, text='Jan')
Feb = ttk.Frame(tabControl)
tabControl.add(Feb, text='Feb')
Mar = ttk.Frame(tabControl)
tabControl.add(Mar, text='Mar')
Apr = ttk.Frame(tabControl)
tabControl.add(Apr, text='Apr')
May = ttk.Frame(tabControl)
tabControl.add(May, text='May')
Jun = ttk.Frame(tabControl)
tabControl.add(Jun, text='Jun')
Jul = ttk.Frame(tabControl)
tabControl.add(Jul, text='Jul')
Aug = ttk.Frame(tabControl)
tabControl.add(Aug, text='Aug')
Sep = ttk.Frame(tabControl)
tabControl.add(Sep, text='Sep')
Oct = ttk.Frame(tabControl)
tabControl.add(Oct, text='Oct')
Nov = ttk.Frame(tabControl)
tabControl.add(Nov, text='Nov')
Dec = ttk.Frame(tabControl)
tabControl.add(Dec, text='Dec')

tabControl.pack(expand=1, fill="both")
#=============================================================================

#일요일부터 토요일까지의 라벨을 표시해줌.=====================================
ttk.Label(Jan, text="Sun").grid(column=1, row=0)
ttk.Label(Jan, text="Mon").grid(column=2, row=0)
ttk.Label(Jan, text="Tue").grid(column=3, row=0)
ttk.Label(Jan, text="Wed").grid(column=4, row=0)
ttk.Label(Jan, text="Thu").grid(column=5, row=0)
ttk.Label(Jan, text="Fri").grid(column=6, row=0)
ttk.Label(Jan, text="Sat").grid(column=7, row=0)

ttk.Label(Feb, text="Sun").grid(column=1, row=0)
ttk.Label(Feb, text="Mon").grid(column=2, row=0)
ttk.Label(Feb, text="Tue").grid(column=3, row=0)
ttk.Label(Feb, text="Wed").grid(column=4, row=0)
ttk.Label(Feb, text="Thu").grid(column=5, row=0)
ttk.Label(Feb, text="Fri").grid(column=6, row=0)
ttk.Label(Feb, text="Sat").grid(column=7, row=0)

ttk.Label(Mar, text="Sun").grid(column=1, row=0)
ttk.Label(Mar, text="Mon").grid(column=2, row=0)
ttk.Label(Mar, text="Tue").grid(column=3, row=0)
ttk.Label(Mar, text="Wed").grid(column=4, row=0)
ttk.Label(Mar, text="Thu").grid(column=5, row=0)
ttk.Label(Mar, text="Fri").grid(column=6, row=0)
ttk.Label(Mar, text="Sat").grid(column=7, row=0)

ttk.Label(Apr, text="Sun").grid(column=1, row=0)
ttk.Label(Apr, text="Mon").grid(column=2, row=0)
ttk.Label(Apr, text="Tue").grid(column=3, row=0)
ttk.Label(Apr, text="Wed").grid(column=4, row=0)
ttk.Label(Apr, text="Thu").grid(column=5, row=0)
ttk.Label(Apr, text="Fri").grid(column=6, row=0)
ttk.Label(Apr, text="Sat").grid(column=7, row=0)

ttk.Label(May, text="Sun").grid(column=1, row=0)
ttk.Label(May, text="Mon").grid(column=2, row=0)
ttk.Label(May, text="Tue").grid(column=3, row=0)
ttk.Label(May, text="Wed").grid(column=4, row=0)
ttk.Label(May, text="Thu").grid(column=5, row=0)
ttk.Label(May, text="Fri").grid(column=6, row=0)
ttk.Label(May, text="Sat").grid(column=7, row=0)

ttk.Label(Jun, text="Sun").grid(column=1, row=0)
ttk.Label(Jun, text="Mon").grid(column=2, row=0)
ttk.Label(Jun, text="Tue").grid(column=3, row=0)
ttk.Label(Jun, text="Wed").grid(column=4, row=0)
ttk.Label(Jun, text="Thu").grid(column=5, row=0)
ttk.Label(Jun, text="Fri").grid(column=6, row=0)
ttk.Label(Jun, text="Sat").grid(column=7, row=0)

ttk.Label(Jul, text="Sun").grid(column=1, row=0)
ttk.Label(Jul, text="Mon").grid(column=2, row=0)
ttk.Label(Jul, text="Tue").grid(column=3, row=0)
ttk.Label(Jul, text="Wed").grid(column=4, row=0)
ttk.Label(Jul, text="Thu").grid(column=5, row=0)
ttk.Label(Jul, text="Fri").grid(column=6, row=0)
ttk.Label(Jul, text="Sat").grid(column=7, row=0)

ttk.Label(Aug, text="Sun").grid(column=1, row=0)
ttk.Label(Aug, text="Mon").grid(column=2, row=0)
ttk.Label(Aug, text="Tue").grid(column=3, row=0)
ttk.Label(Aug, text="Wed").grid(column=4, row=0)
ttk.Label(Aug, text="Thu").grid(column=5, row=0)
ttk.Label(Aug, text="Fri").grid(column=6, row=0)
ttk.Label(Aug, text="Sat").grid(column=7, row=0)

ttk.Label(Sep, text="Sun").grid(column=1, row=0)
ttk.Label(Sep, text="Mon").grid(column=2, row=0)
ttk.Label(Sep, text="Tue").grid(column=3, row=0)
ttk.Label(Sep, text="Wed").grid(column=4, row=0)
ttk.Label(Sep, text="Thu").grid(column=5, row=0)
ttk.Label(Sep, text="Fri").grid(column=6, row=0)
ttk.Label(Sep, text="Sat").grid(column=7, row=0)

ttk.Label(Oct, text="Sun").grid(column=1, row=0)
ttk.Label(Oct, text="Mon").grid(column=2, row=0)
ttk.Label(Oct, text="Tue").grid(column=3, row=0)
ttk.Label(Oct, text="Wed").grid(column=4, row=0)
ttk.Label(Oct, text="Thu").grid(column=5, row=0)
ttk.Label(Oct, text="Fri").grid(column=6, row=0)
ttk.Label(Oct, text="Sat").grid(column=7, row=0)

ttk.Label(Nov, text="Sun").grid(column=1, row=0)
ttk.Label(Nov, text="Mon").grid(column=2, row=0)
ttk.Label(Nov, text="Tue").grid(column=3, row=0)
ttk.Label(Nov, text="Wed").grid(column=4, row=0)
ttk.Label(Nov, text="Thu").grid(column=5, row=0)
ttk.Label(Nov, text="Fri").grid(column=6, row=0)
ttk.Label(Nov, text="Sat").grid(column=7, row=0)

ttk.Label(Dec, text="Sun").grid(column=1, row=0)
ttk.Label(Dec, text="Mon").grid(column=2, row=0)
ttk.Label(Dec, text="Tue").grid(column=3, row=0)
ttk.Label(Dec, text="Wed").grid(column=4, row=0)
ttk.Label(Dec, text="Thu").grid(column=5, row=0)
ttk.Label(Dec, text="Fri").grid(column=6, row=0)
ttk.Label(Dec, text="Sat").grid(column=7, row=0)
#================================================================================

##########################################################1월 시작#####################################################
#1월 n일을 입력하는 함수=========================================================
def Jansave1(self):
    value = work.get()
    scr1.insert(tk.INSERT, 'Day1 = ' + value + '\n')
    print('Jan Day1 schedule = ' + value + '\n')

def Jansave2(self):
    value = work.get()
    scr1.insert(tk.INSERT, 'Day2 = ' + value + '\n')
    print('Jan Day2 schedule = ' + value + '\n')

def Jansave3(self):
    value = work.get()
    scr1.insert(tk.INSERT, 'Day3 = ' + value + '\n')
    print('Jan Day3 schedule = ' + value + '\n')

def Jansave4(self):
    value = work.get()
    scr1.insert(tk.INSERT, 'Day4 = ' + value + '\n')
    print('Jan Day4 schedule = ' + value + '\n')

def Jansave5(self):
    value = work.get()
    scr1.insert(tk.INSERT, 'Day5 = ' + value + '\n')
    print('Jan Day5 schedule = ' + value + '\n')

def Jansave6(self):
    value = work.get()
    scr1.insert(tk.INSERT, 'Day6 = ' + value + '\n')
    print('Jan Day6 schedule = ' + value + '\n')

def Jansave7(self):
    value = work.get()
    scr1.insert(tk.INSERT, 'Day7 = ' + value + '\n')
    print('Jan Day7 schedule = ' + value + '\n')

def Jansave8(self):
    value = work.get()
    scr1.insert(tk.INSERT, 'Day8 = ' + value + '\n')
    print('Jan Day8 schedule = ' + value + '\n')

def Jansave9(self):
    value = work.get()
    scr1.insert(tk.INSERT, 'Day9 = ' + value + '\n')
    print('Jan Day9 schedule = ' + value + '\n')

def Jansave10(self):
    value = work.get()
    scr1.insert(tk.INSERT, 'Day10 = ' + value + '\n')
    print('Jan Day10 schedule = ' + value + '\n')

def Jansave11(self):
    value = work.get()
    scr1.insert(tk.INSERT, 'Day11 = ' + value + '\n')
    print('Jan Day11 schedule = ' + value + '\n')

def Jansave12(self):
    value = work.get()
    scr1.insert(tk.INSERT, 'Day12 = ' + value + '\n')
    print('Jan Day12 schedule = ' + value + '\n')

def Jansave13(self):
    value = work.get()
    scr1.insert(tk.INSERT, 'Day13 = ' + value + '\n')
    print('Jan Day13 schedule = ' + value + '\n')

def Jansave14(self):
    value = work.get()
    scr1.insert(tk.INSERT, 'Day14 = ' + value + '\n')
    print('Jan Day1 schedule = ' + value + '\n')

def Jansave15(self):
    value = work.get()
    scr1.insert(tk.INSERT, 'Day15 = ' + value + '\n')
    print('Jan Day15 schedule = ' + value + '\n')

def Jansave16(self):
    value = work.get()
    scr1.insert(tk.INSERT, 'Day16 = ' + value + '\n')
    print('Jan Day16 schedule = ' + value + '\n')

def Jansave17(self):
    value = work.get()
    scr1.insert(tk.INSERT, 'Day17 = ' + value + '\n')
    print('Jan Day17 schedule = ' + value + '\n')

def Jansave18(self):
    value = work.get()
    scr1.insert(tk.INSERT, 'Day18 = ' + value + '\n')
    print('Jan Day18 schedule = ' + value + '\n')

def Jansave19(self):
    value = work.get()
    scr1.insert(tk.INSERT, 'Day19 = ' + value + '\n')
    print('Jan Day19 schedule = ' + value + '\n')

def Jansave20(self):
    value = work.get()
    scr1.insert(tk.INSERT, 'Day20 = ' + value + '\n')
    print('Jan Day20 schedule = ' + value + '\n')

def Jansave21(self):
    value = work.get()
    scr1.insert(tk.INSERT, 'Day21 = ' + value + '\n')
    print('Jan Day21 schedule = ' + value + '\n')

def Jansave22(self):
    value = work.get()
    scr1.insert(tk.INSERT, 'Day22 = ' + value + '\n')
    print('Jan Day22 schedule = ' + value + '\n')

def Jansave23(self):
    value = work.get()
    scr1.insert(tk.INSERT, 'Day23 = ' + value + '\n')
    print('Jan Day23 schedule = ' + value + '\n')

def Jansave24(self):
    value = work.get()
    scr1.insert(tk.INSERT, 'Day24 = ' + value + '\n')
    print('Jan Day24 schedule = ' + value + '\n')

def Jansave25(self):
    value = work.get()
    scr1.insert(tk.INSERT, 'Day25 = ' + value + '\n')
    print('Jan Day25 schedule = ' + value + '\n')

def Jansave26(self):
    value = work.get()
    scr1.insert(tk.INSERT, 'Day26 = ' + value + '\n')
    print('Jan Day26 schedule = ' + value + '\n')

def Jansave27(self):
    value = work.get()
    scr1.insert(tk.INSERT, 'Day27 = ' + value + '\n')
    print('Jan Day27 schedule = ' + value + '\n')

def Jansave28(self):
    value = work.get()
    scr1.insert(tk.INSERT, 'Day28 = ' + value + '\n')
    print('Jan Day28 schedule = ' + value + '\n')

def Jansave29(self):
    value = work.get()
    scr1.insert(tk.INSERT, 'Day29 = ' + value + '\n')
    print('Jan Day29 schedule = ' + value + '\n')

def Jansave30(self):
    value = work.get()
    scr1.insert(tk.INSERT, 'Day30 = ' + value + '\n')
    print('Jan Day30 schedule = ' + value + '\n')

def Jansave31(self):
    value = work.get()
    scr1.insert(tk.INSERT, 'Day31 = ' + value + '\n')
    print('Jan Day31 schedule = ' + value + '\n')
#=============================================================================


#콜백되면 Entry가 생성되고, 입력시 스크롤텍스트에 출력할 수 있음 (일마다 하나씩 만들어줘야함)
def Jandiary1():
    global work
    global work_entered
    
    Label(Jan, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jan, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Jansave1)

def Jandiary2():
    global work
    global work_entered
    
    Label(Jan, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jan, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Jansave2)

def Jandiary3():
    global work
    global work_entered
    
    Label(Jan, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jan, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Jansave3)

def Jandiary4():
    global work
    global work_entered
    
    Label(Jan, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jan, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Jansave4)

def Jandiary5():
    global work
    global work_entered
    
    Label(Jan, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jan, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Jansave5)

def Jandiary6():
    global work
    global work_entered
    
    Label(Jan, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jan, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Jansave6)

def Jandiary7():
    global work
    global work_entered
    
    Label(Jan, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jan, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Jansave7)

def Jandiary8():
    global work
    global work_entered
    
    Label(Jan, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jan, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Jansave8)

def Jandiary9():
    global work
    global work_entered
    
    Label(Jan, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jan, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Jansave9)

def Jandiary10():
    global work
    global work_entered
    
    Label(Jan, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jan, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Jansave10)

def Jandiary11():
    global work
    global work_entered
    
    Label(Jan, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jan, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Jansave11)

def Jandiary12():
    global work
    global work_entered
    
    Label(Jan, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jan, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Jansave12)

def Jandiary13():
    global work
    global work_entered
    
    Label(Jan, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jan, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Jansave13)

def Jandiary14():
    global work
    global work_entered
    
    Label(Jan, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jan, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Jansave14)

def Jandiary15():
    global work
    global work_entered
    
    Label(Jan, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jan, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Jansave15)

def Jandiary16():
    global work
    global work_entered
    
    Label(Jan, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jan, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Jansave16)

def Jandiary17():
    global work
    global work_entered
    
    Label(Jan, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jan, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Jansave17)

def Jandiary18():
    global work
    global work_entered
    
    Label(Jan, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jan, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Jansave18)

def Jandiary19():
    global work
    global work_entered
    
    Label(Jan, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jan, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Jansave19)

def Jandiary20():
    global work
    global work_entered
    
    Label(Jan, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jan, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Jansave20)

def Jandiary21():
    global work
    global work_entered
    
    Label(Jan, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jan, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Jansave21)

def Jandiary22():
    global work
    global work_entered
    
    Label(Jan, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jan, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Jansave22)

def Jandiary23():
    global work
    global work_entered
    
    Label(Jan, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jan, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Jansave23)

def Jandiary24():
    global work
    global work_entered
    
    Label(Jan, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jan, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Jansave24)

def Jandiary25():
    global work
    global work_entered
    
    Label(Jan, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jan, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Jansave25)

def Jandiary26():
    global work
    global work_entered
    
    Label(Jan, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jan, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Jansave26)

def Jandiary27():
    global work
    global work_entered
    
    Label(Jan, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jan, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Jansave27)

def Jandiary28():
    global work
    global work_entered
    
    Label(Jan, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jan, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Jansave28)

def Jandiary29():
    global work
    global work_entered
    
    Label(Jan, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jan, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Jansave29)

def Jandiary30():
    global work
    global work_entered
    
    Label(Jan, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jan, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Jansav30)

def Jandiary31():
    global work
    global work_entered
    
    Label(Jan, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jan, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Jansave31)

#==============================================================================================


#1월 일정을 저장 할 scrolledtext 만듦 (1월부터 12월까지 다 해줘야함)===============================
scrol_w=30
scrol_h=12
scr1=scrolledtext.ScrolledText(Jan, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr1.grid(column=10, row=1,columnspan=6, rowspan=6)
#==============================================================================================
    

#1일 부터 월의 최대 일까지의 버튼을 만든다. 19년도 달력을 보고 요일과 일이 매치되도록 함 일일이...
    
#1월 달력판====================================================================================
day1 = Button(Jan, text=" 1 ",command = Jandiary1)
day1.grid(column=3, row=1)
day2 = Button(Jan, text=" 2 ",command = Jandiary2)
day2.grid(column=4, row=1)
day3 = Button(Jan, text=" 3 ",command = Jandiary3)
day3.grid(column=5, row=1)
day4 = Button(Jan, text=" 4 ",command = Jandiary4)
day4.grid(column=6, row=1)
day5 = Button(Jan, text=" 5 ",command = Jandiary5)
day5.grid(column=7, row=1)
day6 = Button(Jan, text=" 6 ",command = Jandiary6)
day6.grid(column=1, row=2)
day7 = Button(Jan, text=" 7 ",command = Jandiary7)
day7.grid(column=2, row=2)
day8 = Button(Jan, text=" 8 ",command = Jandiary8)
day8.grid(column=3, row=2)
day9 = Button(Jan, text=" 9 ",command = Jandiary9)
day9.grid(column=4, row=2)
day10 = Button(Jan, text="10",command = Jandiary10)
day10.grid(column=5, row=2)
day11 = Button(Jan, text="11",command = Jandiary11)
day11.grid(column=6, row=2)
day12 = Button(Jan, text="12",command = Jandiary12)
day12.grid(column=7, row=2)
day13 = Button(Jan, text="13",command = Jandiary13)
day13.grid(column=1, row=3)
day14 = Button(Jan, text="14",command = Jandiary14)
day14.grid(column=2, row=3)
day15 = Button(Jan, text="15",command = Jandiary15)
day15.grid(column=3, row=3)
day16 = Button(Jan, text="16",command = Jandiary16)
day16.grid(column=4, row=3)
day17 = Button(Jan, text="17",command = Jandiary17)
day17.grid(column=5, row=3)
day18 = Button(Jan, text="18",command = Jandiary18)
day18.grid(column=6, row=3)
day19 = Button(Jan, text="19",command = Jandiary19)
day19.grid(column=7, row=3)
day20 = Button(Jan, text="20",command = Jandiary20)
day20.grid(column=1, row=4)
day21 = Button(Jan, text="21",command = Jandiary21)
day21.grid(column=2, row=4)
day22 = Button(Jan, text="22",command = Jandiary22)
day22.grid(column=3, row=4)
day23 = Button(Jan, text="23",command = Jandiary23)
day23.grid(column=4, row=4)
day24 = Button(Jan, text="24",command = Jandiary24)
day24.grid(column=5, row=4)
day25 = Button(Jan, text="25",command = Jandiary25)
day25.grid(column=6, row=4)
day26 = Button(Jan, text="26",command = Jandiary26)
day26.grid(column=7, row=4)
day27 = Button(Jan, text="27",command = Jandiary27)
day27.grid(column=1, row=5)
day28 = Button(Jan, text="28",command = Jandiary28)
day28.grid(column=2, row=5)
day29 = Button(Jan, text="29",command = Jandiary29)
day29.grid(column=3, row=5)
day30 = Button(Jan, text="30",command = Jandiary30)
day30.grid(column=4, row=5)
day31 = Button(Jan, text="31",command = Jandiary31)
day31.grid(column=5, row=5)
#===============================================================================================
##########################################################1월 끝#####################################################

##########################################################2월 시작#####################################################
#2월 n일을 입력하는 함수=========================================================
def Febsave1(self):
    value = work.get()
    scr2.insert(tk.INSERT, 'Day1 = ' + value + '\n')
    print('Feb Day1 schedule = ' + value + '\n')

def Febsave2(self):
    value = work.get()
    scr2.insert(tk.INSERT, 'Day2 = ' + value + '\n')
    print('Feb Day2 schedule = ' + value + '\n')

def Febsave3(self):
    value = work.get()
    scr2.insert(tk.INSERT, 'Day3 = ' + value + '\n')
    print('Feb Day3 schedule = ' + value + '\n')

def Febsave4(self):
    value = work.get()
    scr2.insert(tk.INSERT, 'Day4 = ' + value + '\n')
    print('Feb Day4 schedule = ' + value + '\n')

def Febsave5(self):
    value = work.get()
    scr2.insert(tk.INSERT, 'Day5 = ' + value + '\n')
    print('Feb Day5 schedule = ' + value + '\n')

def Febsave6(self):
    value = work.get()
    scr2.insert(tk.INSERT, 'Day6 = ' + value + '\n')
    print('Feb Day6 schedule = ' + value + '\n')

def Febsave7(self):
    value = work.get()
    scr2.insert(tk.INSERT, 'Day7 = ' + value + '\n')
    print('Feb Day7 schedule = ' + value + '\n')

def Febsave8(self):
    value = work.get()
    scr2.insert(tk.INSERT, 'Day8 = ' + value + '\n')
    print('Feb Day8 schedule = ' + value + '\n')

def Febsave9(self):
    value = work.get()
    scr.insert(tk.INSERT, 'Day9 = ' + value + '\n')
    print('Feb Day9 schedule = ' + value + '\n')

def Febsave10(self):
    value = work.get()
    scr2.insert(tk.INSERT, 'Day10 = ' + value + '\n')
    print('Feb Day10 schedule = ' + value + '\n')

def Febsave11(self):
    value = work.get()
    scr2.insert(tk.INSERT, 'Day11 = ' + value + '\n')
    print('Feb Day11 schedule = ' + value + '\n')

def Febsave12(self):
    value = work.get()
    scr2.insert(tk.INSERT, 'Day12 = ' + value + '\n')
    print('Feb Day12 schedule = ' + value + '\n')

def Febsave13(self):
    value = work.get()
    scr2.insert(tk.INSERT, 'Day13 = ' + value + '\n')
    print('Feb Day13 schedule = ' + value + '\n')

def Febsave14(self):
    value = work.get()
    scr2.insert(tk.INSERT, 'Day14 = ' + value + '\n')
    print('Feb Day1 schedule = ' + value + '\n')

def Febsave15(self):
    value = work.get()
    scr2.insert(tk.INSERT, 'Day15 = ' + value + '\n')
    print('Feb Day15 schedule = ' + value + '\n')

def Febsave16(self):
    value = work.get()
    scr2.insert(tk.INSERT, 'Day16 = ' + value + '\n')
    print('Feb Day16 schedule = ' + value + '\n')

def Febsave17(self):
    value = work.get()
    scr2.insert(tk.INSERT, 'Day17 = ' + value + '\n')
    print('Feb Day17 schedule = ' + value + '\n')

def Febsave18(self):
    value = work.get()
    scr2.insert(tk.INSERT, 'Day18 = ' + value + '\n')
    print('Feb Day18 schedule = ' + value + '\n')

def Febsave19(self):
    value = work.get()
    scr2.insert(tk.INSERT, 'Day19 = ' + value + '\n')
    print('Feb Day19 schedule = ' + value + '\n')

def Febsave20(self):
    value = work.get()
    scr2.insert(tk.INSERT, 'Day20 = ' + value + '\n')
    print('Feb Day20 schedule = ' + value + '\n')

def Febsave21(self):
    value = work.get()
    scr2.insert(tk.INSERT, 'Day21 = ' + value + '\n')
    print('Feb Day21 schedule = ' + value + '\n')

def Febsave22(self):
    value = work.get()
    scr2.insert(tk.INSERT, 'Day22 = ' + value + '\n')
    print('Feb Day22 schedule = ' + value + '\n')

def Febsave23(self):
    value = work.get()
    scr2.insert(tk.INSERT, 'Day23 = ' + value + '\n')
    print('Feb Day23 schedule = ' + value + '\n')

def Febsave24(self):
    value = work.get()
    scr2.insert(tk.INSERT, 'Day24 = ' + value + '\n')
    print('Feb Day24 schedule = ' + value + '\n')

def Febsave25(self):
    value = work.get()
    scr2.insert(tk.INSERT, 'Day25 = ' + value + '\n')
    print('Feb Day25 schedule = ' + value + '\n')

def Febsave26(self):
    value = work.get()
    scr2.insert(tk.INSERT, 'Day26 = ' + value + '\n')
    print('Feb Day26 schedule = ' + value + '\n')

def Febsave27(self):
    value = work.get()
    scr2.insert(tk.INSERT, 'Day27 = ' + value + '\n')
    print('Feb Day27 schedule = ' + value + '\n')

def Febsave28(self):
    value = work.get()
    scr2.insert(tk.INSERT, 'Day28 = ' + value + '\n')
    print('Feb Day28 schedule = ' + value + '\n')

#====================================================================


#콜백되면 Entry가 생성되고, 스크롤텍스트에 출력할 수 있음. (일마다 하나씩 만들어줘야함)
def Febdiary1():
    global work
    global work_entered
    
    Label(Feb, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Feb, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Febsave1)

def Febdiary2():
    global work
    global work_entered
    
    Label(Feb, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Feb, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Febsave2)

def Febdiary3():
    global work
    global work_entered
    
    Label(Feb, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Feb, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Febsave3)

def Febdiary4():
    global work
    global work_entered
    
    Label(Feb, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Feb, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Febsave4)

def Febdiary5():
    global work
    global work_entered
    
    Label(Feb, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Feb, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Febsave5)

def Febdiary6():
    global work
    global work_entered
    
    Label(Feb, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Feb, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Febsave6)

def Febdiary7():
    global work
    global work_entered
    
    Label(Feb, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Feb, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Febsave7)

def Febdiary8():
    global work
    global work_entered
    
    Label(Feb, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Feb, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Febsave8)

def Febdiary9():
    global work
    global work_entered
    
    Label(Feb, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Feb, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Febsave9)

def Febdiary10():
    global work
    global work_entered
    
    Label(Feb, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Feb, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Febsave10)

def Febdiary11():
    global work
    global work_entered
    
    Label(Feb, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Feb, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Febsave11)

def Febdiary12():
    global work
    global work_entered
    
    Label(Feb, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Feb, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Febsave12)

def Febdiary13():
    global work
    global work_entered
    
    Label(Feb, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Feb, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Febsave13)

def Febdiary14():
    global work
    global work_entered
    
    Label(Feb, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Feb, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Febsave14)

def Febdiary15():
    global work
    global work_entered
    
    Label(Feb, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Feb, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Febsave15)

def Febdiary16():
    global work
    global work_entered
    
    Label(Feb, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Feb, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Febsave16)

def Febdiary17():
    global work
    global work_entered
    
    Label(Feb, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Feb, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Febsave17)

def Febdiary18():
    global work
    global work_entered
    
    Label(Feb, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Feb, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Febsave18)

def Febdiary19():
    global work
    global work_entered
    
    Label(Feb, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Feb, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Febsave19)

def Febdiary20():
    global work
    global work_entered
    
    Label(Feb, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Feb, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Febsave20)

def Febdiary21():
    global work
    global work_entered
    
    Label(Feb, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Feb, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Febsave21)

def Febdiary22():
    global work
    global work_entered
    
    Label(Feb, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Feb, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Febsave22)

def Febdiary23():
    global work
    global work_entered
    
    Label(Feb, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Feb, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Febsave23)

def Febdiary24():
    global work
    global work_entered
    
    Label(Feb, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Feb, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Febsave24)

def Febdiary25():
    global work
    global work_entered
    
    Label(Feb, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Feb, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Febsave25)

def Febdiary26():
    global work
    global work_entered
    
    Label(Feb, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Feb, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Febsave26)

def Febdiary27():
    global work
    global work_entered
    
    Label(Feb, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Feb, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Febsave27)

def Febdiary28():
    global work
    global work_entered
    
    Label(Feb, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Feb, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Febsave28)


#==============================================================================================
      
    

#2월 일정을 저장 할 scrolledtext 만듦 (1월부터 12월까지 다 해줘야함)===============================
scrol_w=30
scrol_h=12
scr2=scrolledtext.ScrolledText(Feb, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr2.grid(column=10, row=1,columnspan=6, rowspan=6)
#==============================================================================================
    

#1일 부터 월의 최대 일까지의 버튼을 만든다. 19년도 달력을 보고 요일과 일이 매치되도록 함 일일이...
    
#2월 달력판====================================================================================
day1 = Button(Feb, text=" 1 ",command = Febdiary1)
day1.grid(column=6, row=1)
day2 = Button(Feb, text=" 2 ",command = Febdiary2)
day2.grid(column=7, row=1)
day3 = Button(Feb, text=" 3 ",command = Febdiary3)
day3.grid(column=1, row=2)
day4 = Button(Feb, text=" 4 ",command = Febdiary4)
day4.grid(column=2, row=2)
day5 = Button(Feb, text=" 5 ",command = Febdiary5)
day5.grid(column=3, row=2)
day6 = Button(Feb, text=" 6 ",command = Febdiary6)
day6.grid(column=4, row=2)
day7 = Button(Feb, text=" 7 ",command = Febdiary7)
day7.grid(column=5, row=2)
day8 = Button(Feb, text=" 8 ",command = Febdiary8)
day8.grid(column=6, row=2)
day9 = Button(Feb, text=" 9 ",command = Febdiary9)
day9.grid(column=7, row=2)
day10 = Button(Feb, text="10",command = Febdiary10)
day10.grid(column=1, row=3)
day11 = Button(Feb, text="11",command = Febdiary11)
day11.grid(column=2, row=3)
day12 = Button(Feb, text="12",command = Febdiary12)
day12.grid(column=3, row=3)
day13 = Button(Feb, text="13",command = Febdiary13)
day13.grid(column=4, row=3)
day14 = Button(Feb, text="14",command = Febdiary14)
day14.grid(column=5, row=3)
day15 = Button(Feb, text="15",command = Febdiary15)
day15.grid(column=6, row=3)
day16 = Button(Feb, text="16",command = Febdiary16)
day16.grid(column=7, row=3)
day17 = Button(Feb, text="17",command = Febdiary17)
day17.grid(column=1, row=4)
day18 = Button(Feb, text="18",command = Febdiary18)
day18.grid(column=2, row=4)
day19 = Button(Feb, text="19",command = Febdiary19)
day19.grid(column=3, row=4)
day20 = Button(Feb, text="20",command = Febdiary20)
day20.grid(column=4, row=4)
day21 = Button(Feb, text="21",command = Febdiary21)
day21.grid(column=5, row=4)
day22 = Button(Feb, text="22",command = Febdiary22)
day22.grid(column=6, row=4)
day23 = Button(Feb, text="23",command = Febdiary23)
day23.grid(column=7, row=4)
day24 = Button(Feb, text="24",command = Febdiary24)
day24.grid(column=1, row=5)
day25 = Button(Feb, text="25",command = Febdiary25)
day25.grid(column=2, row=5)
day26 = Button(Feb, text="26",command = Febdiary26)
day26.grid(column=3, row=5)
day27 = Button(Feb, text="27",command = Febdiary27)
day27.grid(column=4, row=5)
day28 = Button(Feb, text="28",command = Febdiary28)
day28.grid(column=5, row=5)

#===============================================================================================
##########################################################2월 끝#####################################################

##########################################################3월 시작#####################################################
#3월 n일을 입력하는 함수=========================================================
def Marsave1(self):
    value = work.get()
    scr3.insert(tk.INSERT, 'Day1 = ' + value + '\n')
    print('Mar Day1 schedule = ' + value + '\n')

def Marsave2(self):
    value = work.get()
    scr3.insert(tk.INSERT, 'Day2 = ' + value + '\n')
    print('Mar Day2 schedule = ' + value + '\n')

def Marsave3(self):
    value = work.get()
    scr3.insert(tk.INSERT, 'Day3 = ' + value + '\n')
    print('Mar Day3 schedule = ' + value + '\n')

def Marsave4(self):
    value = work.get()
    scr3.insert(tk.INSERT, 'Day4 = ' + value + '\n')
    print('Mar Day4 schedule = ' + value + '\n')

def Marsave5(self):
    value = work.get()
    scr3.insert(tk.INSERT, 'Day5 = ' + value + '\n')
    print('Mar Day5 schedule = ' + value + '\n')

def Marsave6(self):
    value = work.get()
    scr3.insert(tk.INSERT, 'Day6 = ' + value + '\n')
    print('Mar Day6 schedule = ' + value + '\n')

def Marsave7(self):
    value = work.get()
    scr3.insert(tk.INSERT, 'Day7 = ' + value + '\n')
    print('Mar Day7 schedule = ' + value + '\n')

def Marsave8(self):
    value = work.get()
    scr3.insert(tk.INSERT, 'Day8 = ' + value + '\n')
    print('Mar Day8 schedule = ' + value + '\n')

def Marsave9(self):
    value = work.get()
    scr3.insert(tk.INSERT, 'Day9 = ' + value + '\n')
    print('Mar Day9 schedule = ' + value + '\n')

def Marsave10(self):
    value = work.get()
    scr3.insert(tk.INSERT, 'Day10 = ' + value + '\n')
    print('Mar Day10 schedule = ' + value + '\n')

def Marsave11(self):
    value = work.get()
    scr3.insert(tk.INSERT, 'Day11 = ' + value + '\n')
    print('Mar Day11 schedule = ' + value + '\n')

def Marsave12(self):
    value = work.get()
    scr3.insert(tk.INSERT, 'Day12 = ' + value + '\n')
    print('Mar Day12 schedule = ' + value + '\n')

def Marsave13(self):
    value = work.get()
    scr3.insert(tk.INSERT, 'Day13 = ' + value + '\n')
    print('Mar Day13 schedule = ' + value + '\n')

def Marsave14(self):
    value = work.get()
    scr3.insert(tk.INSERT, 'Day14 = ' + value + '\n')
    print('Mar Day1 schedule = ' + value + '\n')

def Marsave15(self):
    value = work.get()
    scr3.insert(tk.INSERT, 'Day15 = ' + value + '\n')
    print('Mar Day15 schedule = ' + value + '\n')

def Marsave16(self):
    value = work.get()
    scr3.insert(tk.INSERT, 'Day16 = ' + value + '\n')
    print('Mar Day16 schedule = ' + value + '\n')

def Marsave17(self):
    value = work.get()
    scr3.insert(tk.INSERT, 'Day17 = ' + value + '\n')
    print('Mar Day17 schedule = ' + value + '\n')

def Marsave18(self):
    value = work.get()
    scr3.insert(tk.INSERT, 'Day18 = ' + value + '\n')
    print('Mar Day18 schedule = ' + value + '\n')

def Marsave19(self):
    value = work.get()
    scr3.insert(tk.INSERT, 'Day19 = ' + value + '\n')
    print('Mar Day19 schedule = ' + value + '\n')

def Marsave20(self):
    value = work.get()
    scr3.insert(tk.INSERT, 'Day20 = ' + value + '\n')
    print('Mar Day20 schedule = ' + value + '\n')

def Marsave21(self):
    value = work.get()
    scr3.insert(tk.INSERT, 'Day21 = ' + value + '\n')
    print('Mar Day21 schedule = ' + value + '\n')

def Marsave22(self):
    value = work.get()
    scr3.insert(tk.INSERT, 'Day22 = ' + value + '\n')
    print('Mar Day22 schedule = ' + value + '\n')

def Marsave23(self):
    value = work.get()
    scr3.insert(tk.INSERT, 'Day23 = ' + value + '\n')
    print('Mar Day23 schedule = ' + value + '\n')

def Marsave24(self):
    value = work.get()
    scr3.insert(tk.INSERT, 'Day24 = ' + value + '\n')
    print('Mar Day24 schedule = ' + value + '\n')

def Marsave25(self):
    value = work.get()
    scr3.insert(tk.INSERT, 'Day25 = ' + value + '\n')
    print('Mar Day25 schedule = ' + value + '\n')

def Marsave26(self):
    value = work.get()
    scr3.insert(tk.INSERT, 'Day26 = ' + value + '\n')
    print('Mar Day26 schedule = ' + value + '\n')

def Marsave27(self):
    value = work.get()
    scr3.insert(tk.INSERT, 'Day27 = ' + value + '\n')
    print('Mar Day27 schedule = ' + value + '\n')

def Marsave28(self):
    value = work.get()
    scr3.insert(tk.INSERT, 'Day28 = ' + value + '\n')
    print('Mar Day28 schedule = ' + value + '\n')

def Marsave29(self):
    value = work.get()
    scr3.insert(tk.INSERT, 'Day29 = ' + value + '\n')
    print('Mar Day29 schedule = ' + value + '\n')

def Marsave30(self):
    value = work.get()
    scr3.insert(tk.INSERT, 'Day30 = ' + value + '\n')
    print('Mar Day30 schedule = ' + value + '\n')

def Marsave31(self):
    value = work.get()
    scr3.insert(tk.INSERT, 'Day31 = ' + value + '\n')
    print('Mar Day31 schedule = ' + value + '\n')
#============================================================


#콜백되면 Entry가 생성되고, 입력시 스크롤텍스트에 출력할 수 있음 (일마다 하나씩 만들어줘야함)
def Mardiary1():
    global work
    global work_entered
    
    Label(Mar, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Mar, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Marsave1)

def Mardiary2():
    global work
    global work_entered
    
    Label(Mar, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Mar, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Marsave2)

def Mardiary3():
    global work
    global work_entered
    
    Label(Mar, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Mar, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Marsave3)

def Mardiary4():
    global work
    global work_entered
    
    Label(Mar, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Mar, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Marsave4)

def Mardiary5():
    global work
    global work_entered
    
    Label(Mar, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Mar, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Marsave5)

def Mardiary6():
    global work
    global work_entered
    
    Label(Mar, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Mar, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Marsave6)

def Mardiary7():
    global work
    global work_entered
    
    Label(Mar, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Mar, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Marsave7)

def Mardiary8():
    global work
    global work_entered
    
    Label(Mar, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Mar, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Marsave8)

def Mardiary9():
    global work
    global work_entered
    
    Label(Mar, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Mar, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Marsave9)

def Mardiary10():
    global work
    global work_entered
    
    Label(Mar, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Mar, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Marsave10)

def Mardiary11():
    global work
    global work_entered
    
    Label(Mar, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Mar, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Marsave11)

def Mardiary12():
    global work
    global work_entered
    
    Label(Mar, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Mar, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Marsave12)

def Mardiary13():
    global work
    global work_entered
    
    Label(Mar, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Mar, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Marsave13)

def Mardiary14():
    global work
    global work_entered
    
    Label(Mar, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Mar, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Marsave14)

def Mardiary15():
    global work
    global work_entered
    
    Label(Mar, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Mar, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Marsave15)

def Mardiary16():
    global work
    global work_entered
    
    Label(Mar, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Mar, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Marsave16)

def Mardiary17():
    global work
    global work_entered
    
    Label(Mar, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Mar, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Marsave17)

def Mardiary18():
    global work
    global work_entered
    
    Label(Mar, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Mar, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Marsave18)

def Mardiary19():
    global work
    global work_entered
    
    Label(Mar, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Mar, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Marsave19)

def Mardiary20():
    global work
    global work_entered
    
    Label(Mar, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Mar, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Marsave20)

def Mardiary21():
    global work
    global work_entered
    
    Label(Mar, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Mar, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Marsave21)

def Mardiary22():
    global work
    global work_entered
    
    Label(Mar, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Mar, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Marsave22)

def Mardiary23():
    global work
    global work_entered
    
    Label(Mar, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Mar, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Marsave23)

def Mardiary24():
    global work
    global work_entered
    
    Label(Mar, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Mar, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Marsave24)

def Mardiary25():
    global work
    global work_entered
    
    Label(Mar, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Mar, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Marsave25)

def Mardiary26():
    global work
    global work_entered
    
    Label(Mar, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Mar, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Marsave26)

def Mardiary27():
    global work
    global work_entered
    
    Label(Mar, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Mar, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Marsave27)

def Mardiary28():
    global work
    global work_entered
    
    Label(Mar, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Mar, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Marsave28)

def Mardiary29():
    global work
    global work_entered
    
    Label(Mar, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Mar, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Marsave29)

def Mardiary30():
    global work
    global work_entered
    
    Label(Mar, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Mar, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Marsav30)

def Mardiary31():
    global work
    global work_entered
    
    Label(Mar, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Mar, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Marsave31)

#==============================================================================================
      
    

#3월 일정을 저장 할 scrolledtext 만듦 (1월부터 12월까지 다 해줘야함)===============================
scrol_w=30
scrol_h=12
scr3=scrolledtext.ScrolledText(Mar, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr3.grid(column=10, row=1,columnspan=6, rowspan=6)
#==============================================================================================
    

#1일 부터 월의 최대 일까지의 버튼을 만든다. 19년도 달력을 보고 요일과 일이 매치되도록 함 일일이...
    
#3월 달력판====================================================================================
day1 = Button(Mar, text=" 1 ",command = Mardiary1)
day1.grid(column=6, row=1)
day2 = Button(Mar, text=" 2 ",command = Mardiary2)
day2.grid(column=7, row=1)
day3 = Button(Mar, text=" 3 ",command = Mardiary3)
day3.grid(column=1, row=2)
day4 = Button(Mar, text=" 4 ",command = Mardiary4)
day4.grid(column=2, row=2)
day5 = Button(Mar, text=" 5 ",command = Mardiary5)
day5.grid(column=3, row=2)
day6 = Button(Mar, text=" 6 ",command = Mardiary6)
day6.grid(column=4, row=2)
day7 = Button(Mar, text=" 7 ",command = Mardiary7)
day7.grid(column=5, row=2)
day8 = Button(Mar, text=" 8 ",command = Mardiary8)
day8.grid(column=6, row=2)
day9 = Button(Mar, text=" 9 ",command = Mardiary9)
day9.grid(column=7, row=2)
day10 = Button(Mar, text="10",command = Mardiary10)
day10.grid(column=1, row=3)
day11 = Button(Mar, text="11",command = Mardiary11)
day11.grid(column=2, row=3)
day12 = Button(Mar, text="12",command = Mardiary12)
day12.grid(column=3, row=3)
day13 = Button(Mar, text="13",command = Mardiary13)
day13.grid(column=4, row=3)
day14 = Button(Mar, text="14",command = Mardiary14)
day14.grid(column=5, row=3)
day15 = Button(Mar, text="15",command = Mardiary15)
day15.grid(column=6, row=3)
day16 = Button(Mar, text="16",command = Mardiary16)
day16.grid(column=7, row=3)
day17 = Button(Mar, text="17",command = Mardiary17)
day17.grid(column=1, row=4)
day18 = Button(Mar, text="18",command = Mardiary18)
day18.grid(column=2, row=4)
day19 = Button(Mar, text="19",command = Mardiary19)
day19.grid(column=3, row=4)
day20 = Button(Mar, text="20",command = Mardiary20)
day20.grid(column=4, row=4)
day21 = Button(Mar, text="21",command = Mardiary21)
day21.grid(column=5, row=4)
day22 = Button(Mar, text="22",command = Mardiary22)
day22.grid(column=6, row=4)
day23 = Button(Mar, text="23",command = Mardiary23)
day23.grid(column=7, row=4)
day24 = Button(Mar, text="24",command = Mardiary24)
day24.grid(column=1, row=5)
day25 = Button(Mar, text="25",command = Mardiary25)
day25.grid(column=2, row=5)
day26 = Button(Mar, text="26",command = Mardiary26)
day26.grid(column=3, row=5)
day27 = Button(Mar, text="27",command = Mardiary27)
day27.grid(column=4, row=5)
day28 = Button(Mar, text="28",command = Mardiary28)
day28.grid(column=5, row=5)
day29 = Button(Mar, text="29",command = Mardiary29)
day29.grid(column=6, row=5)
day30 = Button(Mar, text="30",command = Mardiary30)
day30.grid(column=7, row=5)
day31 = Button(Mar, text="31",command = Mardiary31)
day31.grid(column=1, row=6)
#===============================================================================================
##########################################################3월 끝#####################################################

##########################################################4월 시작#####################################################
#4월 n일을 입력하는 함수=========================================================
def Aprsave1(self):
    value = work.get()
    scr4.insert(tk.INSERT, 'Day1 = ' + value + '\n')
    print('Apr Day1 schedule = ' + value + '\n')

def Aprsave2(self):
    value = work.get()
    scr4.insert(tk.INSERT, 'Day2 = ' + value + '\n')
    print('Apr Day2 schedule = ' + value + '\n')

def Aprsave3(self):
    value = work.get()
    scr4.insert(tk.INSERT, 'Day3 = ' + value + '\n')
    print('Apr Day3 schedule = ' + value + '\n')

def Aprsave4(self):
    value = work.get()
    scr4.insert(tk.INSERT, 'Day4 = ' + value + '\n')
    print('Apr Day4 schedule = ' + value + '\n')

def Aprsave5(self):
    value = work.get()
    scr4.insert(tk.INSERT, 'Day5 = ' + value + '\n')
    print('Apr Day5 schedule = ' + value + '\n')

def Aprsave6(self):
    value = work.get()
    scr4.insert(tk.INSERT, 'Day6 = ' + value + '\n')
    print('Apr Day6 schedule = ' + value + '\n')

def Aprsave7(self):
    value = work.get()
    scr4.insert(tk.INSERT, 'Day7 = ' + value + '\n')
    print('Apr Day7 schedule = ' + value + '\n')

def Aprsave8(self):
    value = work.get()
    scr4.insert(tk.INSERT, 'Day8 = ' + value + '\n')
    print('Apr Day8 schedule = ' + value + '\n')

def Aprsave9(self):
    value = work.get()
    scr4.insert(tk.INSERT, 'Day9 = ' + value + '\n')
    print('Apr Day9 schedule = ' + value + '\n')

def Aprsave10(self):
    value = work.get()
    scr4.insert(tk.INSERT, 'Day10 = ' + value + '\n')
    print('Apr Day10 schedule = ' + value + '\n')

def Aprsave11(self):
    value = work.get()
    scr4.insert(tk.INSERT, 'Day11 = ' + value + '\n')
    print('Apr Day11 schedule = ' + value + '\n')

def Aprsave12(self):
    value = work.get()
    scr4.insert(tk.INSERT, 'Day12 = ' + value + '\n')
    print('Apr Day12 schedule = ' + value + '\n')

def Aprsave13(self):
    value = work.get()
    scr4.insert(tk.INSERT, 'Day13 = ' + value + '\n')
    print('Apr Day13 schedule = ' + value + '\n')

def Aprsave14(self):
    value = work.get()
    scr4.insert(tk.INSERT, 'Day14 = ' + value + '\n')
    print('Apr Day1 schedule = ' + value + '\n')

def Aprsave15(self):
    value = work.get()
    scr4.insert(tk.INSERT, 'Day15 = ' + value + '\n')
    print('Apr Day15 schedule = ' + value + '\n')

def Aprsave16(self):
    value = work.get()
    scr4.insert(tk.INSERT, 'Day16 = ' + value + '\n')
    print('Apr Day16 schedule = ' + value + '\n')

def Aprsave17(self):
    value = work.get()
    scr4.insert(tk.INSERT, 'Day17 = ' + value + '\n')
    print('Apr Day17 schedule = ' + value + '\n')

def Aprsave18(self):
    value = work.get()
    scr4.insert(tk.INSERT, 'Day18 = ' + value + '\n')
    print('Apr Day18 schedule = ' + value + '\n')

def Aprsave19(self):
    value = work.get()
    scr4.insert(tk.INSERT, 'Day19 = ' + value + '\n')
    print('Apr Day19 schedule = ' + value + '\n')

def Aprsave20(self):
    value = work.get()
    scr4.insert(tk.INSERT, 'Day20 = ' + value + '\n')
    print('Apr Day20 schedule = ' + value + '\n')

def Aprsave21(self):
    value = work.get()
    scr4.insert(tk.INSERT, 'Day21 = ' + value + '\n')
    print('Apr Day21 schedule = ' + value + '\n')

def Aprsave22(self):
    value = work.get()
    scr4.insert(tk.INSERT, 'Day22 = ' + value + '\n')
    print('Apr Day22 schedule = ' + value + '\n')

def Aprsave23(self):
    value = work.get()
    scr4.insert(tk.INSERT, 'Day23 = ' + value + '\n')
    print('Apr Day23 schedule = ' + value + '\n')

def Aprsave24(self):
    value = work.get()
    scr4.insert(tk.INSERT, 'Day24 = ' + value + '\n')
    print('Apr Day24 schedule = ' + value + '\n')

def Aprsave25(self):
    value = work.get()
    scr4.insert(tk.INSERT, 'Day25 = ' + value + '\n')
    print('Apr Day25 schedule = ' + value + '\n')

def Aprsave26(self):
    value = work.get()
    scr4.insert(tk.INSERT, 'Day26 = ' + value + '\n')
    print('Apr Day26 schedule = ' + value + '\n')

def Aprsave27(self):
    value = work.get()
    scr4.insert(tk.INSERT, 'Day27 = ' + value + '\n')
    print('Apr Day27 schedule = ' + value + '\n')

def Aprsave28(self):
    value = work.get()
    scr4.insert(tk.INSERT, 'Day28 = ' + value + '\n')
    print('Apr Day28 schedule = ' + value + '\n')

def Aprsave29(self):
    value = work.get()
    scr4.insert(tk.INSERT, 'Day29 = ' + value + '\n')
    print('Apr Day29 schedule = ' + value + '\n')

def Aprsave30(self):
    value = work.get()
    scr4.insert(tk.INSERT, 'Day30 = ' + value + '\n')
    print('Apr Day30 schedule = ' + value + '\n')

#============================================================


#콜백되면 Entry가 생성되고, 입력시 스크롤텍스트에 출력할 수 있음 (일마다 하나씩 만들어줘야함)
def Aprdiary1():
    global work
    global work_entered
    
    Label(Apr, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Apr, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Aprsave1)

def Aprdiary2():
    global work
    global work_entered
    
    Label(Apr, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Apr, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Aprsave2)

def Aprdiary3():
    global work
    global work_entered
    
    Label(Apr, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Apr, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Aprsave3)

def Aprdiary4():
    global work
    global work_entered
    
    Label(Apr, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Apr, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Aprsave4)

def Aprdiary5():
    global work
    global work_entered
    
    Label(Apr, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Apr, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Aprsave5)

def Aprdiary6():
    global work
    global work_entered
    
    Label(Apr, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Apr, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Aprsave6)

def Aprdiary7():
    global work
    global work_entered
    
    Label(Apr, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Apr, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Aprsave7)

def Aprdiary8():
    global work
    global work_entered
    
    Label(Apr, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Apr, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Aprsave8)

def Aprdiary9():
    global work
    global work_entered
    
    Label(Apr, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Apr, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Aprsave9)

def Aprdiary10():
    global work
    global work_entered
    
    Label(Apr, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Apr, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Aprsave10)

def Aprdiary11():
    global work
    global work_entered
    
    Label(Apr, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Apr, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Aprsave11)

def Aprdiary12():
    global work
    global work_entered
    
    Label(Apr, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Apr, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Aprsave12)

def Aprdiary13():
    global work
    global work_entered
    
    Label(Apr, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Apr, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Aprsave13)

def Aprdiary14():
    global work
    global work_entered
    
    Label(Apr, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Apr, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Aprsave14)

def Aprdiary15():
    global work
    global work_entered
    
    Label(Apr, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Apr, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Aprsave15)

def Aprdiary16():
    global work
    global work_entered
    
    Label(Apr, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Apr, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Aprsave16)

def Aprdiary17():
    global work
    global work_entered
    
    Label(Apr, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Apr, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Aprsave17)

def Aprdiary18():
    global work
    global work_entered
    
    Label(Apr, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Apr, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Aprsave18)

def Aprdiary19():
    global work
    global work_entered
    
    Label(Apr, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Apr, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Aprsave19)

def Aprdiary20():
    global work
    global work_entered
    
    Label(Apr, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Apr, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Aprsave20)

def Aprdiary21():
    global work
    global work_entered
    
    Label(Apr, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Apr, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Aprsave21)

def Aprdiary22():
    global work
    global work_entered
    
    Label(Apr, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Apr, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Aprsave22)

def Aprdiary23():
    global work
    global work_entered
    
    Label(Apr, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Apr, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Aprsave23)

def Aprdiary24():
    global work
    global work_entered
    
    Label(Apr, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Apr, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Aprsave24)

def Aprdiary25():
    global work
    global work_entered
    
    Label(Apr, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Apr, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Aprsave25)

def Aprdiary26():
    global work
    global work_entered
    
    Label(Apr, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Apr, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Aprsave26)

def Aprdiary27():
    global work
    global work_entered
    
    Label(Apr, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Apr, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Aprsave27)

def Aprdiary28():
    global work
    global work_entered
    
    Label(Apr, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Apr, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Aprsave28)

def Aprdiary29():
    global work
    global work_entered
    
    Label(Apr, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Apr, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Aprsave29)

def Aprdiary30():
    global work
    global work_entered
    
    Label(Apr, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Apr, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Aprsav30)

#==============================================================================================
      

#4월 일정을 저장 할 scrolledtext 만듦 (1월부터 12월까지 다 해줘야함)===============================
scrol_w=30
scrol_h=12
scr4=scrolledtext.ScrolledText(Apr, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr4.grid(column=10, row=1,columnspan=6, rowspan=6)
#==============================================================================================
    

#1일 부터 월의 최대 일까지의 버튼을 만든다. 19년도 달력을 보고 요일과 일이 매치되도록 함 일일이...
    
#4월 달력판====================================================================================
day1 = Button(Apr, text=" 1 ",command = Aprdiary1)
day1.grid(column=2, row=1)
day2 = Button(Apr, text=" 2 ",command = Aprdiary2)
day2.grid(column=3, row=1)
day3 = Button(Apr, text=" 3 ",command = Aprdiary3)
day3.grid(column=4, row=1)
day4 = Button(Apr, text=" 4 ",command = Aprdiary4)
day4.grid(column=5, row=1)
day5 = Button(Apr, text=" 5 ",command = Aprdiary5)
day5.grid(column=6, row=1)
day6 = Button(Apr, text=" 6 ",command = Aprdiary6)
day6.grid(column=7, row=1)
day7 = Button(Apr, text=" 7 ",command = Aprdiary7)
day7.grid(column=1, row=2)
day8 = Button(Apr, text=" 8 ",command = Aprdiary8)
day8.grid(column=2, row=2)
day9 = Button(Apr, text=" 9 ",command = Aprdiary9)
day9.grid(column=3, row=2)
day10 = Button(Apr, text="10",command = Aprdiary10)
day10.grid(column=4, row=2)
day11 = Button(Apr, text="11",command = Aprdiary11)
day11.grid(column=5, row=2)
day12 = Button(Apr, text="12",command = Aprdiary12)
day12.grid(column=6, row=2)
day13 = Button(Apr, text="13",command = Aprdiary13)
day13.grid(column=7, row=2)
day14 = Button(Apr, text="14",command = Aprdiary14)
day14.grid(column=1, row=3)
day15 = Button(Apr, text="15",command = Aprdiary15)
day15.grid(column=2, row=3)
day16 = Button(Apr, text="16",command = Aprdiary16)
day16.grid(column=3, row=3)
day17 = Button(Apr, text="17",command = Aprdiary17)
day17.grid(column=4, row=3)
day18 = Button(Apr, text="18",command = Aprdiary18)
day18.grid(column=5, row=3)
day19 = Button(Apr, text="19",command = Aprdiary19)
day19.grid(column=6, row=3)
day20 = Button(Apr, text="20",command = Aprdiary20)
day20.grid(column=7, row=3)
day21 = Button(Apr, text="21",command = Aprdiary21)
day21.grid(column=1, row=4)
day22 = Button(Apr, text="22",command = Aprdiary22)
day22.grid(column=2, row=4)
day23 = Button(Apr, text="23",command = Aprdiary23)
day23.grid(column=3, row=4)
day24 = Button(Apr, text="24",command = Aprdiary24)
day24.grid(column=4, row=4)
day25 = Button(Apr, text="25",command = Aprdiary25)
day25.grid(column=5, row=4)
day26 = Button(Apr, text="26",command = Aprdiary26)
day26.grid(column=6, row=4)
day27 = Button(Apr, text="27",command = Aprdiary27)
day27.grid(column=7, row=4)
day28 = Button(Apr, text="28",command = Aprdiary28)
day28.grid(column=1, row=5)
day29 = Button(Apr, text="29",command = Aprdiary29)
day29.grid(column=2, row=5)
day30 = Button(Apr, text="30",command = Aprdiary30)
day30.grid(column=3, row=5)
#===============================================================================================
##########################################################4월 끝#####################################################

##########################################################5월 시작#####################################################
#5월 n일을 입력하는 함수=========================================================
def Maysave1(self):
    value = work.get()
    scr5.insert(tk.INSERT, 'Day1 = ' + value + '\n')
    print('May Day1 schedule = ' + value + '\n')

def Maysave2(self):
    value = work.get()
    scr5.insert(tk.INSERT, 'Day2 = ' + value + '\n')
    print('May Day2 schedule = ' + value + '\n')

def Maysave3(self):
    value = work.get()
    scr5.insert(tk.INSERT, 'Day3 = ' + value + '\n')
    print('May Day3 schedule = ' + value + '\n')

def Maysave4(self):
    value = work.get()
    scr5.insert(tk.INSERT, 'Day4 = ' + value + '\n')
    print('May Day4 schedule = ' + value + '\n')

def Maysave5(self):
    value = work.get()
    scr5.insert(tk.INSERT, 'Day5 = ' + value + '\n')
    print('May Day5 schedule = ' + value + '\n')

def Maysave6(self):
    value = work.get()
    scr5.insert(tk.INSERT, 'Day6 = ' + value + '\n')
    print('May Day6 schedule = ' + value + '\n')

def Maysave7(self):
    value = work.get()
    scr5.insert(tk.INSERT, 'Day7 = ' + value + '\n')
    print('May Day7 schedule = ' + value + '\n')

def Maysave8(self):
    value = work.get()
    scr5.insert(tk.INSERT, 'Day8 = ' + value + '\n')
    print('May Day8 schedule = ' + value + '\n')

def Maysave9(self):
    value = work.get()
    scr5.insert(tk.INSERT, 'Day9 = ' + value + '\n')
    print('May Day9 schedule = ' + value + '\n')

def Maysave10(self):
    value = work.get()
    scr5.insert(tk.INSERT, 'Day10 = ' + value + '\n')
    print('May Day10 schedule = ' + value + '\n')

def Maysave11(self):
    value = work.get()
    scr5.insert(tk.INSERT, 'Day11 = ' + value + '\n')
    print('May Day11 schedule = ' + value + '\n')

def Maysave12(self):
    value = work.get()
    scr5.insert(tk.INSERT, 'Day12 = ' + value + '\n')
    print('May Day12 schedule = ' + value + '\n')

def Maysave13(self):
    value = work.get()
    scr5.insert(tk.INSERT, 'Day13 = ' + value + '\n')
    print('May Day13 schedule = ' + value + '\n')

def Maysave14(self):
    value = work.get()
    scr5.insert(tk.INSERT, 'Day14 = ' + value + '\n')
    print('May Day1 schedule = ' + value + '\n')

def Maysave15(self):
    value = work.get()
    scr5.insert(tk.INSERT, 'Day15 = ' + value + '\n')
    print('May Day15 schedule = ' + value + '\n')

def Maysave16(self):
    value = work.get()
    scr5.insert(tk.INSERT, 'Day16 = ' + value + '\n')
    print('May Day16 schedule = ' + value + '\n')

def Maysave17(self):
    value = work.get()
    scr5.insert(tk.INSERT, 'Day17 = ' + value + '\n')
    print('May Day17 schedule = ' + value + '\n')

def Maysave18(self):
    value = work.get()
    scr5.insert(tk.INSERT, 'Day18 = ' + value + '\n')
    print('May Day18 schedule = ' + value + '\n')

def Maysave19(self):
    value = work.get()
    scr5.insert(tk.INSERT, 'Day19 = ' + value + '\n')
    print('May Day19 schedule = ' + value + '\n')

def Maysave20(self):
    value = work.get()
    scr5.insert(tk.INSERT, 'Day20 = ' + value + '\n')
    print('May Day20 schedule = ' + value + '\n')

def Maysave21(self):
    value = work.get()
    scr5.insert(tk.INSERT, 'Day21 = ' + value + '\n')
    print('May Day21 schedule = ' + value + '\n')

def Maysave22(self):
    value = work.get()
    scr5.insert(tk.INSERT, 'Day22 = ' + value + '\n')
    print('May Day22 schedule = ' + value + '\n')

def Maysave23(self):
    value = work.get()
    scr5.insert(tk.INSERT, 'Day23 = ' + value + '\n')
    print('May Day23 schedule = ' + value + '\n')

def Maysave24(self):
    value = work.get()
    scr5.insert(tk.INSERT, 'Day24 = ' + value + '\n')
    print('May Day24 schedule = ' + value + '\n')

def Maysave25(self):
    value = work.get()
    scr5.insert(tk.INSERT, 'Day25 = ' + value + '\n')
    print('May Day25 schedule = ' + value + '\n')

def Maysave26(self):
    value = work.get()
    scr5.insert(tk.INSERT, 'Day26 = ' + value + '\n')
    print('May Day26 schedule = ' + value + '\n')

def Maysave27(self):
    value = work.get()
    scr5.insert(tk.INSERT, 'Day27 = ' + value + '\n')
    print('May Day27 schedule = ' + value + '\n')

def Maysave28(self):
    value = work.get()
    scr5.insert(tk.INSERT, 'Day28 = ' + value + '\n')
    print('May Day28 schedule = ' + value + '\n')

def Maysave29(self):
    value = work.get()
    scr5.insert(tk.INSERT, 'Day29 = ' + value + '\n')
    print('May Day29 schedule = ' + value + '\n')

def Maysave30(self):
    value = work.get()
    scr5.insert(tk.INSERT, 'Day30 = ' + value + '\n')
    print('May Day30 schedule = ' + value + '\n')

def Maysave31(self):
    value = work.get()
    scr5.insert(tk.INSERT, 'Day31 = ' + value + '\n')
    print('May Day31 schedule = ' + value + '\n')

#============================================================


#콜백되면 Entry가 생성되고, 입력시 스크롤텍스트에 출력할 수 있음 (일마다 하나씩 만들어줘야함)
def Maydiary1():
    global work
    global work_entered
    
    Label(May, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(May, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Maysave1)

def Maydiary2():
    global work
    global work_entered
    
    Label(May, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(May, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Maysave2)

def Maydiary3():
    global work
    global work_entered
    
    Label(May, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(May, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Maysave3)

def Maydiary4():
    global work
    global work_entered
    
    Label(May, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(May, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Maysave4)

def Maydiary5():
    global work
    global work_entered
    
    Label(May, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(May, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Maysave5)

def Maydiary6():
    global work
    global work_entered
    
    Label(May, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(May, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Maysave6)

def Maydiary7():
    global work
    global work_entered
    
    Label(May, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(May, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Maysave7)

def Maydiary8():
    global work
    global work_entered
    
    Label(May, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(May, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Maysave8)

def Maydiary9():
    global work
    global work_entered
    
    Label(May, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(May, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Maysave9)

def Maydiary10():
    global work
    global work_entered
    
    Label(May, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(May, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Maysave10)

def Maydiary11():
    global work
    global work_entered
    
    Label(May, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(May, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Maysave11)

def Maydiary12():
    global work
    global work_entered
    
    Label(May, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(May, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Maysave12)

def Maydiary13():
    global work
    global work_entered
    
    Label(May, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(May, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Maysave13)

def Maydiary14():
    global work
    global work_entered
    
    Label(May, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(May, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Maysave14)

def Maydiary15():
    global work
    global work_entered
    
    Label(May, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(May, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Maysave15)

def Maydiary16():
    global work
    global work_entered
    
    Label(May, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(May, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Maysave16)

def Maydiary17():
    global work
    global work_entered
    
    Label(May, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(May, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Maysave17)

def Maydiary18():
    global work
    global work_entered
    
    Label(May, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(May, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Maysave18)

def Maydiary19():
    global work
    global work_entered
    
    Label(May, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(May, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Maysave19)

def Maydiary20():
    global work
    global work_entered
    
    Label(May, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(May, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Maysave20)

def Maydiary21():
    global work
    global work_entered
    
    Label(May, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(May, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Maysave21)

def Maydiary22():
    global work
    global work_entered
    
    Label(May, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(May, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Maysave22)

def Maydiary23():
    global work
    global work_entered
    
    Label(May, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(May, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Maysave23)

def Maydiary24():
    global work
    global work_entered
    
    Label(May, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(May, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Maysave24)

def Maydiary25():
    global work
    global work_entered
    
    Label(May, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(May, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Maysave25)

def Maydiary26():
    global work
    global work_entered
    
    Label(May, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(May, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Maysave26)

def Maydiary27():
    global work
    global work_entered
    
    Label(May, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(May, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Maysave27)

def Maydiary28():
    global work
    global work_entered
    
    Label(May, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(May, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Maysave28)

def Maydiary29():
    global work
    global work_entered
    
    Label(May, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(May, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Maysave29)

def Maydiary30():
    global work
    global work_entered
    
    Label(May, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(May, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Maysav30)

def Maydiary31():
    global work
    global work_entered
    
    Label(May, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(May, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Maysave31)

#==============================================================================================
      
    

#5월 일정을 저장 할 scrolledtext 만듦 (1월부터 12월까지 다 해줘야함)===============================
scrol_w=30
scrol_h=12
scr5=scrolledtext.ScrolledText(May, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr5.grid(column=10, row=1,columnspan=6, rowspan=6)
#==============================================================================================
    

#1일 부터 월의 최대 일까지의 버튼을 만든다. 19년도 달력을 보고 요일과 일이 매치되도록 함 일일이...
    
#5월 달력판====================================================================================
day1 = Button(May, text=" 1 ",command = Maydiary1)
day1.grid(column=4, row=1)
day2 = Button(May, text=" 2 ",command = Maydiary2)
day2.grid(column=5, row=1)
day3 = Button(May, text=" 3 ",command = Maydiary3)
day3.grid(column=6, row=1)
day4 = Button(May, text=" 4 ",command = Maydiary4)
day4.grid(column=7, row=1)
day5 = Button(May, text=" 5 ",command = Maydiary5)
day5.grid(column=1, row=2)
day6 = Button(May, text=" 6 ",command = Maydiary6)
day6.grid(column=2, row=2)
day7 = Button(May, text=" 7 ",command = Maydiary7)
day7.grid(column=3, row=2)
day8 = Button(May, text=" 8 ",command = Maydiary8)
day8.grid(column=4, row=2)
day9 = Button(May, text=" 9 ",command = Maydiary9)
day9.grid(column=5, row=2)
day10 = Button(May, text="10",command = Maydiary10)
day10.grid(column=6, row=2)
day11 = Button(May, text="11",command = Maydiary11)
day11.grid(column=7, row=2)
day12 = Button(May, text="12",command = Maydiary12)
day12.grid(column=1, row=3)
day13 = Button(May, text="13",command = Maydiary13)
day13.grid(column=2, row=3)
day14 = Button(May, text="14",command = Maydiary14)
day14.grid(column=3, row=3)
day15 = Button(May, text="15",command = Maydiary15)
day15.grid(column=4, row=3)
day16 = Button(May, text="16",command = Maydiary16)
day16.grid(column=5, row=3)
day17 = Button(May, text="17",command = Maydiary17)
day17.grid(column=6, row=3)
day18 = Button(May, text="18",command = Maydiary18)
day18.grid(column=7, row=3)
day19 = Button(May, text="19",command = Maydiary19)
day19.grid(column=1, row=4)
day20 = Button(May, text="20",command = Maydiary20)
day20.grid(column=2, row=4)
day21 = Button(May, text="21",command = Maydiary21)
day21.grid(column=3, row=4)
day22 = Button(May, text="22",command = Maydiary22)
day22.grid(column=4, row=4)
day23 = Button(May, text="23",command = Maydiary23)
day23.grid(column=5, row=4)
day24 = Button(May, text="24",command = Maydiary24)
day24.grid(column=6, row=4)
day25 = Button(May, text="25",command = Maydiary25)
day25.grid(column=7, row=4)
day26 = Button(May, text="26",command = Maydiary26)
day26.grid(column=1, row=5)
day27 = Button(May, text="27",command = Maydiary27)
day27.grid(column=2, row=5)
day28 = Button(May, text="28",command = Maydiary28)
day28.grid(column=3, row=5)
day29 = Button(May, text="29",command = Maydiary29)
day29.grid(column=4, row=5)
day30 = Button(May, text="30",command = Maydiary30)
day30.grid(column=5, row=5)
day31 = Button(May, text="31",command = Maydiary31)
day31.grid(column=6, row=5)
#===============================================================================================
##########################################################5월 끝#####################################################

##########################################################6월 시작#####################################################
#6월 n일을 입력하는 함수=========================================================
def Junsave1(self):
    value = work.get()
    scr6.insert(tk.INSERT, 'Day1 = ' + value + '\n')
    print('Jun Day1 schedule = ' + value + '\n')

def Junsave2(self):
    value = work.get()
    scr6.insert(tk.INSERT, 'Day2 = ' + value + '\n')
    print('Jun Day2 schedule = ' + value + '\n')

def Junsave3(self):
    value = work.get()
    scr6.insert(tk.INSERT, 'Day3 = ' + value + '\n')
    print('Jun Day3 schedule = ' + value + '\n')

def Junsave4(self):
    value = work.get()
    scr6.insert(tk.INSERT, 'Day4 = ' + value + '\n')
    print('Jun Day4 schedule = ' + value + '\n')

def Junsave5(self):
    value = work.get()
    scr6.insert(tk.INSERT, 'Day5 = ' + value + '\n')
    print('Jun Day5 schedule = ' + value + '\n')

def Junsave6(self):
    value = work.get()
    scr6.insert(tk.INSERT, 'Day6 = ' + value + '\n')
    print('Jun Day6 schedule = ' + value + '\n')

def Junsave7(self):
    value = work.get()
    scr6.insert(tk.INSERT, 'Day7 = ' + value + '\n')
    print('Jun Day7 schedule = ' + value + '\n')

def Junsave8(self):
    value = work.get()
    scr6.insert(tk.INSERT, 'Day8 = ' + value + '\n')
    print('Jun Day8 schedule = ' + value + '\n')

def Junsave9(self):
    value = work.get()
    scr6.insert(tk.INSERT, 'Day9 = ' + value + '\n')
    print('Jun Day9 schedule = ' + value + '\n')

def Junsave10(self):
    value = work.get()
    scr6.insert(tk.INSERT, 'Day10 = ' + value + '\n')
    print('Jun Day10 schedule = ' + value + '\n')

def Junsave11(self):
    value = work.get()
    scr6.insert(tk.INSERT, 'Day11 = ' + value + '\n')
    print('Jun Day11 schedule = ' + value + '\n')

def Junsave12(self):
    value = work.get()
    scr6.insert(tk.INSERT, 'Day12 = ' + value + '\n')
    print('Jun Day12 schedule = ' + value + '\n')

def Junsave13(self):
    value = work.get()
    scr6.insert(tk.INSERT, 'Day13 = ' + value + '\n')
    print('Jun Day13 schedule = ' + value + '\n')

def Junsave14(self):
    value = work.get()
    scr6.insert(tk.INSERT, 'Day14 = ' + value + '\n')
    print('Jun Day1 schedule = ' + value + '\n')

def Junsave15(self):
    value = work.get()
    scr6.insert(tk.INSERT, 'Day15 = ' + value + '\n')
    print('Jun Day15 schedule = ' + value + '\n')

def Junsave16(self):
    value = work.get()
    scr6.insert(tk.INSERT, 'Day16 = ' + value + '\n')
    print('Jun Day16 schedule = ' + value + '\n')

def Junsave17(self):
    value = work.get()
    scr6.insert(tk.INSERT, 'Day17 = ' + value + '\n')
    print('Jun Day17 schedule = ' + value + '\n')

def Junsave18(self):
    value = work.get()
    scr6.insert(tk.INSERT, 'Day18 = ' + value + '\n')
    print('Jun Day18 schedule = ' + value + '\n')

def Junsave19(self):
    value = work.get()
    scr6.insert(tk.INSERT, 'Day19 = ' + value + '\n')
    print('Jun Day19 schedule = ' + value + '\n')

def Junsave20(self):
    value = work.get()
    scr6.insert(tk.INSERT, 'Day20 = ' + value + '\n')
    print('Jun Day20 schedule = ' + value + '\n')

def Junsave21(self):
    value = work.get()
    scr6.insert(tk.INSERT, 'Day21 = ' + value + '\n')
    print('Jun Day21 schedule = ' + value + '\n')

def Junsave22(self):
    value = work.get()
    scr6.insert(tk.INSERT, 'Day22 = ' + value + '\n')
    print('Jun Day22 schedule = ' + value + '\n')

def Junsave23(self):
    value = work.get()
    scr6.insert(tk.INSERT, 'Day23 = ' + value + '\n')
    print('Jun Day23 schedule = ' + value + '\n')

def Junsave24(self):
    value = work.get()
    scr6.insert(tk.INSERT, 'Day24 = ' + value + '\n')
    print('Jun Day24 schedule = ' + value + '\n')

def Junsave25(self):
    value = work.get()
    scr6.insert(tk.INSERT, 'Day25 = ' + value + '\n')
    print('Jun Day25 schedule = ' + value + '\n')

def Junsave26(self):
    value = work.get()
    scr6.insert(tk.INSERT, 'Day26 = ' + value + '\n')
    print('Jun Day26 schedule = ' + value + '\n')

def Junsave27(self):
    value = work.get()
    scr6.insert(tk.INSERT, 'Day27 = ' + value + '\n')
    print('Jun Day27 schedule = ' + value + '\n')

def Junsave28(self):
    value = work.get()
    scr6.insert(tk.INSERT, 'Day28 = ' + value + '\n')
    print('Jun Day28 schedule = ' + value + '\n')

def Junsave29(self):
    value = work.get()
    scr6.insert(tk.INSERT, 'Day29 = ' + value + '\n')
    print('Jun Day29 schedule = ' + value + '\n')

def Junsave30(self):
    value = work.get()
    scr6.insert(tk.INSERT, 'Day30 = ' + value + '\n')
    print('Jun Day30 schedule = ' + value + '\n')

#============================================================


#콜백되면 Entry가 생성되고, 입력시 스크롤텍스트에 출력할 수 있음 (일마다 하나씩 만들어줘야함)
def Jundiary1():
    global work
    global work_entered
    
    Label(Jun, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jun, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Junsave1)

def Jundiary2():
    global work
    global work_entered
    
    Label(Jun, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jun, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Junsave2)

def Jundiary3():
    global work
    global work_entered
    
    Label(Jun, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jun, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Junsave3)

def Jundiary4():
    global work
    global work_entered
    
    Label(Jun, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jun, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Junsave4)

def Jundiary5():
    global work
    global work_entered
    
    Label(Jun, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jun, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Junsave5)

def Jundiary6():
    global work
    global work_entered
    
    Label(Jun, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jun, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Junsave6)

def Jundiary7():
    global work
    global work_entered
    
    Label(Jun, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jun, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Junsave7)

def Jundiary8():
    global work
    global work_entered
    
    Label(Jun, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jun, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Junsave8)

def Jundiary9():
    global work
    global work_entered
    
    Label(Jun, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jun, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Junsave9)

def Jundiary10():
    global work
    global work_entered
    
    Label(Jun, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jun, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Junsave10)

def Jundiary11():
    global work
    global work_entered
    
    Label(Jun, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jun, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Junsave11)

def Jundiary12():
    global work
    global work_entered
    
    Label(Jun, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jun, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Junsave12)

def Jundiary13():
    global work
    global work_entered
    
    Label(Jun, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jun, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Junsave13)

def Jundiary14():
    global work
    global work_entered
    
    Label(Jun, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jun, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Junsave14)

def Jundiary15():
    global work
    global work_entered
    
    Label(Jun, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jun, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Junsave15)

def Jundiary16():
    global work
    global work_entered
    
    Label(Jun, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jun, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Junsave16)

def Jundiary17():
    global work
    global work_entered
    
    Label(Jun, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jun, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Junsave17)

def Jundiary18():
    global work
    global work_entered
    
    Label(Jun, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jun, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Junsave18)

def Jundiary19():
    global work
    global work_entered
    
    Label(Jun, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jun, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Junsave19)

def Jundiary20():
    global work
    global work_entered
    
    Label(Jun, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jun, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Junsave20)

def Jundiary21():
    global work
    global work_entered
    
    Label(Jun, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jun, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Junsave21)

def Jundiary22():
    global work
    global work_entered
    
    Label(Jun, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jun, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Junsave22)

def Jundiary23():
    global work
    global work_entered
    
    Label(Jun, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jun, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Junsave23)

def Jundiary24():
    global work
    global work_entered
    
    Label(Jun, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jun, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Junsave24)

def Jundiary25():
    global work
    global work_entered
    
    Label(Jun, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jun, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Junsave25)

def Jundiary26():
    global work
    global work_entered
    
    Label(Jun, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jun, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Junsave26)

def Jundiary27():
    global work
    global work_entered
    
    Label(Jun, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jun, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Junsave27)

def Jundiary28():
    global work
    global work_entered
    
    Label(Jun, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jun, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Junsave28)

def Jundiary29():
    global work
    global work_entered
    
    Label(Jun, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jun, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Junsave29)

def Jundiary30():
    global work
    global work_entered
    
    Label(Jun, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jun, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Junsav30)

#==============================================================================================
      

#6월 일정을 저장 할 scrolledtext 만듦 (1월부터 12월까지 다 해줘야함)===============================
scrol_w=30
scrol_h=12
scr6=scrolledtext.ScrolledText(Jun, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr6.grid(column=10, row=1,columnspan=6, rowspan=6)
#==============================================================================================
    

#1일 부터 월의 최대 일까지의 버튼을 만든다. 19년도 달력을 보고 요일과 일이 매치되도록 함 일일이...
    
#6월 달력판====================================================================================
day1 = Button(Jun, text=" 1 ",command = Jundiary1)
day1.grid(column=7, row=1)
day2 = Button(Jun, text=" 2 ",command = Jundiary2)
day2.grid(column=1, row=2)
day3 = Button(Jun, text=" 3 ",command = Jundiary3)
day3.grid(column=2, row=2)
day4 = Button(Jun, text=" 4 ",command = Jundiary4)
day4.grid(column=3, row=2)
day5 = Button(Jun, text=" 5 ",command = Jundiary5)
day5.grid(column=4, row=2)
day6 = Button(Jun, text=" 6 ",command = Jundiary6)
day6.grid(column=5, row=2)
day7 = Button(Jun, text=" 7 ",command = Jundiary7)
day7.grid(column=6, row=2)
day8 = Button(Jun, text=" 8 ",command = Jundiary8)
day8.grid(column=7, row=2)
day9 = Button(Jun, text=" 9 ",command = Jundiary9)
day9.grid(column=1, row=3)
day10 = Button(Jun, text="10",command = Jundiary10)
day10.grid(column=2, row=3)
day11 = Button(Jun, text="11",command = Jundiary11)
day11.grid(column=3, row=3)
day12 = Button(Jun, text="12",command = Jundiary12)
day12.grid(column=4, row=3)
day13 = Button(Jun, text="13",command = Jundiary13)
day13.grid(column=5, row=3)
day14 = Button(Jun, text="14",command = Jundiary14)
day14.grid(column=6, row=3)
day15 = Button(Jun, text="15",command = Jundiary15)
day15.grid(column=7, row=3)
day16 = Button(Jun, text="16",command = Jundiary16)
day16.grid(column=1, row=4)
day17 = Button(Jun, text="17",command = Jundiary17)
day17.grid(column=2, row=4)
day18 = Button(Jun, text="18",command = Jundiary18)
day18.grid(column=3, row=4)
day19 = Button(Jun, text="19",command = Jundiary19)
day19.grid(column=4, row=4)
day20 = Button(Jun, text="20",command = Jundiary20)
day20.grid(column=5, row=4)
day21 = Button(Jun, text="21",command = Jundiary21)
day21.grid(column=6, row=4)
day22 = Button(Jun, text="22",command = Jundiary22)
day22.grid(column=7, row=4)
day23 = Button(Jun, text="23",command = Jundiary23)
day23.grid(column=1, row=5)
day24 = Button(Jun, text="24",command = Jundiary24)
day24.grid(column=2, row=5)
day25 = Button(Jun, text="25",command = Jundiary25)
day25.grid(column=3, row=5)
day26 = Button(Jun, text="26",command = Jundiary26)
day26.grid(column=4, row=5)
day27 = Button(Jun, text="27",command = Jundiary27)
day27.grid(column=5, row=5)
day28 = Button(Jun, text="28",command = Jundiary28)
day28.grid(column=6, row=5)
day29 = Button(Jun, text="29",command = Jundiary29)
day29.grid(column=7, row=5)
day30 = Button(Jun, text="30",command = Jundiary30)
day30.grid(column=1, row=6)

#===============================================================================================
##########################################################6월 끝#####################################################

##########################################################7월 시작#####################################################
#7월 n일을 입력하는 함수=========================================================
def Julsave1(self):
    value = work.get()
    scr7.insert(tk.INSERT, 'Day1 = ' + value + '\n')
    print('Jul Day1 schedule = ' + value + '\n')

def Julsave2(self):
    value = work.get()
    scr7.insert(tk.INSERT, 'Day2 = ' + value + '\n')
    print('Jul Day2 schedule = ' + value + '\n')

def Julsave3(self):
    value = work.get()
    scr7.insert(tk.INSERT, 'Day3 = ' + value + '\n')
    print('Jul Day3 schedule = ' + value + '\n')

def Julsave4(self):
    value = work.get()
    scr7.insert(tk.INSERT, 'Day4 = ' + value + '\n')
    print('Jul Day4 schedule = ' + value + '\n')

def Julsave5(self):
    value = work.get()
    scr7.insert(tk.INSERT, 'Day5 = ' + value + '\n')
    print('Jul Day5 schedule = ' + value + '\n')

def Julsave6(self):
    value = work.get()
    scr7.insert(tk.INSERT, 'Day6 = ' + value + '\n')
    print('Jul Day6 schedule = ' + value + '\n')

def Julsave7(self):
    value = work.get()
    scr7.insert(tk.INSERT, 'Day7 = ' + value + '\n')
    print('Jul Day7 schedule = ' + value + '\n')

def Julsave8(self):
    value = work.get()
    scr7.insert(tk.INSERT, 'Day8 = ' + value + '\n')
    print('Jul Day8 schedule = ' + value + '\n')

def Julsave9(self):
    value = work.get()
    scr7.insert(tk.INSERT, 'Day9 = ' + value + '\n')
    print('Jul Day9 schedule = ' + value + '\n')

def Julsave10(self):
    value = work.get()
    scr7.insert(tk.INSERT, 'Day10 = ' + value + '\n')
    print('Jul Day10 schedule = ' + value + '\n')

def Julsave11(self):
    value = work.get()
    scr7.insert(tk.INSERT, 'Day11 = ' + value + '\n')
    print('Jul Day11 schedule = ' + value + '\n')

def Julsave12(self):
    value = work.get()
    scr7.insert(tk.INSERT, 'Day12 = ' + value + '\n')
    print('Jul Day12 schedule = ' + value + '\n')

def Julsave13(self):
    value = work.get()
    scr7.insert(tk.INSERT, 'Day13 = ' + value + '\n')
    print('Jul Day13 schedule = ' + value + '\n')

def Julsave14(self):
    value = work.get()
    scr7.insert(tk.INSERT, 'Day14 = ' + value + '\n')
    print('Jul Day1 schedule = ' + value + '\n')

def Julsave15(self):
    value = work.get()
    scr7.insert(tk.INSERT, 'Day15 = ' + value + '\n')
    print('Jul Day15 schedule = ' + value + '\n')

def Julsave16(self):
    value = work.get()
    scr7.insert(tk.INSERT, 'Day16 = ' + value + '\n')
    print('Jul Day16 schedule = ' + value + '\n')

def Julsave17(self):
    value = work.get()
    scr7.insert(tk.INSERT, 'Day17 = ' + value + '\n')
    print('Jul Day17 schedule = ' + value + '\n')

def Julsave18(self):
    value = work.get()
    scr7.insert(tk.INSERT, 'Day18 = ' + value + '\n')
    print('Jul Day18 schedule = ' + value + '\n')

def Julsave19(self):
    value = work.get()
    scr7.insert(tk.INSERT, 'Day19 = ' + value + '\n')
    print('Jul Day19 schedule = ' + value + '\n')

def Julsave20(self):
    value = work.get()
    scr7.insert(tk.INSERT, 'Day20 = ' + value + '\n')
    print('Jul Day20 schedule = ' + value + '\n')

def Julsave21(self):
    value = work.get()
    scr7.insert(tk.INSERT, 'Day21 = ' + value + '\n')
    print('Jul Day21 schedule = ' + value + '\n')

def Julsave22(self):
    value = work.get()
    scr7.insert(tk.INSERT, 'Day22 = ' + value + '\n')
    print('Jul Day22 schedule = ' + value + '\n')

def Julsave23(self):
    value = work.get()
    scr7.insert(tk.INSERT, 'Day23 = ' + value + '\n')
    print('Jul Day23 schedule = ' + value + '\n')

def Julsave24(self):
    value = work.get()
    scr7.insert(tk.INSERT, 'Day24 = ' + value + '\n')
    print('Jul Day24 schedule = ' + value + '\n')

def Julsave25(self):
    value = work.get()
    scr7.insert(tk.INSERT, 'Day25 = ' + value + '\n')
    print('Jul Day25 schedule = ' + value + '\n')

def Julsave26(self):
    value = work.get()
    scr7.insert(tk.INSERT, 'Day26 = ' + value + '\n')
    print('Jul Day26 schedule = ' + value + '\n')

def Julsave27(self):
    value = work.get()
    scr7.insert(tk.INSERT, 'Day27 = ' + value + '\n')
    print('Jul Day27 schedule = ' + value + '\n')

def Julsave28(self):
    value = work.get()
    scr7.insert(tk.INSERT, 'Day28 = ' + value + '\n')
    print('Jul Day28 schedule = ' + value + '\n')

def Julsave29(self):
    value = work.get()
    scr7.insert(tk.INSERT, 'Day29 = ' + value + '\n')
    print('Jul Day29 schedule = ' + value + '\n')

def Julsave30(self):
    value = work.get()
    scr7.insert(tk.INSERT, 'Day30 = ' + value + '\n')
    print('Jul Day30 schedule = ' + value + '\n')

def Julsave31(self):
    value = work.get()
    scr7.insert(tk.INSERT, 'Day31 = ' + value + '\n')
    print('Jul Day31 schedule = ' + value + '\n')
#============================================================


#콜백되면 Entry가 생성되고, 입력시 스크롤텍스트에 출력할 수 있음 (일마다 하나씩 만들어줘야함)
def Juldiary1():
    global work
    global work_entered
    
    Label(Jul, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jul, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Julsave1)

def Juldiary2():
    global work
    global work_entered
    
    Label(Jul, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jul, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Julsave2)

def Juldiary3():
    global work
    global work_entered
    
    Label(Jul, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jul, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Julsave3)

def Juldiary4():
    global work
    global work_entered
    
    Label(Jul, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jul, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Julsave4)

def Juldiary5():
    global work
    global work_entered
    
    Label(Jul, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jul, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Julsave5)

def Juldiary6():
    global work
    global work_entered
    
    Label(Jul, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jul, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Julsave6)

def Juldiary7():
    global work
    global work_entered
    
    Label(Jul, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jul, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Julsave7)

def Juldiary8():
    global work
    global work_entered
    
    Label(Jul, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jul, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Julsave8)

def Juldiary9():
    global work
    global work_entered
    
    Label(Jul, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jul, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Julsave9)

def Juldiary10():
    global work
    global work_entered
    
    Label(Jul, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jul, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Julsave10)

def Juldiary11():
    global work
    global work_entered
    
    Label(Jul, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jul, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Julsave11)

def Juldiary12():
    global work
    global work_entered
    
    Label(Jul, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jul, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Julsave12)

def Juldiary13():
    global work
    global work_entered
    
    Label(Jul, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jul, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Julsave13)

def Juldiary14():
    global work
    global work_entered
    
    Label(Jul, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jul, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Julsave14)

def Juldiary15():
    global work
    global work_entered
    
    Label(Jul, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jul, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Julsave15)

def Juldiary16():
    global work
    global work_entered
    
    Label(Jul, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jul, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Julsave16)

def Juldiary17():
    global work
    global work_entered
    
    Label(Jul, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jul, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Julsave17)

def Juldiary18():
    global work
    global work_entered
    
    Label(Jul, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jul, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Julsave18)

def Juldiary19():
    global work
    global work_entered
    
    Label(Jul, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jul, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Julsave19)

def Juldiary20():
    global work
    global work_entered
    
    Label(Jul, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jul, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Julsave20)

def Juldiary21():
    global work
    global work_entered
    
    Label(Jul, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jul, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Julsave21)

def Juldiary22():
    global work
    global work_entered
    
    Label(Jul, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jul, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Julsave22)

def Juldiary23():
    global work
    global work_entered
    
    Label(Jul, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jul, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Julsave23)

def Juldiary24():
    global work
    global work_entered
    
    Label(Jul, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jul, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Julsave24)

def Juldiary25():
    global work
    global work_entered
    
    Label(Jul, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jul, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Julsave25)

def Juldiary26():
    global work
    global work_entered
    
    Label(Jul, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jul, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Julsave26)

def Juldiary27():
    global work
    global work_entered
    
    Label(Jul, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jul, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Julsave27)

def Juldiary28():
    global work
    global work_entered
    
    Label(Jul, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jul, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Julsave28)

def Juldiary29():
    global work
    global work_entered
    
    Label(Jul, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jul, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Julsave29)

def Juldiary30():
    global work
    global work_entered
    
    Label(Jul, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jul, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Julsav30)

def Juldiary31():
    global work
    global work_entered
    
    Label(Jul, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Jul, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Julsave31)

#==============================================================================================
      
    

#7월 일정을 저장 할 scrolledtext 만듦 (1월부터 12월까지 다 해줘야함)===============================
scrol_w=30
scrol_h=12
scr7=scrolledtext.ScrolledText(Jul, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr7.grid(column=10, row=1,columnspan=6, rowspan=6)
#==============================================================================================
    

#1일 부터 월의 최대 일까지의 버튼을 만든다. 19년도 달력을 보고 요일과 일이 매치되도록 함 일일이...
    
#7월 달력판====================================================================================
day1 = Button(Jul, text=" 1 ",command = Juldiary1)
day1.grid(column=2, row=1)
day2 = Button(Jul, text=" 2 ",command = Juldiary2)
day2.grid(column=3, row=1)
day3 = Button(Jul, text=" 3 ",command = Juldiary3)
day3.grid(column=4, row=1)
day4 = Button(Jul, text=" 4 ",command = Juldiary4)
day4.grid(column=5, row=1)
day5 = Button(Jul, text=" 5 ",command = Juldiary5)
day5.grid(column=6, row=1)
day6 = Button(Jul, text=" 6 ",command = Juldiary6)
day6.grid(column=7, row=1)
day7 = Button(Jul, text=" 7 ",command = Juldiary7)
day7.grid(column=1, row=2)
day8 = Button(Jul, text=" 8 ",command = Juldiary8)
day8.grid(column=2, row=2)
day9 = Button(Jul, text=" 9 ",command = Juldiary9)
day9.grid(column=3, row=2)
day10 = Button(Jul, text="10",command = Juldiary10)
day10.grid(column=4, row=2)
day11 = Button(Jul, text="11",command = Juldiary11)
day11.grid(column=5, row=2)
day12 = Button(Jul, text="12",command = Juldiary12)
day12.grid(column=6, row=2)
day13 = Button(Jul, text="13",command = Juldiary13)
day13.grid(column=7, row=2)
day14 = Button(Jul, text="14",command = Juldiary14)
day14.grid(column=1, row=3)
day15 = Button(Jul, text="15",command = Juldiary15)
day15.grid(column=2, row=3)
day16 = Button(Jul, text="16",command = Juldiary16)
day16.grid(column=3, row=3)
day17 = Button(Jul, text="17",command = Juldiary17)
day17.grid(column=4, row=3)
day18 = Button(Jul, text="18",command = Juldiary18)
day18.grid(column=5, row=3)
day19 = Button(Jul, text="19",command = Juldiary19)
day19.grid(column=6, row=3)
day20 = Button(Jul, text="20",command = Juldiary20)
day20.grid(column=7, row=3)
day21 = Button(Jul, text="21",command = Juldiary21)
day21.grid(column=1, row=4)
day22 = Button(Jul, text="22",command = Juldiary22)
day22.grid(column=2, row=4)
day23 = Button(Jul, text="23",command = Juldiary23)
day23.grid(column=3, row=4)
day24 = Button(Jul, text="24",command = Juldiary24)
day24.grid(column=4, row=4)
day25 = Button(Jul, text="25",command = Juldiary25)
day25.grid(column=5, row=4)
day26 = Button(Jul, text="26",command = Juldiary26)
day26.grid(column=6, row=4)
day27 = Button(Jul, text="27",command = Juldiary27)
day27.grid(column=7, row=4)
day28 = Button(Jul, text="28",command = Juldiary28)
day28.grid(column=1, row=5)
day29 = Button(Jul, text="29",command = Juldiary29)
day29.grid(column=2, row=5)
day30 = Button(Jul, text="30",command = Juldiary30)
day30.grid(column=3, row=5)
day31 = Button(Jul, text="31",command = Juldiary31)
day31.grid(column=4, row=5)
#===============================================================================================
##########################################################7월 끝#####################################################

##########################################################8월 시작#####################################################
#8월 n일을 입력하는 함수=========================================================
def Augsave1(self):
    value = work.get()
    scr8.insert(tk.INSERT, 'Day1 = ' + value + '\n')
    print('Aug Day1 schedule = ' + value + '\n')

def Augsave2(self):
    value = work.get()
    scr8.insert(tk.INSERT, 'Day2 = ' + value + '\n')
    print('Aug Day2 schedule = ' + value + '\n')

def Augsave3(self):
    value = work.get()
    scr8.insert(tk.INSERT, 'Day3 = ' + value + '\n')
    print('Aug Day3 schedule = ' + value + '\n')

def Augsave4(self):
    value = work.get()
    scr8.insert(tk.INSERT, 'Day4 = ' + value + '\n')
    print('Aug Day4 schedule = ' + value + '\n')

def Augsave5(self):
    value = work.get()
    scr8.insert(tk.INSERT, 'Day5 = ' + value + '\n')
    print('Aug Day5 schedule = ' + value + '\n')

def Augsave6(self):
    value = work.get()
    scr8.insert(tk.INSERT, 'Day6 = ' + value + '\n')
    print('Aug Day6 schedule = ' + value + '\n')

def Augsave7(self):
    value = work.get()
    scr8.insert(tk.INSERT, 'Day7 = ' + value + '\n')
    print('Aug Day7 schedule = ' + value + '\n')

def Augsave8(self):
    value = work.get()
    scr8.insert(tk.INSERT, 'Day8 = ' + value + '\n')
    print('Aug Day8 schedule = ' + value + '\n')

def Augsave9(self):
    value = work.get()
    scr8.insert(tk.INSERT, 'Day9 = ' + value + '\n')
    print('Aug Day9 schedule = ' + value + '\n')

def Augsave10(self):
    value = work.get()
    scr8.insert(tk.INSERT, 'Day10 = ' + value + '\n')
    print('Aug Day10 schedule = ' + value + '\n')

def Augsave11(self):
    value = work.get()
    scr8.insert(tk.INSERT, 'Day11 = ' + value + '\n')
    print('Aug Day11 schedule = ' + value + '\n')

def Augsave12(self):
    value = work.get()
    scr8.insert(tk.INSERT, 'Day12 = ' + value + '\n')
    print('Aug Day12 schedule = ' + value + '\n')

def Augsave13(self):
    value = work.get()
    scr8.insert(tk.INSERT, 'Day13 = ' + value + '\n')
    print('Aug Day13 schedule = ' + value + '\n')

def Augsave14(self):
    value = work.get()
    scr8.insert(tk.INSERT, 'Day14 = ' + value + '\n')
    print('Aug Day1 schedule = ' + value + '\n')

def Augsave15(self):
    value = work.get()
    scr8.insert(tk.INSERT, 'Day15 = ' + value + '\n')
    print('Aug Day15 schedule = ' + value + '\n')

def Augsave16(self):
    value = work.get()
    scr8.insert(tk.INSERT, 'Day16 = ' + value + '\n')
    print('Aug Day16 schedule = ' + value + '\n')

def Augsave17(self):
    value = work.get()
    scr8.insert(tk.INSERT, 'Day17 = ' + value + '\n')
    print('Aug Day17 schedule = ' + value + '\n')

def Augsave18(self):
    value = work.get()
    scr8.insert(tk.INSERT, 'Day18 = ' + value + '\n')
    print('Aug Day18 schedule = ' + value + '\n')

def Augsave19(self):
    value = work.get()
    scr8.insert(tk.INSERT, 'Day19 = ' + value + '\n')
    print('Aug Day19 schedule = ' + value + '\n')

def Augsave20(self):
    value = work.get()
    scr8.insert(tk.INSERT, 'Day20 = ' + value + '\n')
    print('Aug Day20 schedule = ' + value + '\n')

def Augsave21(self):
    value = work.get()
    scr8.insert(tk.INSERT, 'Day21 = ' + value + '\n')
    print('Aug Day21 schedule = ' + value + '\n')

def Augsave22(self):
    value = work.get()
    scr8.insert(tk.INSERT, 'Day22 = ' + value + '\n')
    print('Aug Day22 schedule = ' + value + '\n')

def Augsave23(self):
    value = work.get()
    scr8.insert(tk.INSERT, 'Day23 = ' + value + '\n')
    print('Aug Day23 schedule = ' + value + '\n')

def Augsave24(self):
    value = work.get()
    scr8.insert(tk.INSERT, 'Day24 = ' + value + '\n')
    print('Aug Day24 schedule = ' + value + '\n')

def Augsave25(self):
    value = work.get()
    scr8.insert(tk.INSERT, 'Day25 = ' + value + '\n')
    print('Aug Day25 schedule = ' + value + '\n')

def Augsave26(self):
    value = work.get()
    scr8.insert(tk.INSERT, 'Day26 = ' + value + '\n')
    print('Aug Day26 schedule = ' + value + '\n')

def Augsave27(self):
    value = work.get()
    scr8.insert(tk.INSERT, 'Day27 = ' + value + '\n')
    print('Aug Day27 schedule = ' + value + '\n')

def Augsave28(self):
    value = work.get()
    scr8.insert(tk.INSERT, 'Day28 = ' + value + '\n')
    print('Aug Day28 schedule = ' + value + '\n')

def Augsave29(self):
    value = work.get()
    scr8.insert(tk.INSERT, 'Day29 = ' + value + '\n')
    print('Aug Day29 schedule = ' + value + '\n')

def Augsave30(self):
    value = work.get()
    scr8.insert(tk.INSERT, 'Day30 = ' + value + '\n')
    print('Aug Day30 schedule = ' + value + '\n')

def Augsave31(self):
    value = work.get()
    scr8.insert(tk.INSERT, 'Day31 = ' + value + '\n')
    print('Aug Day31 schedule = ' + value + '\n')

#============================================================


#콜백되면 Entry가 생성되고, 입력시 스크롤텍스트에 출력할 수 있음 (일마다 하나씩 만들어줘야함)
def Augdiary1():
    global work
    global work_entered
    
    Label(Aug, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Aug, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Augsave1)

def Augdiary2():
    global work
    global work_entered
    
    Label(Aug, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Aug, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Augsave2)

def Augdiary3():
    global work
    global work_entered
    
    Label(Aug, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Aug, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Augsave3)

def Augdiary4():
    global work
    global work_entered
    
    Label(Aug, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Aug, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Augsave4)

def Augdiary5():
    global work
    global work_entered
    
    Label(Aug, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Aug, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Augsave5)

def Augdiary6():
    global work
    global work_entered
    
    Label(Aug, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Aug, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Augsave6)

def Augdiary7():
    global work
    global work_entered
    
    Label(Aug, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Aug, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Augsave7)

def Augdiary8():
    global work
    global work_entered
    
    Label(Aug, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Aug, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Augsave8)

def Augdiary9():
    global work
    global work_entered
    
    Label(Aug, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Aug, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Augsave9)

def Augdiary10():
    global work
    global work_entered
    
    Label(Aug, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Aug, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Augsave10)

def Augdiary11():
    global work
    global work_entered
    
    Label(Aug, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Aug, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Augsave11)

def Augdiary12():
    global work
    global work_entered
    
    Label(Aug, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Aug, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Augsave12)

def Augdiary13():
    global work
    global work_entered
    
    Label(Aug, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Aug, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Augsave13)

def Augdiary14():
    global work
    global work_entered
    
    Label(Aug, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Aug, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Augsave14)

def Augdiary15():
    global work
    global work_entered
    
    Label(Aug, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Aug, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Augsave15)

def Augdiary16():
    global work
    global work_entered
    
    Label(Aug, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Aug, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Augsave16)

def Augdiary17():
    global work
    global work_entered
    
    Label(Aug, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Aug, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Augsave17)

def Augdiary18():
    global work
    global work_entered
    
    Label(Aug, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Aug, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Augsave18)

def Augdiary19():
    global work
    global work_entered
    
    Label(Aug, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Aug, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Augsave19)

def Augdiary20():
    global work
    global work_entered
    
    Label(Aug, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Aug, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Augsave20)

def Augdiary21():
    global work
    global work_entered
    
    Label(Aug, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Aug, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Augsave21)

def Augdiary22():
    global work
    global work_entered
    
    Label(Aug, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Aug, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Augsave22)

def Augdiary23():
    global work
    global work_entered
    
    Label(Aug, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Aug, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Augsave23)

def Augdiary24():
    global work
    global work_entered
    
    Label(Aug, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Aug, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Augsave24)

def Augdiary25():
    global work
    global work_entered
    
    Label(Aug, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Aug, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Augsave25)

def Augdiary26():
    global work
    global work_entered
    
    Label(Aug, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Aug, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Augsave26)

def Augdiary27():
    global work
    global work_entered
    
    Label(Aug, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Aug, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Augsave27)

def Augdiary28():
    global work
    global work_entered
    
    Label(Aug, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Aug, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Augsave28)

def Augdiary29():
    global work
    global work_entered
    
    Label(Aug, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Aug, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Augsave29)

def Augdiary30():
    global work
    global work_entered
    
    Label(Aug, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Aug, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Augsav30)

def Augdiary31():
    global work
    global work_entered
    
    Label(Aug, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Aug, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Augsav31)

#==============================================================================================
      

#8월 일정을 저장 할 scrolledtext 만듦 (1월부터 12월까지 다 해줘야함)===============================
scrol_w=30
scrol_h=12
scr8=scrolledtext.ScrolledText(Aug, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr8.grid(column=10, row=1,columnspan=6, rowspan=6)
#==============================================================================================
    

#1일 부터 월의 최대 일까지의 버튼을 만든다. 19년도 달력을 보고 요일과 일이 매치되도록 함 일일이...
    
#8월 달력판====================================================================================
day1 = Button(Aug, text=" 1 ",command = Augdiary1)
day1.grid(column=5, row=1)
day2 = Button(Aug, text=" 2 ",command = Augdiary2)
day2.grid(column=6, row=1)
day3 = Button(Aug, text=" 3 ",command = Augdiary3)
day3.grid(column=7, row=1)
day4 = Button(Aug, text=" 4 ",command = Augdiary4)
day4.grid(column=1, row=2)
day5 = Button(Aug, text=" 5 ",command = Augdiary5)
day5.grid(column=2, row=2)
day6 = Button(Aug, text=" 6 ",command = Augdiary6)
day6.grid(column=3, row=2)
day7 = Button(Aug, text=" 7 ",command = Augdiary7)
day7.grid(column=4, row=2)
day8 = Button(Aug, text=" 8 ",command = Augdiary8)
day8.grid(column=5, row=2)
day9 = Button(Aug, text=" 9 ",command = Augdiary9)
day9.grid(column=6, row=2)
day10 = Button(Aug, text="10",command = Augdiary10)
day10.grid(column=7, row=2)
day11 = Button(Aug, text="11",command = Augdiary11)
day11.grid(column=1, row=3)
day12 = Button(Aug, text="12",command = Augdiary12)
day12.grid(column=2, row=3)
day13 = Button(Aug, text="13",command = Augdiary13)
day13.grid(column=3, row=3)
day14 = Button(Aug, text="14",command = Augdiary14)
day14.grid(column=4, row=3)
day15 = Button(Aug, text="15",command = Augdiary15)
day15.grid(column=5, row=3)
day16 = Button(Aug, text="16",command = Augdiary16)
day16.grid(column=6, row=3)
day17 = Button(Aug, text="17",command = Augdiary17)
day17.grid(column=7, row=3)
day18 = Button(Aug, text="18",command = Augdiary18)
day18.grid(column=1, row=4)
day19 = Button(Aug, text="19",command = Augdiary19)
day19.grid(column=2, row=4)
day20 = Button(Aug, text="20",command = Augdiary20)
day20.grid(column=3, row=4)
day21 = Button(Aug, text="21",command = Augdiary21)
day21.grid(column=4, row=4)
day22 = Button(Aug, text="22",command = Augdiary22)
day22.grid(column=5, row=4)
day23 = Button(Aug, text="23",command = Augdiary23)
day23.grid(column=6, row=4)
day24 = Button(Aug, text="24",command = Augdiary24)
day24.grid(column=7, row=4)
day25 = Button(Aug, text="25",command = Augdiary25)
day25.grid(column=1, row=5)
day26 = Button(Aug, text="26",command = Augdiary26)
day26.grid(column=2, row=5)
day27 = Button(Aug, text="27",command = Augdiary27)
day27.grid(column=3, row=5)
day28 = Button(Aug, text="28",command = Augdiary28)
day28.grid(column=4, row=5)
day29 = Button(Aug, text="29",command = Augdiary29)
day29.grid(column=5, row=5)
day30 = Button(Aug, text="30",command = Augdiary30)
day30.grid(column=6, row=5)
day31 = Button(Aug, text="31",command = Augdiary31)
day31.grid(column=7, row=5)
#===============================================================================================
##########################################################8월 끝#####################################################

##########################################################9월 시작#####################################################
#9월 n일을 입력하는 함수=========================================================
def Sepsave1(self):
    value = work.get()
    scr9.insert(tk.INSERT, 'Day1 = ' + value + '\n')
    print('Sep Day1 schedule = ' + value + '\n')

def Sepsave2(self):
    value = work.get()
    scr9.insert(tk.INSERT, 'Day2 = ' + value + '\n')
    print('Sep Day2 schedule = ' + value + '\n')

def Sepsave3(self):
    value = work.get()
    scr9.insert(tk.INSERT, 'Day3 = ' + value + '\n')
    print('Sep Day3 schedule = ' + value + '\n')

def Sepsave4(self):
    value = work.get()
    scr9.insert(tk.INSERT, 'Day4 = ' + value + '\n')
    print('Sep Day4 schedule = ' + value + '\n')

def Sepsave5(self):
    value = work.get()
    scr9.insert(tk.INSERT, 'Day5 = ' + value + '\n')
    print('Sep Day5 schedule = ' + value + '\n')

def Sepsave6(self):
    value = work.get()
    scr9.insert(tk.INSERT, 'Day6 = ' + value + '\n')
    print('Sep Day6 schedule = ' + value + '\n')

def Sepsave7(self):
    value = work.get()
    scr9.insert(tk.INSERT, 'Day7 = ' + value + '\n')
    print('Sep Day7 schedule = ' + value + '\n')

def Sepsave8(self):
    value = work.get()
    scr9.insert(tk.INSERT, 'Day8 = ' + value + '\n')
    print('Sep Day8 schedule = ' + value + '\n')

def Sepsave9(self):
    value = work.get()
    scr9.insert(tk.INSERT, 'Day9 = ' + value + '\n')
    print('Sep Day9 schedule = ' + value + '\n')

def Sepsave10(self):
    value = work.get()
    scr9.insert(tk.INSERT, 'Day10 = ' + value + '\n')
    print('Sep Day10 schedule = ' + value + '\n')

def Sepsave11(self):
    value = work.get()
    scr9.insert(tk.INSERT, 'Day11 = ' + value + '\n')
    print('Sep Day11 schedule = ' + value + '\n')

def Sepsave12(self):
    value = work.get()
    scr9.insert(tk.INSERT, 'Day12 = ' + value + '\n')
    print('Sep Day12 schedule = ' + value + '\n')

def Sepsave13(self):
    value = work.get()
    scr9.insert(tk.INSERT, 'Day13 = ' + value + '\n')
    print('Sep Day13 schedule = ' + value + '\n')

def Sepsave14(self):
    value = work.get()
    scr9.insert(tk.INSERT, 'Day14 = ' + value + '\n')
    print('Sep Day1 schedule = ' + value + '\n')

def Sepsave15(self):
    value = work.get()
    scr9.insert(tk.INSERT, 'Day15 = ' + value + '\n')
    print('Sep Day15 schedule = ' + value + '\n')

def Sepsave16(self):
    value = work.get()
    scr9.insert(tk.INSERT, 'Day16 = ' + value + '\n')
    print('Sep Day16 schedule = ' + value + '\n')

def Sepsave17(self):
    value = work.get()
    scr9.insert(tk.INSERT, 'Day17 = ' + value + '\n')
    print('Sep Day17 schedule = ' + value + '\n')

def Sepsave18(self):
    value = work.get()
    scr9.insert(tk.INSERT, 'Day18 = ' + value + '\n')
    print('Sep Day18 schedule = ' + value + '\n')

def Sepsave19(self):
    value = work.get()
    scr9.insert(tk.INSERT, 'Day19 = ' + value + '\n')
    print('Sep Day19 schedule = ' + value + '\n')

def Sepsave20(self):
    value = work.get()
    scr9.insert(tk.INSERT, 'Day20 = ' + value + '\n')
    print('Sep Day20 schedule = ' + value + '\n')

def Sepsave21(self):
    value = work.get()
    scr9.insert(tk.INSERT, 'Day21 = ' + value + '\n')
    print('Sep Day21 schedule = ' + value + '\n')

def Sepsave22(self):
    value = work.get()
    scr9.insert(tk.INSERT, 'Day22 = ' + value + '\n')
    print('Sep Day22 schedule = ' + value + '\n')

def Sepsave23(self):
    value = work.get()
    scr9.insert(tk.INSERT, 'Day23 = ' + value + '\n')
    print('Sep Day23 schedule = ' + value + '\n')

def Sepsave24(self):
    value = work.get()
    scr9.insert(tk.INSERT, 'Day24 = ' + value + '\n')
    print('Sep Day24 schedule = ' + value + '\n')

def Sepsave25(self):
    value = work.get()
    scr9.insert(tk.INSERT, 'Day25 = ' + value + '\n')
    print('Sep Day25 schedule = ' + value + '\n')

def Sepsave26(self):
    value = work.get()
    scr9.insert(tk.INSERT, 'Day26 = ' + value + '\n')
    print('Sep Day26 schedule = ' + value + '\n')

def Sepsave27(self):
    value = work.get()
    scr9.insert(tk.INSERT, 'Day27 = ' + value + '\n')
    print('Sep Day27 schedule = ' + value + '\n')

def Sepsave28(self):
    value = work.get()
    scr9.insert(tk.INSERT, 'Day28 = ' + value + '\n')
    print('Sep Day28 schedule = ' + value + '\n')

def Sepsave29(self):
    value = work.get()
    scr9.insert(tk.INSERT, 'Day29 = ' + value + '\n')
    print('Sep Day29 schedule = ' + value + '\n')

def Sepsave30(self):
    value = work.get()
    scr9.insert(tk.INSERT, 'Day30 = ' + value + '\n')
    print('Sep Day30 schedule = ' + value + '\n')


#============================================================


#콜백되면 Entry가 생성되고, 입력시 스크롤텍스트에 출력할 수 있음 (일마다 하나씩 만들어줘야함)
def Sepdiary1():
    global work
    global work_entered
    
    Label(Sep, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Sep, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Sepsave1)

def Sepdiary2():
    global work
    global work_entered
    
    Label(Sep, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Sep, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Sepsave2)

def Sepdiary3():
    global work
    global work_entered
    
    Label(Sep, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Sep, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Sepsave3)

def Sepdiary4():
    global work
    global work_entered
    
    Label(Sep, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Sep, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Sepsave4)

def Sepdiary5():
    global work
    global work_entered
    
    Label(Sep, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Sep, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Sepsave5)

def Sepdiary6():
    global work
    global work_entered
    
    Label(Sep, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Sep, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Sepsave6)

def Sepdiary7():
    global work
    global work_entered
    
    Label(Sep, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Sep, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Sepsave7)

def Sepdiary8():
    global work
    global work_entered
    
    Label(Sep, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Sep, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Sepsave8)

def Sepdiary9():
    global work
    global work_entered
    
    Label(Sep, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Sep, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Sepsave9)

def Sepdiary10():
    global work
    global work_entered
    
    Label(Sep, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Sep, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Sepsave10)

def Sepdiary11():
    global work
    global work_entered
    
    Label(Sep, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Sep, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Sepsave11)

def Sepdiary12():
    global work
    global work_entered
    
    Label(Sep, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Sep, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Sepsave12)

def Sepdiary13():
    global work
    global work_entered
    
    Label(Sep, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Sep, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Sepsave13)

def Sepdiary14():
    global work
    global work_entered
    
    Label(Sep, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Sep, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Sepsave14)

def Sepdiary15():
    global work
    global work_entered
    
    Label(Sep, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Sep, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Sepsave15)

def Sepdiary16():
    global work
    global work_entered
    
    Label(Sep, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Sep, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Sepsave16)

def Sepdiary17():
    global work
    global work_entered
    
    Label(Sep, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Sep, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Sepsave17)

def Sepdiary18():
    global work
    global work_entered
    
    Label(Sep, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Sep, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Sepsave18)

def Sepdiary19():
    global work
    global work_entered
    
    Label(Sep, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Sep, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Sepsave19)

def Sepdiary20():
    global work
    global work_entered
    
    Label(Sep, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Sep, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Sepsave20)

def Sepdiary21():
    global work
    global work_entered
    
    Label(Sep, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Sep, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Sepsave21)

def Sepdiary22():
    global work
    global work_entered
    
    Label(Sep, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Sep, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Sepsave22)

def Sepdiary23():
    global work
    global work_entered
    
    Label(Sep, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Sep, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Sepsave23)

def Sepdiary24():
    global work
    global work_entered
    
    Label(Sep, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Sep, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Sepsave24)

def Sepdiary25():
    global work
    global work_entered
    
    Label(Sep, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Sep, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Sepsave25)

def Sepdiary26():
    global work
    global work_entered
    
    Label(Sep, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Sep, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Sepsave26)

def Sepdiary27():
    global work
    global work_entered
    
    Label(Sep, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Sep, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Sepsave27)

def Sepdiary28():
    global work
    global work_entered
    
    Label(Sep, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Sep, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Sepsave28)

def Sepdiary29():
    global work
    global work_entered
    
    Label(Sep, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Sep, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Sepsave29)

def Sepdiary30():
    global work
    global work_entered
    
    Label(Sep, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Sep, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Sepsav30)

#==============================================================================================
      

#9월 일정을 저장 할 scrolledtext 만듦 (1월부터 12월까지 다 해줘야함)===============================
scrol_w=30
scrol_h=12
scr9=scrolledtext.ScrolledText(Sep, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr9.grid(column=10, row=1,columnspan=6, rowspan=6)
#==============================================================================================
    

#1일 부터 월의 최대 일까지의 버튼을 만든다. 19년도 달력을 보고 요일과 일이 매치되도록 함 일일이...
    
#9월 달력판====================================================================================
day1 = Button(Sep, text=" 1 ",command = Sepdiary1)
day1.grid(column=1, row=1)
day2 = Button(Sep, text=" 2 ",command = Sepdiary2)
day2.grid(column=2, row=1)
day3 = Button(Sep, text=" 3 ",command = Sepdiary3)
day3.grid(column=3, row=1)
day4 = Button(Sep, text=" 4 ",command = Sepdiary4)
day4.grid(column=4, row=1)
day5 = Button(Sep, text=" 5 ",command = Sepdiary5)
day5.grid(column=5, row=1)
day6 = Button(Sep, text=" 6 ",command = Sepdiary6)
day6.grid(column=6, row=1)
day7 = Button(Sep, text=" 7 ",command = Sepdiary7)
day7.grid(column=7, row=1)
day8 = Button(Sep, text=" 8 ",command = Sepdiary8)
day8.grid(column=1, row=2)
day9 = Button(Sep, text=" 9 ",command = Sepdiary9)
day9.grid(column=2, row=2)
day10 = Button(Sep, text="10",command = Sepdiary10)
day10.grid(column=3, row=2)
day11 = Button(Sep, text="11",command = Sepdiary11)
day11.grid(column=4, row=2)
day12 = Button(Sep, text="12",command = Sepdiary12)
day12.grid(column=5, row=2)
day13 = Button(Sep, text="13",command = Sepdiary13)
day13.grid(column=6, row=2)
day14 = Button(Sep, text="14",command = Sepdiary14)
day14.grid(column=7, row=2)
day15 = Button(Sep, text="15",command = Sepdiary15)
day15.grid(column=1, row=3)
day16 = Button(Sep, text="16",command = Sepdiary16)
day16.grid(column=2, row=3)
day17 = Button(Sep, text="17",command = Sepdiary17)
day17.grid(column=3, row=3)
day18 = Button(Sep, text="18",command = Sepdiary18)
day18.grid(column=4, row=3)
day19 = Button(Sep, text="19",command = Sepdiary19)
day19.grid(column=5, row=3)
day20 = Button(Sep, text="20",command = Sepdiary20)
day20.grid(column=6, row=3)
day21 = Button(Sep, text="21",command = Sepdiary21)
day21.grid(column=7, row=3)
day22 = Button(Sep, text="22",command = Sepdiary22)
day22.grid(column=1, row=4)
day23 = Button(Sep, text="23",command = Sepdiary23)
day23.grid(column=2, row=4)
day24 = Button(Sep, text="24",command = Sepdiary24)
day24.grid(column=3, row=4)
day25 = Button(Sep, text="25",command = Sepdiary25)
day25.grid(column=4, row=4)
day26 = Button(Sep, text="26",command = Sepdiary26)
day26.grid(column=5, row=4)
day27 = Button(Sep, text="27",command = Sepdiary27)
day27.grid(column=6, row=4)
day28 = Button(Sep, text="28",command = Sepdiary28)
day28.grid(column=7, row=4)
day29 = Button(Sep, text="29",command = Sepdiary29)
day29.grid(column=1, row=5)
day30 = Button(Sep, text="30",command = Sepdiary30)
day30.grid(column=2, row=5)

#===============================================================================================
##########################################################9월 끝#####################################################

##########################################################10월 시작#####################################################
#10월 n일을 입력하는 함수=========================================================
def Octsave1(self):
    value = work.get()
    scr10.insert(tk.INSERT, 'Day1 = ' + value + '\n')
    print('Oct Day1 schedule = ' + value + '\n')

def Octsave2(self):
    value = work.get()
    scr10.insert(tk.INSERT, 'Day2 = ' + value + '\n')
    print('Oct Day2 schedule = ' + value + '\n')

def Octsave3(self):
    value = work.get()
    scr10.insert(tk.INSERT, 'Day3 = ' + value + '\n')
    print('Oct Day3 schedule = ' + value + '\n')

def Octsave4(self):
    value = work.get()
    scr10.insert(tk.INSERT, 'Day4 = ' + value + '\n')
    print('Oct Day4 schedule = ' + value + '\n')

def Octsave5(self):
    value = work.get()
    scr10.insert(tk.INSERT, 'Day5 = ' + value + '\n')
    print('Oct Day5 schedule = ' + value + '\n')

def Octsave6(self):
    value = work.get()
    scr10.insert(tk.INSERT, 'Day6 = ' + value + '\n')
    print('Oct Day6 schedule = ' + value + '\n')

def Octsave7(self):
    value = work.get()
    scr10.insert(tk.INSERT, 'Day7 = ' + value + '\n')
    print('Oct Day7 schedule = ' + value + '\n')

def Octsave8(self):
    value = work.get()
    scr10.insert(tk.INSERT, 'Day8 = ' + value + '\n')
    print('Oct Day8 schedule = ' + value + '\n')

def Octsave9(self):
    value = work.get()
    scr10.insert(tk.INSERT, 'Day9 = ' + value + '\n')
    print('Oct Day9 schedule = ' + value + '\n')

def Octsave10(self):
    value = work.get()
    scr10.insert(tk.INSERT, 'Day10 = ' + value + '\n')
    print('Oct Day10 schedule = ' + value + '\n')

def Octsave11(self):
    value = work.get()
    scr10.insert(tk.INSERT, 'Day11 = ' + value + '\n')
    print('Oct Day11 schedule = ' + value + '\n')

def Octsave12(self):
    value = work.get()
    scr10.insert(tk.INSERT, 'Day12 = ' + value + '\n')
    print('Oct Day12 schedule = ' + value + '\n')

def Octsave13(self):
    value = work.get()
    scr10.insert(tk.INSERT, 'Day13 = ' + value + '\n')
    print('Oct Day13 schedule = ' + value + '\n')

def Octsave14(self):
    value = work.get()
    scr10.insert(tk.INSERT, 'Day14 = ' + value + '\n')
    print('Oct Day1 schedule = ' + value + '\n')

def Octsave15(self):
    value = work.get()
    scr10.insert(tk.INSERT, 'Day15 = ' + value + '\n')
    print('Oct Day15 schedule = ' + value + '\n')

def Octsave16(self):
    value = work.get()
    scr10.insert(tk.INSERT, 'Day16 = ' + value + '\n')
    print('Oct Day16 schedule = ' + value + '\n')

def Octsave17(self):
    value = work.get()
    scr10.insert(tk.INSERT, 'Day17 = ' + value + '\n')
    print('Oct Day17 schedule = ' + value + '\n')

def Octsave18(self):
    value = work.get()
    scr10.insert(tk.INSERT, 'Day18 = ' + value + '\n')
    print('Oct Day18 schedule = ' + value + '\n')

def Octsave19(self):
    value = work.get()
    scr10.insert(tk.INSERT, 'Day19 = ' + value + '\n')
    print('Oct Day19 schedule = ' + value + '\n')

def Octsave20(self):
    value = work.get()
    scr10.insert(tk.INSERT, 'Day20 = ' + value + '\n')
    print('Oct Day20 schedule = ' + value + '\n')

def Octsave21(self):
    value = work.get()
    scr10.insert(tk.INSERT, 'Day21 = ' + value + '\n')
    print('Oct Day21 schedule = ' + value + '\n')

def Octsave22(self):
    value = work.get()
    scr10.insert(tk.INSERT, 'Day22 = ' + value + '\n')
    print('Oct Day22 schedule = ' + value + '\n')

def Octsave23(self):
    value = work.get()
    scr10.insert(tk.INSERT, 'Day23 = ' + value + '\n')
    print('Oct Day23 schedule = ' + value + '\n')

def Octsave24(self):
    value = work.get()
    scr10.insert(tk.INSERT, 'Day24 = ' + value + '\n')
    print('Oct Day24 schedule = ' + value + '\n')

def Octsave25(self):
    value = work.get()
    scr10.insert(tk.INSERT, 'Day25 = ' + value + '\n')
    print('Oct Day25 schedule = ' + value + '\n')

def Octsave26(self):
    value = work.get()
    scr10.insert(tk.INSERT, 'Day26 = ' + value + '\n')
    print('Oct Day26 schedule = ' + value + '\n')

def Octsave27(self):
    value = work.get()
    scr10.insert(tk.INSERT, 'Day27 = ' + value + '\n')
    print('Oct Day27 schedule = ' + value + '\n')

def Octsave28(self):
    value = work.get()
    scr10.insert(tk.INSERT, 'Day28 = ' + value + '\n')
    print('Oct Day28 schedule = ' + value + '\n')

def Octsave29(self):
    value = work.get()
    scr10.insert(tk.INSERT, 'Day29 = ' + value + '\n')
    print('Oct Day29 schedule = ' + value + '\n')

def Octsave30(self):
    value = work.get()
    scr10.insert(tk.INSERT, 'Day30 = ' + value + '\n')
    print('Oct Day30 schedule = ' + value + '\n')

def Octsave31(self):
    value = work.get()
    scr10.insert(tk.INSERT, 'Day31 = ' + value + '\n')
    print('Oct Day31 schedule = ' + value + '\n')


#============================================================


#콜백되면 Entry가 생성되고, 입력시 스크롤텍스트에 출력할 수 있음 (일마다 하나씩 만들어줘야함)
def Octdiary1():
    global work
    global work_entered
    
    Label(Oct, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Oct, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Octsave1)

def Octdiary2():
    global work
    global work_entered
    
    Label(Oct, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Oct, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Octsave2)

def Octdiary3():
    global work
    global work_entered
    
    Label(Oct, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Oct, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Octsave3)

def Octdiary4():
    global work
    global work_entered
    
    Label(Oct, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Oct, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Octsave4)

def Octdiary5():
    global work
    global work_entered
    
    Label(Oct, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Oct, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Octsave5)

def Octdiary6():
    global work
    global work_entered
    
    Label(Oct, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Oct, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Octsave6)

def Octdiary7():
    global work
    global work_entered
    
    Label(Oct, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Oct, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Octsave7)

def Octdiary8():
    global work
    global work_entered
    
    Label(Oct, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Oct, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Octsave8)

def Octdiary9():
    global work
    global work_entered
    
    Label(Oct, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Oct, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Octsave9)

def Octdiary10():
    global work
    global work_entered
    
    Label(Oct, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Oct, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Octsave10)

def Octdiary11():
    global work
    global work_entered
    
    Label(Oct, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Oct, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Octsave11)

def Octdiary12():
    global work
    global work_entered
    
    Label(Oct, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Oct, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Octsave12)

def Octdiary13():
    global work
    global work_entered
    
    Label(Oct, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Oct, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Octsave13)

def Octdiary14():
    global work
    global work_entered
    
    Label(Oct, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Oct, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Octsave14)

def Octdiary15():
    global work
    global work_entered
    
    Label(Oct, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Oct, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Octsave15)

def Octdiary16():
    global work
    global work_entered
    
    Label(Oct, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Oct, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Octsave16)

def Octdiary17():
    global work
    global work_entered
    
    Label(Oct, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Oct, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Octsave17)

def Octdiary18():
    global work
    global work_entered
    
    Label(Oct, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Oct, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Octsave18)

def Octdiary19():
    global work
    global work_entered
    
    Label(Oct, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Oct, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Octsave19)

def Octdiary20():
    global work
    global work_entered
    
    Label(Oct, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Oct, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Octsave20)

def Octdiary21():
    global work
    global work_entered
    
    Label(Oct, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Oct, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Octsave21)

def Octdiary22():
    global work
    global work_entered
    
    Label(Oct, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Oct, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Octsave22)

def Octdiary23():
    global work
    global work_entered
    
    Label(Oct, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Oct, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Octsave23)

def Octdiary24():
    global work
    global work_entered
    
    Label(Oct, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Oct, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Octsave24)

def Octdiary25():
    global work
    global work_entered
    
    Label(Oct, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Oct, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Octsave25)

def Octdiary26():
    global work
    global work_entered
    
    Label(Oct, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Oct, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Octsave26)

def Octdiary27():
    global work
    global work_entered
    
    Label(Oct, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Oct, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Octsave27)

def Octdiary28():
    global work
    global work_entered
    
    Label(Oct, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Oct, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Octsave28)

def Octdiary29():
    global work
    global work_entered
    
    Label(Oct, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Oct, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Octsave29)

def Octdiary30():
    global work
    global work_entered
    
    Label(Oct, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Oct, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Octsav30)

def Octdiary31():
    global work
    global work_entered
    
    Label(Oct, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Oct, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Octsav31)

#==============================================================================================
      

#10월 일정을 저장 할 scrolledtext 만듦 (1월부터 12월까지 다 해줘야함)===============================
scrol_w=30
scrol_h=12
scr10=scrolledtext.ScrolledText(Oct, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr10.grid(column=10, row=1,columnspan=6, rowspan=6)
#==============================================================================================
    

#1일 부터 월의 최대 일까지의 버튼을 만든다. 19년도 달력을 보고 요일과 일이 매치되도록 함 일일이...
    
#10월 달력판====================================================================================
day1 = Button(Oct, text=" 1 ",command = Octdiary1)
day1.grid(column=3, row=1)
day2 = Button(Oct, text=" 2 ",command = Octdiary2)
day2.grid(column=4, row=1)
day3 = Button(Oct, text=" 3 ",command = Octdiary3)
day3.grid(column=5, row=1)
day4 = Button(Oct, text=" 4 ",command = Octdiary4)
day4.grid(column=6, row=1)
day5 = Button(Oct, text=" 5 ",command = Octdiary5)
day5.grid(column=7, row=1)
day6 = Button(Oct, text=" 6 ",command = Octdiary6)
day6.grid(column=1, row=2)
day7 = Button(Oct, text=" 7 ",command = Octdiary7)
day7.grid(column=2, row=2)
day8 = Button(Oct, text=" 8 ",command = Octdiary8)
day8.grid(column=3, row=2)
day9 = Button(Oct, text=" 9 ",command = Octdiary9)
day9.grid(column=4, row=2)
day10 = Button(Oct, text="10",command = Octdiary10)
day10.grid(column=5, row=2)
day11 = Button(Oct, text="11",command = Octdiary11)
day11.grid(column=6, row=2)
day12 = Button(Oct, text="12",command = Octdiary12)
day12.grid(column=7, row=2)
day13 = Button(Oct, text="13",command = Octdiary13)
day13.grid(column=1, row=3)
day14 = Button(Oct, text="14",command = Octdiary14)
day14.grid(column=2, row=3)
day15 = Button(Oct, text="15",command = Octdiary15)
day15.grid(column=3, row=3)
day16 = Button(Oct, text="16",command = Octdiary16)
day16.grid(column=4, row=3)
day17 = Button(Oct, text="17",command = Octdiary17)
day17.grid(column=5, row=3)
day18 = Button(Oct, text="18",command = Octdiary18)
day18.grid(column=6, row=3)
day19 = Button(Oct, text="19",command = Octdiary19)
day19.grid(column=7, row=3)
day20 = Button(Oct, text="20",command = Octdiary20)
day20.grid(column=1, row=4)
day21 = Button(Oct, text="21",command = Octdiary21)
day21.grid(column=2, row=4)
day22 = Button(Oct, text="22",command = Octdiary22)
day22.grid(column=3, row=4)
day23 = Button(Oct, text="23",command = Octdiary23)
day23.grid(column=4, row=4)
day24 = Button(Oct, text="24",command = Octdiary24)
day24.grid(column=5, row=4)
day25 = Button(Oct, text="25",command = Octdiary25)
day25.grid(column=6, row=4)
day26 = Button(Oct, text="26",command = Octdiary26)
day26.grid(column=7, row=4)
day27 = Button(Oct, text="27",command = Octdiary27)
day27.grid(column=1, row=5)
day28 = Button(Oct, text="28",command = Octdiary28)
day28.grid(column=2, row=5)
day29 = Button(Oct, text="29",command = Octdiary29)
day29.grid(column=3, row=5)
day30 = Button(Oct, text="30",command = Octdiary30)
day30.grid(column=4, row=5)
day31 = Button(Oct, text="31",command = Octdiary31)
day31.grid(column=5, row=5)
#===============================================================================================
##########################################################10월 끝#####################################################

##########################################################11월 시작#####################################################
#11월 n일을 입력하는 함수=========================================================
def Novsave1(self):
    value = work.get()
    scr11.insert(tk.INSERT, 'Day1 = ' + value + '\n')
    print('Nov Day1 schedule = ' + value + '\n')

def Novsave2(self):
    value = work.get()
    scr11.insert(tk.INSERT, 'Day2 = ' + value + '\n')
    print('Nov Day2 schedule = ' + value + '\n')

def Novsave3(self):
    value = work.get()
    scr11.insert(tk.INSERT, 'Day3 = ' + value + '\n')
    print('Nov Day3 schedule = ' + value + '\n')

def Novsave4(self):
    value = work.get()
    scr11.insert(tk.INSERT, 'Day4 = ' + value + '\n')
    print('Nov Day4 schedule = ' + value + '\n')

def Novsave5(self):
    value = work.get()
    scr11.insert(tk.INSERT, 'Day5 = ' + value + '\n')
    print('Nov Day5 schedule = ' + value + '\n')

def Novsave6(self):
    value = work.get()
    scr11.insert(tk.INSERT, 'Day6 = ' + value + '\n')
    print('Nov Day6 schedule = ' + value + '\n')

def Novsave7(self):
    value = work.get()
    scr11.insert(tk.INSERT, 'Day7 = ' + value + '\n')
    print('Nov Day7 schedule = ' + value + '\n')

def Novsave8(self):
    value = work.get()
    scr11.insert(tk.INSERT, 'Day8 = ' + value + '\n')
    print('Nov Day8 schedule = ' + value + '\n')

def Novsave9(self):
    value = work.get()
    scr11.insert(tk.INSERT, 'Day9 = ' + value + '\n')
    print('Nov Day9 schedule = ' + value + '\n')

def Novsave10(self):
    value = work.get()
    scr11.insert(tk.INSERT, 'Day10 = ' + value + '\n')
    print('Nov Day10 schedule = ' + value + '\n')

def Novsave11(self):
    value = work.get()
    scr11.insert(tk.INSERT, 'Day11 = ' + value + '\n')
    print('Nov Day11 schedule = ' + value + '\n')

def Novsave12(self):
    value = work.get()
    scr11.insert(tk.INSERT, 'Day12 = ' + value + '\n')
    print('Nov Day12 schedule = ' + value + '\n')

def Novsave13(self):
    value = work.get()
    scr11.insert(tk.INSERT, 'Day13 = ' + value + '\n')
    print('Nov Day13 schedule = ' + value + '\n')

def Novsave14(self):
    value = work.get()
    scr11.insert(tk.INSERT, 'Day14 = ' + value + '\n')
    print('Nov Day1 schedule = ' + value + '\n')

def Novsave15(self):
    value = work.get()
    scr11.insert(tk.INSERT, 'Day15 = ' + value + '\n')
    print('Nov Day15 schedule = ' + value + '\n')

def Novsave16(self):
    value = work.get()
    scr11.insert(tk.INSERT, 'Day16 = ' + value + '\n')
    print('Nov Day16 schedule = ' + value + '\n')

def Novsave17(self):
    value = work.get()
    scr11.insert(tk.INSERT, 'Day17 = ' + value + '\n')
    print('Nov Day17 schedule = ' + value + '\n')

def Novsave18(self):
    value = work.get()
    scr11.insert(tk.INSERT, 'Day18 = ' + value + '\n')
    print('Nov Day18 schedule = ' + value + '\n')

def Novsave19(self):
    value = work.get()
    scr11.insert(tk.INSERT, 'Day19 = ' + value + '\n')
    print('Nov Day19 schedule = ' + value + '\n')

def Novsave20(self):
    value = work.get()
    scr11.insert(tk.INSERT, 'Day20 = ' + value + '\n')
    print('Nov Day20 schedule = ' + value + '\n')

def Novsave21(self):
    value = work.get()
    scr11.insert(tk.INSERT, 'Day21 = ' + value + '\n')
    print('Nov Day21 schedule = ' + value + '\n')

def Novsave22(self):
    value = work.get()
    scr11.insert(tk.INSERT, 'Day22 = ' + value + '\n')
    print('Nov Day22 schedule = ' + value + '\n')

def Novsave23(self):
    value = work.get()
    scr11.insert(tk.INSERT, 'Day23 = ' + value + '\n')
    print('Nov Day23 schedule = ' + value + '\n')

def Novsave24(self):
    value = work.get()
    scr11.insert(tk.INSERT, 'Day24 = ' + value + '\n')
    print('Nov Day24 schedule = ' + value + '\n')

def Novsave25(self):
    value = work.get()
    scr11.insert(tk.INSERT, 'Day25 = ' + value + '\n')
    print('Nov Day25 schedule = ' + value + '\n')

def Novsave26(self):
    value = work.get()
    scr11.insert(tk.INSERT, 'Day26 = ' + value + '\n')
    print('Nov Day26 schedule = ' + value + '\n')

def Novsave27(self):
    value = work.get()
    scr11.insert(tk.INSERT, 'Day27 = ' + value + '\n')
    print('Nov Day27 schedule = ' + value + '\n')

def Novsave28(self):
    value = work.get()
    scr11.insert(tk.INSERT, 'Day28 = ' + value + '\n')
    print('Nov Day28 schedule = ' + value + '\n')

def Novsave29(self):
    value = work.get()
    scr11.insert(tk.INSERT, 'Day29 = ' + value + '\n')
    print('Nov Day29 schedule = ' + value + '\n')

def Novsave30(self):
    value = work.get()
    scr11.insert(tk.INSERT, 'Day30 = ' + value + '\n')
    print('Nov Day30 schedule = ' + value + '\n')


#============================================================


#콜백되면 Entry가 생성되고, 입력시 스크롤텍스트에 출력할 수 있음 (일마다 하나씩 만들어줘야함)
def Novdiary1():
    global work
    global work_entered
    
    Label(Nov, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Nov, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Novsave1)

def Novdiary2():
    global work
    global work_entered
    
    Label(Nov, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Nov, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Novsave2)

def Novdiary3():
    global work
    global work_entered
    
    Label(Nov, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Nov, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Novsave3)

def Novdiary4():
    global work
    global work_entered
    
    Label(Nov, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Nov, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Novsave4)

def Novdiary5():
    global work
    global work_entered
    
    Label(Nov, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Nov, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Novsave5)

def Novdiary6():
    global work
    global work_entered
    
    Label(Nov, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Nov, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Novsave6)

def Novdiary7():
    global work
    global work_entered
    
    Label(Nov, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Nov, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Novsave7)

def Novdiary8():
    global work
    global work_entered
    
    Label(Nov, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Nov, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Novsave8)

def Novdiary9():
    global work
    global work_entered
    
    Label(Nov, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Nov, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Novsave9)

def Novdiary10():
    global work
    global work_entered
    
    Label(Nov, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Nov, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Novsave10)

def Novdiary11():
    global work
    global work_entered
    
    Label(Nov, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Nov, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Novsave11)

def Novdiary12():
    global work
    global work_entered
    
    Label(Nov, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Nov, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Novsave12)

def Novdiary13():
    global work
    global work_entered
    
    Label(Nov, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Nov, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Novsave13)

def Novdiary14():
    global work
    global work_entered
    
    Label(Nov, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Nov, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Novsave14)

def Novdiary15():
    global work
    global work_entered
    
    Label(Nov, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Nov, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Novsave15)

def Novdiary16():
    global work
    global work_entered
    
    Label(Nov, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Nov, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Novsave16)

def Novdiary17():
    global work
    global work_entered
    
    Label(Nov, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Nov, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Novsave17)

def Novdiary18():
    global work
    global work_entered
    
    Label(Nov, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Nov, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Novsave18)

def Novdiary19():
    global work
    global work_entered
    
    Label(Nov, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Nov, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Novsave19)

def Novdiary20():
    global work
    global work_entered
    
    Label(Nov, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Nov, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Novsave20)

def Novdiary21():
    global work
    global work_entered
    
    Label(Nov, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Nov, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Novsave21)

def Novdiary22():
    global work
    global work_entered
    
    Label(Nov, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Nov, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Novsave22)

def Novdiary23():
    global work
    global work_entered
    
    Label(Nov, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Nov, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Novsave23)

def Novdiary24():
    global work
    global work_entered
    
    Label(Nov, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Nov, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Novsave24)

def Novdiary25():
    global work
    global work_entered
    
    Label(Nov, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Nov, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Novsave25)

def Novdiary26():
    global work
    global work_entered
    
    Label(Nov, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Nov, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Novsave26)

def Novdiary27():
    global work
    global work_entered
    
    Label(Nov, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Nov, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Novsave27)

def Novdiary28():
    global work
    global work_entered
    
    Label(Nov, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Nov, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Novsave28)

def Novdiary29():
    global work
    global work_entered
    
    Label(Nov, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Nov, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Novsave29)

def Novdiary30():
    global work
    global work_entered
    
    Label(Nov, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Nov, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Novsav30)

#==============================================================================================
      

#11월 일정을 저장 할 scrolledtext 만듦 (1월부터 12월까지 다 해줘야함)===============================
scrol_w=30
scrol_h=12
scr11=scrolledtext.ScrolledText(Nov, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr11.grid(column=10, row=1,columnspan=6, rowspan=6)
#==============================================================================================
    

#1일 부터 월의 최대 일까지의 버튼을 만든다. 19년도 달력을 보고 요일과 일이 매치되도록 함 일일이...
    
#11월 달력판====================================================================================
day1 = Button(Nov, text=" 1 ",command = Novdiary1)
day1.grid(column=6, row=1)
day2 = Button(Nov, text=" 2 ",command = Novdiary2)
day2.grid(column=7, row=1)
day3 = Button(Nov, text=" 3 ",command = Novdiary3)
day3.grid(column=1, row=2)
day4 = Button(Nov, text=" 4 ",command = Novdiary4)
day4.grid(column=2, row=2)
day5 = Button(Nov, text=" 5 ",command = Novdiary5)
day5.grid(column=3, row=2)
day6 = Button(Nov, text=" 6 ",command = Novdiary6)
day6.grid(column=4, row=2)
day7 = Button(Nov, text=" 7 ",command = Novdiary7)
day7.grid(column=5, row=2)
day8 = Button(Nov, text=" 8 ",command = Novdiary8)
day8.grid(column=6, row=2)
day9 = Button(Nov, text=" 9 ",command = Novdiary9)
day9.grid(column=7, row=2)
day10 = Button(Nov, text="10",command = Novdiary10)
day10.grid(column=1, row=3)
day11 = Button(Nov, text="11",command = Novdiary11)
day11.grid(column=2, row=3)
day12 = Button(Nov, text="12",command = Novdiary12)
day12.grid(column=3, row=3)
day13 = Button(Nov, text="13",command = Novdiary13)
day13.grid(column=4, row=3)
day14 = Button(Nov, text="14",command = Novdiary14)
day14.grid(column=5, row=3)
day15 = Button(Nov, text="15",command = Novdiary15)
day15.grid(column=6, row=3)
day16 = Button(Nov, text="16",command = Novdiary16)
day16.grid(column=7, row=3)
day17 = Button(Nov, text="17",command = Novdiary17)
day17.grid(column=1, row=4)
day18 = Button(Nov, text="18",command = Novdiary18)
day18.grid(column=2, row=4)
day19 = Button(Nov, text="19",command = Novdiary19)
day19.grid(column=3, row=4)
day20 = Button(Nov, text="20",command = Novdiary20)
day20.grid(column=4, row=4)
day21 = Button(Nov, text="21",command = Novdiary21)
day21.grid(column=5, row=4)
day22 = Button(Nov, text="22",command = Novdiary22)
day22.grid(column=6, row=4)
day23 = Button(Nov, text="23",command = Novdiary23)
day23.grid(column=7, row=4)
day24 = Button(Nov, text="24",command = Novdiary24)
day24.grid(column=1, row=5)
day25 = Button(Nov, text="25",command = Novdiary25)
day25.grid(column=2, row=5)
day26 = Button(Nov, text="26",command = Novdiary26)
day26.grid(column=3, row=5)
day27 = Button(Nov, text="27",command = Novdiary27)
day27.grid(column=4, row=5)
day28 = Button(Nov, text="28",command = Novdiary28)
day28.grid(column=5, row=5)
day29 = Button(Nov, text="29",command = Novdiary29)
day29.grid(column=6, row=5)
day30 = Button(Nov, text="30",command = Novdiary30)
day30.grid(column=7, row=5)

#===============================================================================================
##########################################################11월 끝#####################################################

##########################################################12월 시작#####################################################
#12월 n일을 입력하는 함수=========================================================
def Decsave1(self):
    value = work.get()
    scr12.insert(tk.INSERT, 'Day1 = ' + value + '\n')
    print('Dec Day1 schedule = ' + value + '\n')

def Decsave2(self):
    value = work.get()
    scr12.insert(tk.INSERT, 'Day2 = ' + value + '\n')
    print('Dec Day2 schedule = ' + value + '\n')

def Decsave3(self):
    value = work.get()
    scr12.insert(tk.INSERT, 'Day3 = ' + value + '\n')
    print('Dec Day3 schedule = ' + value + '\n')

def Decsave4(self):
    value = work.get()
    scr12.insert(tk.INSERT, 'Day4 = ' + value + '\n')
    print('Dec Day4 schedule = ' + value + '\n')

def Decsave5(self):
    value = work.get()
    scr12.insert(tk.INSERT, 'Day5 = ' + value + '\n')
    print('Dec Day5 schedule = ' + value + '\n')

def Decsave6(self):
    value = work.get()
    scr12.insert(tk.INSERT, 'Day6 = ' + value + '\n')
    print('Dec Day6 schedule = ' + value + '\n')

def Decsave7(self):
    value = work.get()
    scr12.insert(tk.INSERT, 'Day7 = ' + value + '\n')
    print('Dec Day7 schedule = ' + value + '\n')

def Decsave8(self):
    value = work.get()
    scr12.insert(tk.INSERT, 'Day8 = ' + value + '\n')
    print('Dec Day8 schedule = ' + value + '\n')

def Decsave9(self):
    value = work.get()
    scr12.insert(tk.INSERT, 'Day9 = ' + value + '\n')
    print('Dec Day9 schedule = ' + value + '\n')

def Decsave10(self):
    value = work.get()
    scr12.insert(tk.INSERT, 'Day10 = ' + value + '\n')
    print('Dec Day10 schedule = ' + value + '\n')

def Decsave11(self):
    value = work.get()
    scr12.insert(tk.INSERT, 'Day11 = ' + value + '\n')
    print('Dec Day11 schedule = ' + value + '\n')

def Decsave12(self):
    value = work.get()
    scr12.insert(tk.INSERT, 'Day12 = ' + value + '\n')
    print('Dec Day12 schedule = ' + value + '\n')

def Decsave13(self):
    value = work.get()
    scr12.insert(tk.INSERT, 'Day13 = ' + value + '\n')
    print('Dec Day13 schedule = ' + value + '\n')

def Decsave14(self):
    value = work.get()
    scr12.insert(tk.INSERT, 'Day14 = ' + value + '\n')
    print('Dec Day1 schedule = ' + value + '\n')

def Decsave15(self):
    value = work.get()
    scr12.insert(tk.INSERT, 'Day15 = ' + value + '\n')
    print('Dec Day15 schedule = ' + value + '\n')

def Decsave16(self):
    value = work.get()
    scr12.insert(tk.INSERT, 'Day16 = ' + value + '\n')
    print('Dec Day16 schedule = ' + value + '\n')

def Decsave17(self):
    value = work.get()
    scr12.insert(tk.INSERT, 'Day17 = ' + value + '\n')
    print('Dec Day17 schedule = ' + value + '\n')

def Decsave18(self):
    value = work.get()
    scr12.insert(tk.INSERT, 'Day18 = ' + value + '\n')
    print('Dec Day18 schedule = ' + value + '\n')

def Decsave19(self):
    value = work.get()
    scr12.insert(tk.INSERT, 'Day19 = ' + value + '\n')
    print('Dec Day19 schedule = ' + value + '\n')

def Decsave20(self):
    value = work.get()
    scr12.insert(tk.INSERT, 'Day20 = ' + value + '\n')
    print('Dec Day20 schedule = ' + value + '\n')

def Decsave21(self):
    value = work.get()
    scr12.insert(tk.INSERT, 'Day21 = ' + value + '\n')
    print('Dec Day21 schedule = ' + value + '\n')

def Decsave22(self):
    value = work.get()
    scr12.insert(tk.INSERT, 'Day22 = ' + value + '\n')
    print('Dec Day22 schedule = ' + value + '\n')

def Decsave23(self):
    value = work.get()
    scr12.insert(tk.INSERT, 'Day23 = ' + value + '\n')
    print('Dec Day23 schedule = ' + value + '\n')

def Decsave24(self):
    value = work.get()
    scr12.insert(tk.INSERT, 'Day24 = ' + value + '\n')
    print('Dec Day24 schedule = ' + value + '\n')

def Decsave25(self):
    value = work.get()
    scr12.insert(tk.INSERT, 'Day25 = ' + value + '\n')
    print('Dec Day25 schedule = ' + value + '\n')

def Decsave26(self):
    value = work.get()
    scr12.insert(tk.INSERT, 'Day26 = ' + value + '\n')
    print('Dec Day26 schedule = ' + value + '\n')

def Decsave27(self):
    value = work.get()
    scr12.insert(tk.INSERT, 'Day27 = ' + value + '\n')
    print('Dec Day27 schedule = ' + value + '\n')

def Decsave28(self):
    value = work.get()
    scr12.insert(tk.INSERT, 'Day28 = ' + value + '\n')
    print('Dec Day28 schedule = ' + value + '\n')

def Decsave29(self):
    value = work.get()
    scr12.insert(tk.INSERT, 'Day29 = ' + value + '\n')
    print('Dec Day29 schedule = ' + value + '\n')

def Decsave30(self):
    value = work.get()
    scr12.insert(tk.INSERT, 'Day30 = ' + value + '\n')
    print('Dec Day30 schedule = ' + value + '\n')

def Decsave31(self):
    value = work.get()
    scr12.insert(tk.INSERT, 'Day31 = ' + value + '\n')
    print('Dec Day31 schedule = ' + value + '\n')

#============================================================


#콜백되면 Entry가 생성되고, 입력시 스크롤텍스트에 출력할 수 있음 (일마다 하나씩 만들어줘야함)
def Decdiary1():
    global work
    global work_entered
    
    Label(Dec, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Dec, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Decsave1)

def Decdiary2():
    global work
    global work_entered
    
    Label(Dec, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Dec, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Decsave2)

def Decdiary3():
    global work
    global work_entered
    
    Label(Dec, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Dec, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Decsave3)

def Decdiary4():
    global work
    global work_entered
    
    Label(Dec, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Dec, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Decsave4)

def Decdiary5():
    global work
    global work_entered
    
    Label(Dec, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Dec, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Decsave5)

def Decdiary6():
    global work
    global work_entered
    
    Label(Dec, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Dec, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Decsave6)

def Decdiary7():
    global work
    global work_entered
    
    Label(Dec, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Dec, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Decsave7)

def Decdiary8():
    global work
    global work_entered
    
    Label(Dec, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Dec, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Decsave8)

def Decdiary9():
    global work
    global work_entered
    
    Label(Dec, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Dec, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Decsave9)

def Decdiary10():
    global work
    global work_entered
    
    Label(Dec, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Dec, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Decsave10)

def Decdiary11():
    global work
    global work_entered
    
    Label(Dec, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Dec, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Decsave11)

def Decdiary12():
    global work
    global work_entered
    
    Label(Dec, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Dec, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Decsave12)

def Decdiary13():
    global work
    global work_entered
    
    Label(Dec, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Dec, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Decsave13)

def Decdiary14():
    global work
    global work_entered
    
    Label(Dec, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Dec, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Decsave14)

def Decdiary15():
    global work
    global work_entered
    
    Label(Dec, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Dec, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Decsave15)

def Decdiary16():
    global work
    global work_entered
    
    Label(Dec, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Dec, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Decsave16)

def Decdiary17():
    global work
    global work_entered
    
    Label(Dec, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Dec, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Decsave17)

def Decdiary18():
    global work
    global work_entered
    
    Label(Dec, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Dec, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Decsave18)

def Decdiary19():
    global work
    global work_entered
    
    Label(Dec, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Dec, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Decsave19)

def Decdiary20():
    global work
    global work_entered
    
    Label(Dec, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Dec, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Decsave20)

def Decdiary21():
    global work
    global work_entered
    
    Label(Dec, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Dec, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Decsave21)

def Decdiary22():
    global work
    global work_entered
    
    Label(Dec, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Dec, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Decsave22)

def Decdiary23():
    global work
    global work_entered
    
    Label(Dec, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Dec, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Decsave23)

def Decdiary24():
    global work
    global work_entered
    
    Label(Dec, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Dec, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Decsave24)

def Decdiary25():
    global work
    global work_entered
    
    Label(Dec, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Dec, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Decsave25)

def Decdiary26():
    global work
    global work_entered
    
    Label(Dec, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Dec, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Decsave26)

def Decdiary27():
    global work
    global work_entered
    
    Label(Dec, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Dec, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Decsave27)

def Decdiary28():
    global work
    global work_entered
    
    Label(Dec, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Dec, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Decsave28)

def Decdiary29():
    global work
    global work_entered
    
    Label(Dec, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Dec, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Decsave29)

def Decdiary30():
    global work
    global work_entered
    
    Label(Dec, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Dec, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Decsav30)

def Decdiary31():
    global work
    global work_entered
    
    Label(Dec, text="일정").grid(column=8, row=0,rowspan=6)
    work = tk.StringVar()
    work_entered=Entry(Dec, width=15, textvariable=work)
    work_entered.grid(column=8, row=2,rowspan=6)
    work_entered.bind("<Return>",Decsav31)

#==============================================================================================
      

#12월 일정을 저장 할 scrolledtext 만듦 (1월부터 12월까지 다 해줘야함)===============================
scrol_w=30
scrol_h=12
scr12=scrolledtext.ScrolledText(Dec, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr12.grid(column=10, row=1,columnspan=6, rowspan=6)
#==============================================================================================
    

#1일 부터 월의 최대 일까지의 버튼을 만든다. 19년도 달력을 보고 요일과 일이 매치되도록 함 일일이...
    
#12월 달력판====================================================================================
day1 = Button(Dec, text=" 1 ",command = Decdiary1)
day1.grid(column=1, row=1)
day2 = Button(Dec, text=" 2 ",command = Decdiary2)
day2.grid(column=2, row=1)
day3 = Button(Dec, text=" 3 ",command = Decdiary3)
day3.grid(column=3, row=1)
day4 = Button(Dec, text=" 4 ",command = Decdiary4)
day4.grid(column=4, row=1)
day5 = Button(Dec, text=" 5 ",command = Decdiary5)
day5.grid(column=5, row=1)
day6 = Button(Dec, text=" 6 ",command = Decdiary6)
day6.grid(column=6, row=1)
day7 = Button(Dec, text=" 7 ",command = Decdiary7)
day7.grid(column=7, row=1)
day8 = Button(Dec, text=" 8 ",command = Decdiary8)
day8.grid(column=1, row=2)
day9 = Button(Dec, text=" 9 ",command = Decdiary9)
day9.grid(column=2, row=2)
day10 = Button(Dec, text="10",command = Decdiary10)
day10.grid(column=3, row=2)
day11 = Button(Dec, text="11",command = Decdiary11)
day11.grid(column=4, row=2)
day12 = Button(Dec, text="12",command = Decdiary12)
day12.grid(column=5, row=2)
day13 = Button(Dec, text="13",command = Decdiary13)
day13.grid(column=6, row=2)
day14 = Button(Dec, text="14",command = Decdiary14)
day14.grid(column=7, row=2)
day15 = Button(Dec, text="15",command = Decdiary15)
day15.grid(column=1, row=3)
day16 = Button(Dec, text="16",command = Decdiary16)
day16.grid(column=2, row=3)
day17 = Button(Dec, text="17",command = Decdiary17)
day17.grid(column=3, row=3)
day18 = Button(Dec, text="18",command = Decdiary18)
day18.grid(column=4, row=3)
day19 = Button(Dec, text="19",command = Decdiary19)
day19.grid(column=5, row=3)
day20 = Button(Dec, text="20",command = Decdiary20)
day20.grid(column=6, row=3)
day21 = Button(Dec, text="21",command = Decdiary21)
day21.grid(column=7, row=3)
day22 = Button(Dec, text="22",command = Decdiary22)
day22.grid(column=1, row=4)
day23 = Button(Dec, text="23",command = Decdiary23)
day23.grid(column=2, row=4)
day24 = Button(Dec, text="24",command = Decdiary24)
day24.grid(column=3, row=4)
day25 = Button(Dec, text="25",command = Decdiary25)
day25.grid(column=4, row=4)
day26 = Button(Dec, text="26",command = Decdiary26)
day26.grid(column=5, row=4)
day27 = Button(Dec, text="27",command = Decdiary27)
day27.grid(column=6, row=4)
day28 = Button(Dec, text="28",command = Decdiary28)
day28.grid(column=7, row=4)
day29 = Button(Dec, text="29",command = Decdiary29)
day29.grid(column=1, row=5)
day30 = Button(Dec, text="30",command = Decdiary30)
day30.grid(column=2, row=5)
day31 = Button(Dec, text="31",command = Decdiary31)
day31.grid(column=3, row=5)
#===============================================================================================
##########################################################12월 끝#####################################################


#시계 함수=======================================================================
C_width,C_height = 200,200

def Draw():
    Clock.delete("all")
    for i in range(60):
        angle = -6*i*math.pi/180
        if i%5 == 0:
            needle = 60
        else:
            needle = 70
        Clock.create_line(needle*math.cos(angle)+100,needle*math.sin(angle)+100,80*math.cos(angle)+100,80*math.sin(angle)+100,fill="black")

    time = datetime.datetime.now()
    hour = time.hour
    minu = time.minute
    sec = time.second
    angle_h = -math.pi*0.5 + 30*(hour%12)*math.pi/180+0.5*minu*math.pi/180
    angle_m = -math.pi*0.5 + 6*minu*math.pi/180+6*sec*math.pi/180/60
    angle_s = -math.pi*0.5 + 6*sec*math.pi/180
    
    Clock.create_line(100,100,50*math.cos(angle_h)+100,50*math.sin(angle_h)+100,width = 3)
    Clock.create_line(100,100,65*math.cos(angle_m)+100,65*math.sin(angle_m)+100,width = 2)
    Clock.create_line(100,100,65*math.cos(angle_s)+100,65*math.sin(angle_s)+100)
    Clock.after(1000,Draw)
    #print(time)
    
Clock = tk.Canvas(a,width = C_width,height = C_height)
Clock.pack()
Draw()
#===================================================================================
a.mainloop()
