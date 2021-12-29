from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
import numpy as np
import os
import NRSEFunction


class App(tk.Frame):
    fun = NRSEFunction.NRSEFunction()

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.menubar = tk.Menu(self)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)

        self.menubar.add_cascade(label="文件", menu=self.filemenu)
        self.menubar.add_command(label="帮助", command=self.editorhelp)
        self.menubar.add_command(label="关于", command=self.editorabout)
        self.menubar.add_command(label="退出", command=self.editorquit)

        self.filemenu.add_command(label="新建", command=self.filenew)
        self.filemenu.add_command(label="打开", command=self.fileopen)
        self.filemenu.add_command(label="保存", command=self.filesave)
        self.filemenu.add_command(label="另存", command=self.filesaveas)
        self.filemenu.add_command(label="关闭", command=self.fileclose)

        self.master.config(menu=self.menubar)

        #------------------------------------------------------------
        self.label1 = tk.Label(self.master, font=('Times', 20), fg='#5fb878')
        self.label1["text"] = "Naiwei Robot SysParam Editor"
        self.label1.place(x=200, y=10, width=600, height=50)
        # self.label1["anchor"] = "center"
        # self.label1["justify"] = "center"
        # self.label1["relief"] = "flat"

        #------------------------------------------------------------
        self.text101 = tk.StringVar()
        self.text102 = tk.StringVar()
        self.text103 = tk.StringVar()
        self.text104 = tk.StringVar()
        self.text105 = tk.StringVar()
        self.text106 = tk.StringVar()
        self.text107 = tk.StringVar()
        self.text108 = tk.StringVar()
        self.text109 = tk.StringVar()
        self.text110 = tk.StringVar()
        self.text111 = tk.StringVar()
        self.text112 = tk.StringVar()
        self.text113 = tk.StringVar()
        self.text114 = tk.StringVar()
        self.text115 = tk.StringVar()
        self.text116 = tk.StringVar()
        self.text117 = tk.StringVar()
        self.text201 = tk.StringVar()
        self.text202 = tk.StringVar()
        self.text203 = tk.StringVar()
        self.text204 = tk.StringVar()
        self.text205 = tk.StringVar()
        self.text206 = tk.StringVar()
        self.text207 = tk.StringVar()
        self.text208 = tk.StringVar()
        self.text209 = tk.StringVar()
        self.text210 = tk.StringVar()
        self.text211 = tk.StringVar()
        self.text212 = tk.StringVar()
        self.text213 = tk.StringVar()
        self.text214 = tk.StringVar()
        self.text215 = tk.StringVar()

        #------------------------------------------------------------

        self.label101 = tk.Label(self.master,
                                 font=('Times', 14),
                                 fg='#5fb878',
                                 text='机型选择')
        self.label102 = tk.Label(self.master,
                                 font=('Times', 14),
                                 fg='#5fb878',
                                 text='手动加速度倍数')
        self.label103 = tk.Label(self.master,
                                 font=('Times', 14),
                                 fg='#5fb878',
                                 text='手动减速度倍数')
        self.label104 = tk.Label(self.master,
                                 font=('Times', 14),
                                 fg='#5fb878',
                                 text='手动加加速度倍数')
        self.label105 = tk.Label(self.master,
                                 font=('Times', 14),
                                 fg='#5fb878',
                                 text='手动单步运行速度')
        self.label106 = tk.Label(self.master,
                                 font=('Times', 14),
                                 fg='#5fb878',
                                 text='自动关节加速度倍数')
        self.label107 = tk.Label(self.master,
                                 font=('Times', 14),
                                 fg='#5fb878',
                                 text='自动关节减速度倍数')
        self.label108 = tk.Label(self.master,
                                 font=('Times', 14),
                                 fg='#5fb878',
                                 text='自动关节加加速度倍数')
        self.label109 = tk.Label(self.master,
                                 font=('Times', 14),
                                 fg='#5fb878',
                                 text='自动空间位置插补速度')
        self.label110 = tk.Label(self.master,
                                 font=('Times', 14),
                                 fg='#5fb878',
                                 text='自动空间姿态插补速度')
        self.label111 = tk.Label(self.master,
                                 font=('Times', 14),
                                 fg='#5fb878',
                                 text='自动空间加速度倍数')
        self.label112 = tk.Label(self.master,
                                 font=('Times', 14),
                                 fg='#5fb878',
                                 text='自动空间减速度倍数')
        self.label113 = tk.Label(self.master,
                                 font=('Times', 14),
                                 fg='#5fb878',
                                 text='自动空间加加速度倍数')
        self.label114 = tk.Label(self.master,
                                 font=('Times', 14),
                                 fg='#5fb878',
                                 text='程序首循环速度倍率')
        self.label115 = tk.Label(self.master,
                                 font=('Times', 14),
                                 fg='#5fb878',
                                 text='急停选择')
        self.label116 = tk.Label(self.master,
                                 font=('Times', 14),
                                 fg='#5fb878',
                                 text='工艺选择')
        self.label117 = tk.Label(self.master,
                                 font=('Times', 14),
                                 fg='#5fb878',
                                 text='使能开关选择')
        self.label201 = tk.Label(self.master,
                                 font=('Times', 14),
                                 fg='#5fb878',
                                 text='连杆转角')
        self.label202 = tk.Label(self.master,
                                 font=('Times', 14),
                                 fg='#5fb878',
                                 text='连杆长度')
        self.label203 = tk.Label(self.master,
                                 font=('Times', 14),
                                 fg='#5fb878',
                                 text='连杆偏距')
        self.label204 = tk.Label(self.master,
                                 font=('Times', 14),
                                 fg='#5fb878',
                                 text='关节正限位')
        self.label205 = tk.Label(self.master,
                                 font=('Times', 14),
                                 fg='#5fb878',
                                 text='关节负限位')
        self.label206 = tk.Label(self.master,
                                 font=('Times', 14),
                                 fg='#5fb878',
                                 text='空间正限位')
        self.label207 = tk.Label(self.master,
                                 font=('Times', 14),
                                 fg='#5fb878',
                                 text='空间负限位')
        self.label208 = tk.Label(self.master,
                                 font=('Times', 14),
                                 fg='#5fb878',
                                 text='减速比')
        self.label209 = tk.Label(self.master,
                                 font=('Times', 14),
                                 fg='#5fb878',
                                 text='导程')
        self.label210 = tk.Label(self.master,
                                 font=('Times', 14),
                                 fg='#5fb878',
                                 text='编码器分辨率')
        self.label211 = tk.Label(self.master,
                                 font=('Times', 14),
                                 fg='#5fb878',
                                 text='电机额定力矩')
        self.label212 = tk.Label(self.master,
                                 font=('Times', 14),
                                 fg='#5fb878',
                                 text='电机最大转速')
        self.label213 = tk.Label(self.master,
                                 font=('Times', 14),
                                 fg='#5fb878',
                                 text='手动关节最大速度')
        self.label214 = tk.Label(self.master,
                                 font=('Times', 14),
                                 fg='#5fb878',
                                 text='手动空间最大速度')
        self.label215 = tk.Label(self.master,
                                 font=('Times', 14),
                                 fg='#5fb878',
                                 text='自动附加轴插补速度')

        # self.label101["anchor"] = "center"
        # self.label101["justify"] = "center"
        # self.label101["relief"] = "flat"

        xpix = 5
        ypix = 90
        self.label101.place(x=xpix, y=ypix, width=190, height=30)
        ypix += 34
        self.label102.place(x=xpix, y=ypix, width=190, height=30)
        ypix += 34
        self.label103.place(x=xpix, y=ypix, width=190, height=30)
        ypix += 34
        self.label104.place(x=xpix, y=ypix, width=190, height=30)
        ypix += 34
        self.label105.place(x=xpix, y=ypix, width=190, height=30)
        ypix += 34
        self.label106.place(x=xpix, y=ypix, width=190, height=30)
        ypix += 34
        self.label107.place(x=xpix, y=ypix, width=190, height=30)
        ypix += 34
        self.label108.place(x=xpix, y=ypix, width=190, height=30)
        ypix += 34
        self.label109.place(x=xpix, y=ypix, width=190, height=30)
        ypix += 34
        self.label110.place(x=xpix, y=ypix, width=190, height=30)
        ypix += 34
        self.label111.place(x=xpix, y=ypix, width=190, height=30)
        ypix += 34
        self.label112.place(x=xpix, y=ypix, width=190, height=30)
        ypix += 34
        self.label113.place(x=xpix, y=ypix, width=190, height=30)
        ypix += 34
        self.label114.place(x=xpix, y=ypix, width=190, height=30)
        ypix += 34
        self.label115.place(x=xpix, y=ypix, width=190, height=30)
        ypix += 34
        self.label116.place(x=xpix, y=ypix, width=190, height=30)
        ypix += 34
        self.label117.place(x=xpix, y=ypix, width=190, height=30)
        xpix = 290
        ypix = 90
        self.label201.place(x=xpix, y=ypix, width=190, height=30)
        ypix += 34
        self.label202.place(x=xpix, y=ypix, width=190, height=30)
        ypix += 34
        self.label203.place(x=xpix, y=ypix, width=190, height=30)
        ypix += 34
        self.label204.place(x=xpix, y=ypix, width=190, height=30)
        ypix += 34
        self.label205.place(x=xpix, y=ypix, width=190, height=30)
        ypix += 34
        self.label206.place(x=xpix, y=ypix, width=190, height=30)
        ypix += 34
        self.label207.place(x=xpix, y=ypix, width=190, height=30)
        ypix += 34
        self.label208.place(x=xpix, y=ypix, width=190, height=30)
        ypix += 34
        self.label209.place(x=xpix, y=ypix, width=190, height=30)
        ypix += 34
        self.label210.place(x=xpix, y=ypix, width=190, height=30)
        ypix += 34
        self.label211.place(x=xpix, y=ypix, width=190, height=30)
        ypix += 34
        self.label212.place(x=xpix, y=ypix, width=190, height=30)
        ypix += 34
        self.label213.place(x=xpix, y=ypix, width=190, height=30)
        ypix += 34
        self.label214.place(x=xpix, y=ypix, width=190, height=30)
        ypix += 34
        self.label215.place(x=xpix, y=ypix, width=190, height=30)

        #------------------------------------------------------------
        self.entry101 = tk.Entry(self.master,
                                 font=('Times', 14),
                                 fg='#cc0000',
                                 justify='center',
                                 textvariable=self.text101)
        self.entry102 = tk.Entry(self.master,
                                 font=('Times', 14),
                                 fg='#cc0000',
                                 justify='center',
                                 textvariable=self.text102)
        self.entry103 = tk.Entry(self.master,
                                 font=('Times', 14),
                                 fg='#cc0000',
                                 justify='center',
                                 textvariable=self.text103)
        self.entry104 = tk.Entry(self.master,
                                 font=('Times', 14),
                                 fg='#cc0000',
                                 justify='center',
                                 textvariable=self.text104)
        self.entry105 = tk.Entry(self.master,
                                 font=('Times', 14),
                                 fg='#cc0000',
                                 justify='center',
                                 textvariable=self.text105)
        self.entry106 = tk.Entry(self.master,
                                 font=('Times', 14),
                                 fg='#cc0000',
                                 justify='center',
                                 textvariable=self.text106)
        self.entry107 = tk.Entry(self.master,
                                 font=('Times', 14),
                                 fg='#cc0000',
                                 justify='center',
                                 textvariable=self.text107)
        self.entry108 = tk.Entry(self.master,
                                 font=('Times', 14),
                                 fg='#cc0000',
                                 justify='center',
                                 textvariable=self.text108)
        self.entry109 = tk.Entry(self.master,
                                 font=('Times', 14),
                                 fg='#cc0000',
                                 justify='center',
                                 textvariable=self.text109)
        self.entry110 = tk.Entry(self.master,
                                 font=('Times', 14),
                                 fg='#cc0000',
                                 justify='center',
                                 textvariable=self.text110)
        self.entry111 = tk.Entry(self.master,
                                 font=('Times', 14),
                                 fg='#cc0000',
                                 justify='center',
                                 textvariable=self.text111)
        self.entry112 = tk.Entry(self.master,
                                 font=('Times', 14),
                                 fg='#cc0000',
                                 justify='center',
                                 textvariable=self.text112)
        self.entry113 = tk.Entry(self.master,
                                 font=('Times', 14),
                                 fg='#cc0000',
                                 justify='center',
                                 textvariable=self.text113)
        self.entry114 = tk.Entry(self.master,
                                 font=('Times', 14),
                                 fg='#cc0000',
                                 justify='center',
                                 textvariable=self.text114)
        self.entry115 = tk.Entry(self.master,
                                 font=('Times', 14),
                                 fg='#cc0000',
                                 justify='center',
                                 textvariable=self.text115)
        self.entry116 = tk.Entry(self.master,
                                 font=('Times', 14),
                                 fg='#cc0000',
                                 justify='center',
                                 textvariable=self.text116)
        self.entry117 = tk.Entry(self.master,
                                 font=('Times', 14),
                                 fg='#cc0000',
                                 justify='center',
                                 textvariable=self.text117)
        self.entry201 = tk.Entry(self.master,
                                 font=('Times', 14),
                                 fg='#cc0000',
                                 justify='center',
                                 textvariable=self.text201)
        self.entry202 = tk.Entry(self.master,
                                 font=('Times', 14),
                                 fg='#cc0000',
                                 justify='center',
                                 textvariable=self.text202)
        self.entry203 = tk.Entry(self.master,
                                 font=('Times', 14),
                                 fg='#cc0000',
                                 justify='center',
                                 textvariable=self.text203)
        self.entry204 = tk.Entry(self.master,
                                 font=('Times', 14),
                                 fg='#cc0000',
                                 justify='center',
                                 textvariable=self.text204)
        self.entry205 = tk.Entry(self.master,
                                 font=('Times', 14),
                                 fg='#cc0000',
                                 justify='center',
                                 textvariable=self.text205)
        self.entry206 = tk.Entry(self.master,
                                 font=('Times', 14),
                                 fg='#cc0000',
                                 justify='center',
                                 textvariable=self.text206)
        self.entry207 = tk.Entry(self.master,
                                 font=('Times', 14),
                                 fg='#cc0000',
                                 justify='center',
                                 textvariable=self.text207)
        self.entry208 = tk.Entry(self.master,
                                 font=('Times', 14),
                                 fg='#cc0000',
                                 justify='center',
                                 textvariable=self.text208)
        self.entry209 = tk.Entry(self.master,
                                 font=('Times', 14),
                                 fg='#cc0000',
                                 justify='center',
                                 textvariable=self.text209)
        self.entry210 = tk.Entry(self.master,
                                 font=('Times', 14),
                                 fg='#cc0000',
                                 justify='center',
                                 textvariable=self.text210)
        self.entry211 = tk.Entry(self.master,
                                 font=('Times', 14),
                                 fg='#cc0000',
                                 justify='center',
                                 textvariable=self.text211)
        self.entry212 = tk.Entry(self.master,
                                 font=('Times', 14),
                                 fg='#cc0000',
                                 justify='center',
                                 textvariable=self.text212)
        self.entry213 = tk.Entry(self.master,
                                 font=('Times', 14),
                                 fg='#cc0000',
                                 justify='center',
                                 textvariable=self.text213)
        self.entry214 = tk.Entry(self.master,
                                 font=('Times', 14),
                                 fg='#cc0000',
                                 justify='center',
                                 textvariable=self.text214)
        self.entry215 = tk.Entry(self.master,
                                 font=('Times', 14),
                                 fg='#cc0000',
                                 justify='center',
                                 textvariable=self.text215)

        # self.entry101["borderwidth"] = "1px"
        # self.entry101["relief"] = "groove"

        xpix = 200
        ypix = 90
        self.entry101.place(x=xpix, y=ypix, width=80, height=30)
        ypix += 34
        self.entry102.place(x=xpix, y=ypix, width=80, height=30)
        ypix += 34
        self.entry103.place(x=xpix, y=ypix, width=80, height=30)
        ypix += 34
        self.entry104.place(x=xpix, y=ypix, width=80, height=30)
        ypix += 34
        self.entry105.place(x=xpix, y=ypix, width=80, height=30)
        ypix += 34
        self.entry106.place(x=xpix, y=ypix, width=80, height=30)
        ypix += 34
        self.entry107.place(x=xpix, y=ypix, width=80, height=30)
        ypix += 34
        self.entry108.place(x=xpix, y=ypix, width=80, height=30)
        ypix += 34
        self.entry109.place(x=xpix, y=ypix, width=80, height=30)
        ypix += 34
        self.entry110.place(x=xpix, y=ypix, width=80, height=30)
        ypix += 34
        self.entry111.place(x=xpix, y=ypix, width=80, height=30)
        ypix += 34
        self.entry112.place(x=xpix, y=ypix, width=80, height=30)
        ypix += 34
        self.entry113.place(x=xpix, y=ypix, width=80, height=30)
        ypix += 34
        self.entry114.place(x=xpix, y=ypix, width=80, height=30)
        ypix += 34
        self.entry115.place(x=xpix, y=ypix, width=80, height=30)
        ypix += 34
        self.entry116.place(x=xpix, y=ypix, width=80, height=30)
        ypix += 34
        self.entry117.place(x=xpix, y=ypix, width=80, height=30)
        xpix = 485
        ypix = 90
        self.entry201.place(x=xpix, y=ypix, width=500, height=30)
        ypix += 34
        self.entry202.place(x=xpix, y=ypix, width=500, height=30)
        ypix += 34
        self.entry203.place(x=xpix, y=ypix, width=500, height=30)
        ypix += 34
        self.entry204.place(x=xpix, y=ypix, width=500, height=30)
        ypix += 34
        self.entry205.place(x=xpix, y=ypix, width=500, height=30)
        ypix += 34
        self.entry206.place(x=xpix, y=ypix, width=500, height=30)
        ypix += 34
        self.entry207.place(x=xpix, y=ypix, width=500, height=30)
        ypix += 34
        self.entry208.place(x=xpix, y=ypix, width=500, height=30)
        ypix += 34
        self.entry209.place(x=xpix, y=ypix, width=500, height=30)
        ypix += 34
        self.entry210.place(x=xpix, y=ypix, width=500, height=30)
        ypix += 34
        self.entry211.place(x=xpix, y=ypix, width=500, height=30)
        ypix += 34
        self.entry212.place(x=xpix, y=ypix, width=500, height=30)
        ypix += 34
        self.entry213.place(x=xpix, y=ypix, width=500, height=30)
        ypix += 34
        self.entry214.place(x=xpix, y=ypix, width=500, height=30)
        ypix += 34
        self.entry215.place(x=xpix, y=ypix, width=500, height=30)

        #------------------------------------------------------------
        ypix = ypix + 50
        self.labellog = tk.Label(self.master, font=('Times', 14), fg='#5fb878')
        self.labellog["text"] = 'waiting for you ...'
        self.labellog.place(x=xpix, y=ypix, width=400, height=30)
        # self.labellog["anchor"] = "center"
        # self.labellog["justify"] = "center"
        # self.labellog["relief"] = "flat"
        return

    def dataset(self):
        self.text101.set('; '.join(
            map(lambda x: str(x), self.fun.data.robottype)))
        self.text102.set('; '.join(map(lambda x: str(x),
                                       self.fun.data.jogacc)))
        self.text103.set('; '.join(map(lambda x: str(x),
                                       self.fun.data.jogdec)))
        self.text104.set('; '.join(map(lambda x: str(x),
                                       self.fun.data.jogjerk)))
        self.text105.set('; '.join(
            map(lambda x: str(x), self.fun.data.jogstepvel)))
        self.text106.set('; '.join(
            map(lambda x: str(x), self.fun.data.ataxisacc)))
        self.text107.set('; '.join(
            map(lambda x: str(x), self.fun.data.ataxisdec)))
        self.text108.set('; '.join(
            map(lambda x: str(x), self.fun.data.ataxisjerk)))
        self.text109.set('; '.join(
            map(lambda x: str(x), self.fun.data.atlinemaxvel)))
        self.text110.set('; '.join(
            map(lambda x: str(x), self.fun.data.atposemaxvel)))
        self.text111.set('; '.join(
            map(lambda x: str(x), self.fun.data.atcoordacc)))
        self.text112.set('; '.join(
            map(lambda x: str(x), self.fun.data.atcoorddec)))
        self.text113.set('; '.join(
            map(lambda x: str(x), self.fun.data.atcoordjerk)))
        self.text114.set('; '.join(
            map(lambda x: str(x), self.fun.data.fisrtcycvel)))
        self.text115.set('; '.join(
            map(lambda x: str(x), self.fun.data.emergencysel)))
        self.text116.set('; '.join(
            map(lambda x: str(x), self.fun.data.craftsel)))
        self.text117.set('; '.join(
            map(lambda x: str(x), self.fun.data.enablesel)))
        self.text201.set('; '.join(map(lambda x: str(x), self.fun.data.alpha)))
        self.text202.set('; '.join(map(lambda x: str(x), self.fun.data.a)))
        self.text203.set('; '.join(map(lambda x: str(x), self.fun.data.d)))
        self.text204.set('; '.join(
            map(lambda x: str(x), self.fun.data.axisposlimit)))
        self.text205.set('; '.join(
            map(lambda x: str(x), self.fun.data.axisneglimit)))
        self.text206.set('; '.join(
            map(lambda x: str(x), self.fun.data.coordposlimit)))
        self.text207.set('; '.join(
            map(lambda x: str(x), self.fun.data.coordneglimit)))
        self.text208.set('; '.join(
            map(lambda x: str(x), self.fun.data.reductionratio)))
        self.text209.set('; '.join(
            map(lambda x: str(x), self.fun.data.axislead)))
        self.text210.set('; '.join(
            map(lambda x: str(x), self.fun.data.pulsepercir)))
        self.text211.set('; '.join(
            map(lambda x: str(x), self.fun.data.motortorque)))
        self.text212.set('; '.join(
            map(lambda x: str(x), self.fun.data.motormaxvel)))
        self.text213.set('; '.join(
            map(lambda x: str(x), self.fun.data.jogaxismaxvel)))
        self.text214.set('; '.join(
            map(lambda x: str(x), self.fun.data.jogcordmaxvel)))
        self.text215.set('; '.join(
            map(lambda x: str(x), self.fun.data.atextmaxvel)))
        return

    def dataget(self):
        self.fun.data.robottype = np.uint(self.text101.get())
        self.fun.data.jogacc = np.uint(self.text102.get())
        self.fun.data.jogdec = np.uint(self.text103.get())
        self.fun.data.jogjerk = np.uint(self.text104.get())
        self.fun.data.jogstepvel = np.uint(self.text105.get())
        self.fun.data.ataxisacc = np.uint(self.text106.get())
        self.fun.data.ataxisdec = np.uint(self.text107.get())
        self.fun.data.ataxisjerk = np.uint(self.text108.get())
        self.fun.data.atlinemaxvel = np.float32(self.text109.get())
        self.fun.data.atposemaxvel = np.float32(self.text110.get())
        self.fun.data.atcoordacc = np.uint(self.text111.get())
        self.fun.data.atcoorddec = np.uint(self.text112.get())
        self.fun.data.atcoordjerk = np.uint(self.text113.get())
        self.fun.data.fisrtcycvel = np.int32(self.text114.get())
        self.fun.data.emergencysel = np.int32(self.text115.get())
        self.fun.data.craftsel = np.int32(self.text116.get())
        self.fun.data.enablesel = np.int32(self.text117.get())
        self.fun.data.alpha = np.array(self.text201.get().split('; ')).astype(
            np.float64)
        self.fun.data.a = np.array(self.text202.get().split('; ')).astype(
            np.float64)
        self.fun.data.d = np.array(self.text203.get().split('; ')).astype(
            np.float64)
        self.fun.data.axisposlimit = np.array(
            self.text204.get().split('; ')).astype(np.float32)
        self.fun.data.axisneglimit = np.array(
            self.text205.get().split('; ')).astype(np.float32)
        self.fun.data.coordposlimit = np.array(
            self.text206.get().split('; ')).astype(np.float32)
        self.fun.data.coordneglimit = np.array(
            self.text207.get().split('; ')).astype(np.float32)
        self.fun.data.reductionratio = np.array(
            self.text208.get().split('; ')).astype(np.float32)
        self.fun.data.axislead = np.array(
            self.text209.get().split('; ')).astype(np.float32)
        self.fun.data.pulsepercir = np.array(
            self.text210.get().split('; ')).astype(np.float64)
        self.fun.data.motortorque = np.array(
            self.text211.get().split('; ')).astype(np.float64)
        self.fun.data.motormaxvel = np.array(
            self.text212.get().split('; ')).astype(np.float32)
        self.fun.data.jogaxismaxvel = np.array(
            self.text213.get().split('; ')).astype(np.float32)
        self.fun.data.jogcordmaxvel = np.array(
            self.text214.get().split('; ')).astype(np.float32)
        self.fun.data.atextmaxvel = np.array(
            self.text215.get().split('; ')).astype(np.float32)
        return

    def dataclr(self):
        self.text101.set('')
        self.text102.set('')
        self.text103.set('')
        self.text104.set('')
        self.text105.set('')
        self.text106.set('')
        self.text107.set('')
        self.text108.set('')
        self.text109.set('')
        self.text110.set('')
        self.text111.set('')
        self.text112.set('')
        self.text113.set('')
        self.text114.set('')
        self.text115.set('')
        self.text116.set('')
        self.text117.set('')
        self.text201.set('')
        self.text202.set('')
        self.text203.set('')
        self.text204.set('')
        self.text205.set('')
        self.text206.set('')
        self.text207.set('')
        self.text208.set('')
        self.text209.set('')
        self.text210.set('')
        self.text211.set('')
        self.text212.set('')
        self.text213.set('')
        self.text214.set('')
        self.text215.set('')
        return

    def filenew(self):
        self.dataclr()
        self.fun.file=os.path.join(os.path.expanduser('~'),"Desktop").replace('\\','/')
        self.labellog["text"] = 'start a better one'
        return

    def fileopen(self):
        file = filedialog.askopenfilename(title='选择文件')

        try:
            flag = self.fun.read(file)
        except:
            self.labellog["text"] = 'sorry, something wrong'
        else:
            if flag == False:
                self.labellog["text"] = 'oops, open fail'
            else:
                self.labellog["text"] = 'aha, open success'
                self.dataset()
        finally:
            return

    def filesave(self):
        try:
            self.dataget()
        except:
            self.labellog["text"] = 'sorry, something wrong'
            return

        try:
            flag = self.fun.write()
        except:
            self.labellog["text"] = 'sorry, something wrong'
        else:
            if flag == False:
                self.labellog["text"] = 'oops, save fail'
            else:
                self.labellog["text"] = 'aha, save success'
        finally:
            return

    def filesaveas(self):
        file = filedialog.asksaveasfilename(title='选择文件',
                                            filetypes=[('text', '*.txt')])
        if file == '':
            return
        if file[-4] !='.txt':
            file+='.txt'
        
        try:
            self.dataget()
        except:
            self.labellog["text"] = 'sorry, something wrong'
            return

        try:
            flag = self.fun.write(file)
        except:
            self.fileclose()
            self.labellog["text"] = 'sorry, something wrong'
        else:
            if flag == False:
                self.labellog["text"] = 'oops, save fail'
            else:
                self.labellog["text"] = 'aha, save success'
        finally:
            return

    def fileclose(self):
        self.fun.close()
        return

    def editorquit(self):
        self.quit()
        return

    def editorhelp(self):
        info = '测试'
        messagebox.showinfo(title='帮助', message=info)
        return

    def editorabout(self):
        info='简称：NRSE\r\n' \
            '全称：Naiwei Robot Sysparam Editor\r\n' \
            '功能：实现对耐为控制器系统参数文件的编辑 \r\n' \
            '语言：Python 3.9.6 \r\n' \
            '版本：0.1 \r\n' \
            '日期：2021-12-29 \r\n' \
            '\r\n' \
            '作者：王同辉\r\n' \
            '邮箱：tonghuiwang0610@gmail.com'

        messagebox.showinfo(title='关于', message=info)
        return

if __name__ == "__main__":
    root = tk.Tk()
    root.title("NRSE V0.1")
    width = 1000
    height = 700
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2,
                                (screenheight - height) / 2)
    root.geometry(alignstr)
    root.resizable(width=False, height=False)

    app = App(master=root)
    root.mainloop()
