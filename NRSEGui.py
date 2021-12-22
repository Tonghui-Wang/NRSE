import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
from NRSEFunction import read


class App(tk.Frame):
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
        self.label1 = tk.Label(self.master)
        self.label1["anchor"] = "center"
        ft = tkFont.Font(family='Times', size=20, weight=tkFont.BOLD)
        self.label1["font"] = ft
        self.label1["fg"] = "#5fb878"
        self.label1["justify"] = "center"
        self.label1["text"] = "Naiwei Robot SysParam Editor"
        self.label1["relief"] = "flat"
        self.label1.place(x=200, y=10, width=600, height=50)

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
        xpix = 5
        ypix = 90

        self.label101 = tk.Label(self.master)
        self.label101["anchor"] = "center"
        ft = tkFont.Font(family='Times', size=14)
        self.label101["font"] = ft
        self.label101["fg"] = "#5fb878"
        self.label101["justify"] = "center"
        self.label101["text"] = "机型选择"
        self.label101["relief"] = "flat"
        self.label101.place(x=xpix, y=ypix, width=190, height=30)
        ypix = ypix + 34

        self.label102 = tk.Label(self.master)
        self.label102["anchor"] = "center"
        ft = tkFont.Font(family='Times', size=14)
        self.label102["font"] = ft
        self.label102["fg"] = "#5fb878"
        self.label102["justify"] = "center"
        self.label102["text"] = "手动加速度倍数"
        self.label102["relief"] = "flat"
        self.label102.place(x=xpix, y=ypix, width=190, height=30)
        ypix = ypix + 34

        self.label103 = tk.Label(self.master)
        self.label103["anchor"] = "center"
        ft = tkFont.Font(family='Times', size=14)
        self.label103["font"] = ft
        self.label103["fg"] = "#5fb878"
        self.label103["justify"] = "center"
        self.label103["text"] = "手动减速度倍数"
        self.label103["relief"] = "flat"
        self.label103.place(x=xpix, y=ypix, width=190, height=30)
        ypix = ypix + 34

        self.label104 = tk.Label(self.master)
        self.label104["anchor"] = "center"
        ft = tkFont.Font(family='Times', size=14)
        self.label104["font"] = ft
        self.label104["fg"] = "#5fb878"
        self.label104["justify"] = "center"
        self.label104["text"] = "手动加加速度倍数"
        self.label104["relief"] = "flat"
        self.label104.place(x=xpix, y=ypix, width=190, height=30)
        ypix = ypix + 34

        self.label105 = tk.Label(self.master)
        self.label105["anchor"] = "center"
        ft = tkFont.Font(family='Times', size=14)
        self.label105["font"] = ft
        self.label105["fg"] = "#5fb878"
        self.label105["justify"] = "center"
        self.label105["text"] = "手动单步运行速度"
        self.label105["relief"] = "flat"
        self.label105.place(x=xpix, y=ypix, width=190, height=30)
        ypix = ypix + 34

        self.label106 = tk.Label(self.master)
        self.label106["anchor"] = "center"
        ft = tkFont.Font(family='Times', size=14)
        self.label106["font"] = ft
        self.label106["fg"] = "#5fb878"
        self.label106["justify"] = "center"
        self.label106["text"] = "自动关节加速度倍数"
        self.label106["relief"] = "flat"
        self.label106.place(x=xpix, y=ypix, width=190, height=30)
        ypix = ypix + 34

        self.label107 = tk.Label(self.master)
        self.label107["anchor"] = "center"
        ft = tkFont.Font(family='Times', size=14)
        self.label107["font"] = ft
        self.label107["fg"] = "#5fb878"
        self.label107["justify"] = "center"
        self.label107["text"] = "自动关节减速度倍数"
        self.label107["relief"] = "flat"
        self.label107.place(x=xpix, y=ypix, width=190, height=30)
        ypix = ypix + 34

        self.label108 = tk.Label(self.master)
        self.label108["anchor"] = "center"
        ft = tkFont.Font(family='Times', size=14)
        self.label108["font"] = ft
        self.label108["fg"] = "#5fb878"
        self.label108["justify"] = "center"
        self.label108["text"] = "自动关节加加速度倍数"
        self.label108["relief"] = "flat"
        self.label108.place(x=xpix, y=ypix, width=190, height=30)
        ypix = ypix + 34

        self.label109 = tk.Label(self.master)
        self.label109["anchor"] = "center"
        ft = tkFont.Font(family='Times', size=14)
        self.label109["font"] = ft
        self.label109["fg"] = "#5fb878"
        self.label109["justify"] = "center"
        self.label109["text"] = "自动空间位置插补速度"
        self.label109["relief"] = "flat"
        self.label109.place(x=xpix, y=ypix, width=190, height=30)
        ypix = ypix + 34

        self.label110 = tk.Label(self.master)
        self.label110["anchor"] = "center"
        ft = tkFont.Font(family='Times', size=14)
        self.label110["font"] = ft
        self.label110["fg"] = "#5fb878"
        self.label110["justify"] = "center"
        self.label110["text"] = "自动空间姿态插补速度"
        self.label110["relief"] = "flat"
        self.label110.place(x=xpix, y=ypix, width=190, height=30)
        ypix = ypix + 34

        self.label111 = tk.Label(self.master)
        self.label111["anchor"] = "center"
        ft = tkFont.Font(family='Times', size=14)
        self.label111["font"] = ft
        self.label111["fg"] = "#5fb878"
        self.label111["justify"] = "center"
        self.label111["text"] = "自动空间加速度倍数"
        self.label111["relief"] = "flat"
        self.label111.place(x=xpix, y=ypix, width=190, height=30)
        ypix = ypix + 34

        self.label112 = tk.Label(self.master)
        self.label112["anchor"] = "center"
        ft = tkFont.Font(family='Times', size=14)
        self.label112["font"] = ft
        self.label112["fg"] = "#5fb878"
        self.label112["justify"] = "center"
        self.label112["text"] = "自动空间减速度倍数"
        self.label112["relief"] = "flat"
        self.label112.place(x=xpix, y=ypix, width=190, height=30)
        ypix = ypix + 34

        self.label113 = tk.Label(self.master)
        self.label113["anchor"] = "center"
        ft = tkFont.Font(family='Times', size=14)
        self.label113["font"] = ft
        self.label113["fg"] = "#5fb878"
        self.label113["justify"] = "center"
        self.label113["text"] = "自动空间加加速度倍数"
        self.label113["relief"] = "flat"
        self.label113.place(x=xpix, y=ypix, width=190, height=30)
        ypix = ypix + 34

        self.label114 = tk.Label(self.master)
        self.label114["anchor"] = "center"
        ft = tkFont.Font(family='Times', size=14)
        self.label114["font"] = ft
        self.label114["fg"] = "#5fb878"
        self.label114["justify"] = "center"
        self.label114["text"] = "程序首循环速度倍率"
        self.label114["relief"] = "flat"
        self.label114.place(x=xpix, y=ypix, width=190, height=30)
        ypix = ypix + 34

        self.label115 = tk.Label(self.master)
        self.label115["anchor"] = "center"
        ft = tkFont.Font(family='Times', size=14)
        self.label115["font"] = ft
        self.label115["fg"] = "#5fb878"
        self.label115["justify"] = "center"
        self.label115["text"] = "急停选择"
        self.label115["relief"] = "flat"
        self.label115.place(x=xpix, y=ypix, width=190, height=30)
        ypix = ypix + 34

        self.label116 = tk.Label(self.master)
        self.label116["anchor"] = "center"
        ft = tkFont.Font(family='Times', size=14)
        self.label116["font"] = ft
        self.label116["fg"] = "#5fb878"
        self.label116["justify"] = "center"
        self.label116["text"] = "工艺选择"
        self.label116["relief"] = "flat"
        self.label116.place(x=xpix, y=ypix, width=190, height=30)
        ypix = ypix + 34

        self.label117 = tk.Label(self.master)
        self.label117["anchor"] = "center"
        ft = tkFont.Font(family='Times', size=14)
        self.label117["font"] = ft
        self.label117["fg"] = "#5fb878"
        self.label117["justify"] = "center"
        self.label117["text"] = "使能开关选择"
        self.label117["relief"] = "flat"
        self.label117.place(x=xpix, y=ypix, width=190, height=30)

        #------------------------------------------------------------
        xpix = xpix + 195
        ypix = 90

        self.entry101 = tk.Entry(self.master)
        self.entry101["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=14)
        self.entry101["font"] = ft
        self.entry101["fg"] = "#cc0000"
        self.entry101["justify"] = "center"
        self.entry101["textvariable"] = self.text101
        self.entry101["relief"] = "groove"
        self.entry101.place(x=xpix, y=ypix, width=80, height=30)
        ypix = ypix + 34

        self.entry102 = tk.Entry(self.master)
        self.entry102["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=14)
        self.entry102["font"] = ft
        self.entry102["fg"] = "#cc0000"
        self.entry102["justify"] = "center"
        self.entry102["textvariable"] = self.text102
        self.entry102["relief"] = "groove"
        self.entry102.place(x=xpix, y=ypix, width=80, height=30)
        ypix = ypix + 34

        self.entry103 = tk.Entry(self.master)
        self.entry103["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=14)
        self.entry103["font"] = ft
        self.entry103["fg"] = "#cc0000"
        self.entry103["justify"] = "center"
        self.entry103["textvariable"] = self.text103
        self.entry103["relief"] = "groove"
        self.entry103.place(x=xpix, y=ypix, width=80, height=30)
        ypix = ypix + 34

        self.entry104 = tk.Entry(self.master)
        self.entry104["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=14)
        self.entry104["font"] = ft
        self.entry104["fg"] = "#cc0000"
        self.entry104["justify"] = "center"
        self.entry104["textvariable"] = self.text104
        self.entry104["relief"] = "groove"
        self.entry104.place(x=xpix, y=ypix, width=80, height=30)
        ypix = ypix + 34

        self.entry105 = tk.Entry(self.master)
        self.entry105["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=14)
        self.entry105["font"] = ft
        self.entry105["fg"] = "#cc0000"
        self.entry105["justify"] = "center"
        self.entry105["textvariable"] = self.text105
        self.entry105["relief"] = "groove"
        self.entry105.place(x=xpix, y=ypix, width=80, height=30)
        ypix = ypix + 34

        self.entry106 = tk.Entry(self.master)
        self.entry106["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=14)
        self.entry106["font"] = ft
        self.entry106["fg"] = "#cc0000"
        self.entry106["justify"] = "center"
        self.entry106["textvariable"] = self.text106
        self.entry106["relief"] = "groove"
        self.entry106.place(x=xpix, y=ypix, width=80, height=30)
        ypix = ypix + 34

        self.entry107 = tk.Entry(self.master)
        self.entry107["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=14)
        self.entry107["font"] = ft
        self.entry107["fg"] = "#cc0000"
        self.entry107["justify"] = "center"
        self.entry107["textvariable"] = self.text107
        self.entry107["relief"] = "groove"
        self.entry107.place(x=xpix, y=ypix, width=80, height=30)
        ypix = ypix + 34

        self.entry108 = tk.Entry(self.master)
        self.entry108["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=14)
        self.entry108["font"] = ft
        self.entry108["fg"] = "#cc0000"
        self.entry108["justify"] = "center"
        self.entry108["textvariable"] = self.text108
        self.entry108["relief"] = "groove"
        self.entry108.place(x=xpix, y=ypix, width=80, height=30)
        ypix = ypix + 34

        self.entry109 = tk.Entry(self.master)
        self.entry109["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=14)
        self.entry109["font"] = ft
        self.entry109["fg"] = "#cc0000"
        self.entry109["justify"] = "center"
        self.entry109["textvariable"] = self.text109
        self.entry109["relief"] = "groove"
        self.entry109.place(x=xpix, y=ypix, width=80, height=30)
        ypix = ypix + 34

        self.entry110 = tk.Entry(self.master)
        self.entry110["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=14)
        self.entry110["font"] = ft
        self.entry110["fg"] = "#cc0000"
        self.entry110["justify"] = "center"
        self.entry110["textvariable"] = self.text110
        self.entry110["relief"] = "groove"
        self.entry110.place(x=xpix, y=ypix, width=80, height=30)
        ypix = ypix + 34

        self.entry111 = tk.Entry(self.master)
        self.entry111["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=14)
        self.entry111["font"] = ft
        self.entry111["fg"] = "#cc0000"
        self.entry111["justify"] = "center"
        self.entry111["textvariable"] = self.text111
        self.entry111["relief"] = "groove"
        self.entry111.place(x=xpix, y=ypix, width=80, height=30)
        ypix = ypix + 34

        self.entry112 = tk.Entry(self.master)
        self.entry112["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=14)
        self.entry112["font"] = ft
        self.entry112["fg"] = "#cc0000"
        self.entry112["justify"] = "center"
        self.entry112["textvariable"] = self.text112
        self.entry112["relief"] = "groove"
        self.entry112.place(x=xpix, y=ypix, width=80, height=30)
        ypix = ypix + 34

        self.entry113 = tk.Entry(self.master)
        self.entry113["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=14)
        self.entry113["font"] = ft
        self.entry113["fg"] = "#cc0000"
        self.entry113["justify"] = "center"
        self.entry113["textvariable"] = self.text113
        self.entry113["relief"] = "groove"
        self.entry113.place(x=xpix, y=ypix, width=80, height=30)
        ypix = ypix + 34

        self.entry114 = tk.Entry(self.master)
        self.entry114["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=14)
        self.entry114["font"] = ft
        self.entry114["fg"] = "#cc0000"
        self.entry114["justify"] = "center"
        self.entry114["textvariable"] = self.text114
        self.entry114["relief"] = "groove"
        self.entry114.place(x=xpix, y=ypix, width=80, height=30)
        ypix = ypix + 34

        self.entry115 = tk.Entry(self.master)
        self.entry115["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=14)
        self.entry115["font"] = ft
        self.entry115["fg"] = "#cc0000"
        self.entry115["justify"] = "center"
        self.entry115["textvariable"] = self.text115
        self.entry115["relief"] = "groove"
        self.entry115.place(x=xpix, y=ypix, width=80, height=30)
        ypix = ypix + 34

        self.entry116 = tk.Entry(self.master)
        self.entry116["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=14)
        self.entry116["font"] = ft
        self.entry116["fg"] = "#cc0000"
        self.entry116["justify"] = "center"
        self.entry116["textvariable"] = self.text116
        self.entry116["relief"] = "groove"
        self.entry116.place(x=xpix, y=ypix, width=80, height=30)
        ypix = ypix + 34

        self.entry117 = tk.Entry(self.master)
        self.entry117["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=14)
        self.entry117["font"] = ft
        self.entry117["fg"] = "#cc0000"
        self.entry117["justify"] = "center"
        self.entry117["textvariable"] = self.text117
        self.entry117["relief"] = "groove"
        self.entry117.place(x=xpix, y=ypix, width=80, height=30)

        #------------------------------------------------------------
        xpix = xpix + 90
        ypix = 90

        self.label201 = tk.Label(self.master)
        self.label201["anchor"] = "center"
        ft = tkFont.Font(family='Times', size=14)
        self.label201["font"] = ft
        self.label201["fg"] = "#5fb878"
        self.label201["justify"] = "center"
        self.label201["text"] = "连杆转角"
        self.label201["relief"] = "flat"
        self.label201.place(x=xpix, y=ypix, width=190, height=30)
        ypix = ypix + 34

        self.label202 = tk.Label(self.master)
        self.label202["anchor"] = "center"
        ft = tkFont.Font(family='Times', size=14)
        self.label202["font"] = ft
        self.label202["fg"] = "#5fb878"
        self.label202["justify"] = "center"
        self.label202["text"] = "连杆长度"
        self.label202["relief"] = "flat"
        self.label202.place(x=xpix, y=ypix, width=190, height=30)
        ypix = ypix + 34

        self.label203 = tk.Label(self.master)
        self.label203["anchor"] = "center"
        ft = tkFont.Font(family='Times', size=14)
        self.label203["font"] = ft
        self.label203["fg"] = "#5fb878"
        self.label203["justify"] = "center"
        self.label203["text"] = "连杆偏距"
        self.label203["relief"] = "flat"
        self.label203.place(x=xpix, y=ypix, width=190, height=30)
        ypix = ypix + 34

        self.labe204 = tk.Label(self.master)
        self.labe204["anchor"] = "center"
        ft = tkFont.Font(family='Times', size=14)
        self.labe204["font"] = ft
        self.labe204["fg"] = "#5fb878"
        self.labe204["justify"] = "center"
        self.labe204["text"] = "关节正限位"
        self.labe204["relief"] = "flat"
        self.labe204.place(x=xpix, y=ypix, width=190, height=30)
        ypix = ypix + 34

        self.label205 = tk.Label(self.master)
        self.label205["anchor"] = "center"
        ft = tkFont.Font(family='Times', size=14)
        self.label205["font"] = ft
        self.label205["fg"] = "#5fb878"
        self.label205["justify"] = "center"
        self.label205["text"] = "关节负限位"
        self.label205["relief"] = "flat"
        self.label205.place(x=xpix, y=ypix, width=190, height=30)
        ypix = ypix + 34

        self.label206 = tk.Label(self.master)
        self.label206["anchor"] = "center"
        ft = tkFont.Font(family='Times', size=14)
        self.label206["font"] = ft
        self.label206["fg"] = "#5fb878"
        self.label206["justify"] = "center"
        self.label206["text"] = "空间正限位"
        self.label206["relief"] = "flat"
        self.label206.place(x=xpix, y=ypix, width=190, height=30)
        ypix = ypix + 34

        self.label207 = tk.Label(self.master)
        self.label207["anchor"] = "center"
        ft = tkFont.Font(family='Times', size=14)
        self.label207["font"] = ft
        self.label207["fg"] = "#5fb878"
        self.label207["justify"] = "center"
        self.label207["text"] = "空间负限位"
        self.label207["relief"] = "flat"
        self.label207.place(x=xpix, y=ypix, width=190, height=30)
        ypix = ypix + 34

        self.labe208 = tk.Label(self.master)
        self.labe208["anchor"] = "center"
        ft = tkFont.Font(family='Times', size=14)
        self.labe208["font"] = ft
        self.labe208["fg"] = "#5fb878"
        self.labe208["justify"] = "center"
        self.labe208["text"] = "减速比"
        self.labe208["relief"] = "flat"
        self.labe208.place(x=xpix, y=ypix, width=190, height=30)
        ypix = ypix + 34

        self.label209 = tk.Label(self.master)
        self.label209["anchor"] = "center"
        ft = tkFont.Font(family='Times', size=14)
        self.label209["font"] = ft
        self.label209["fg"] = "#5fb878"
        self.label209["justify"] = "center"
        self.label209["text"] = "导程"
        self.label209["relief"] = "flat"
        self.label209.place(x=xpix, y=ypix, width=190, height=30)
        ypix = ypix + 34

        self.label210 = tk.Label(self.master)
        self.label210["anchor"] = "center"
        ft = tkFont.Font(family='Times', size=14)
        self.label210["font"] = ft
        self.label210["fg"] = "#5fb878"
        self.label210["justify"] = "center"
        self.label210["text"] = "编码器分辨率"
        self.label210["relief"] = "flat"
        self.label210.place(x=xpix, y=ypix, width=190, height=30)
        ypix = ypix + 34

        self.label211 = tk.Label(self.master)
        self.label211["anchor"] = "center"
        ft = tkFont.Font(family='Times', size=14)
        self.label211["font"] = ft
        self.label211["fg"] = "#5fb878"
        self.label211["justify"] = "center"
        self.label211["text"] = "电机额定力矩"
        self.label211["relief"] = "flat"
        self.label211.place(x=xpix, y=ypix, width=190, height=30)
        ypix = ypix + 34

        self.label212 = tk.Label(self.master)
        self.label212["anchor"] = "center"
        ft = tkFont.Font(family='Times', size=14)
        self.label212["font"] = ft
        self.label212["fg"] = "#5fb878"
        self.label212["justify"] = "center"
        self.label212["text"] = "电机最大转速"
        self.label212["relief"] = "flat"
        self.label212.place(x=xpix, y=ypix, width=190, height=30)
        ypix = ypix + 34

        self.label213 = tk.Label(self.master)
        self.label213["anchor"] = "center"
        ft = tkFont.Font(family='Times', size=14)
        self.label213["font"] = ft
        self.label213["fg"] = "#5fb878"
        self.label213["justify"] = "center"
        self.label213["text"] = "手动关节最大速度"
        self.label213["relief"] = "flat"
        self.label213.place(x=xpix, y=ypix, width=190, height=30)
        ypix = ypix + 34

        self.label214 = tk.Label(self.master)
        self.label214["anchor"] = "center"
        ft = tkFont.Font(family='Times', size=14)
        self.label214["font"] = ft
        self.label214["fg"] = "#5fb878"
        self.label214["justify"] = "center"
        self.label214["text"] = "手动空间最大速度"
        self.label214["relief"] = "flat"
        self.label214.place(x=xpix, y=ypix, width=190, height=30)
        ypix = ypix + 34

        self.label215 = tk.Label(self.master)
        self.label215["anchor"] = "center"
        ft = tkFont.Font(family='Times', size=14)
        self.label215["font"] = ft
        self.label215["fg"] = "#5fb878"
        self.label215["justify"] = "center"
        self.label215["text"] = "自动附加轴插补速度"
        self.label215["relief"] = "flat"
        self.label215.place(x=xpix, y=ypix, width=190, height=30)

        #------------------------------------------------------------
        xpix = xpix + 195
        ypix = 90

        self.entry201 = tk.Entry(self.master)
        self.entry201["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=14)
        self.entry201["font"] = ft
        self.entry201["fg"] = "#cc0000"
        self.entry201["justify"] = "center"
        self.entry201["textvariable"] = self.text201
        self.entry201["relief"] = "groove"
        self.entry201.place(x=xpix, y=ypix, width=500, height=30)
        ypix = ypix + 34

        self.entry202 = tk.Entry(self.master)
        self.entry202["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=14)
        self.entry202["font"] = ft
        self.entry202["fg"] = "#cc0000"
        self.entry202["justify"] = "center"
        self.entry202["textvariable"] = self.text202
        self.entry202["relief"] = "groove"
        self.entry202.place(x=xpix, y=ypix, width=500, height=30)
        ypix = ypix + 34

        self.entry203 = tk.Entry(self.master)
        self.entry203["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=14)
        self.entry203["font"] = ft
        self.entry203["fg"] = "#cc0000"
        self.entry203["justify"] = "center"
        self.entry203["textvariable"] = self.text203
        self.entry203["relief"] = "groove"
        self.entry203.place(x=xpix, y=ypix, width=500, height=30)
        ypix = ypix + 34

        self.entry204 = tk.Entry(self.master)
        self.entry204["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=14)
        self.entry204["font"] = ft
        self.entry204["fg"] = "#cc0000"
        self.entry204["justify"] = "center"
        self.entry204["textvariable"] = self.text204
        self.entry204["relief"] = "groove"
        self.entry204.place(x=xpix, y=ypix, width=500, height=30)
        ypix = ypix + 34

        self.entry205 = tk.Entry(self.master)
        self.entry205["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=14)
        self.entry205["font"] = ft
        self.entry205["fg"] = "#cc0000"
        self.entry205["justify"] = "center"
        self.entry205["textvariable"] = self.text205
        self.entry205["relief"] = "groove"
        self.entry205.place(x=xpix, y=ypix, width=500, height=30)
        ypix = ypix + 34

        self.entry206 = tk.Entry(self.master)
        self.entry206["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=14)
        self.entry206["font"] = ft
        self.entry206["fg"] = "#cc0000"
        self.entry206["justify"] = "center"
        self.entry206["textvariable"] = self.text206
        self.entry206["relief"] = "groove"
        self.entry206.place(x=xpix, y=ypix, width=500, height=30)
        ypix = ypix + 34

        self.entry207 = tk.Entry(self.master)
        self.entry207["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=14)
        self.entry207["font"] = ft
        self.entry207["fg"] = "#cc0000"
        self.entry207["justify"] = "center"
        self.entry207["textvariable"] = self.text207
        self.entry207["relief"] = "groove"
        self.entry207.place(x=xpix, y=ypix, width=500, height=30)
        ypix = ypix + 34

        self.entry208 = tk.Entry(self.master)
        self.entry208["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=14)
        self.entry208["font"] = ft
        self.entry208["fg"] = "#cc0000"
        self.entry208["justify"] = "center"
        self.entry208["textvariable"] = self.text208
        self.entry208["relief"] = "groove"
        self.entry208.place(x=xpix, y=ypix, width=500, height=30)
        ypix = ypix + 34

        self.entry209 = tk.Entry(self.master)
        self.entry209["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=14)
        self.entry209["font"] = ft
        self.entry209["fg"] = "#cc0000"
        self.entry209["justify"] = "center"
        self.entry209["textvariable"] = self.text209
        self.entry209["relief"] = "groove"
        self.entry209.place(x=xpix, y=ypix, width=500, height=30)
        ypix = ypix + 34

        self.entry210 = tk.Entry(self.master)
        self.entry210["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=14)
        self.entry210["font"] = ft
        self.entry210["fg"] = "#cc0000"
        self.entry210["justify"] = "center"
        self.entry210["textvariable"] = self.text210
        self.entry210["relief"] = "groove"
        self.entry210.place(x=xpix, y=ypix, width=500, height=30)
        ypix = ypix + 34

        self.entry211 = tk.Entry(self.master)
        self.entry211["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=14)
        self.entry211["font"] = ft
        self.entry211["fg"] = "#cc0000"
        self.entry211["justify"] = "center"
        self.entry211["textvariable"] = self.text211
        self.entry211["relief"] = "groove"
        self.entry211.place(x=xpix, y=ypix, width=500, height=30)
        ypix = ypix + 34

        self.entry212 = tk.Entry(self.master)
        self.entry212["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=14)
        self.entry212["font"] = ft
        self.entry212["fg"] = "#cc0000"
        self.entry212["justify"] = "center"
        self.entry212["textvariable"] = self.text212
        self.entry212["relief"] = "groove"
        self.entry212.place(x=xpix, y=ypix, width=500, height=30)
        ypix = ypix + 34

        self.entry213 = tk.Entry(self.master)
        self.entry213["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=14)
        self.entry213["font"] = ft
        self.entry213["fg"] = "#cc0000"
        self.entry213["justify"] = "center"
        self.entry213["textvariable"] = self.text213
        self.entry213["relief"] = "groove"
        self.entry213.place(x=xpix, y=ypix, width=500, height=30)
        ypix = ypix + 34

        self.entry214 = tk.Entry(self.master)
        self.entry214["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=14)
        self.entry214["font"] = ft
        self.entry214["fg"] = "#cc0000"
        self.entry214["justify"] = "center"
        self.entry214["textvariable"] = self.text214
        self.entry214["relief"] = "groove"
        self.entry214.place(x=xpix, y=ypix, width=500, height=30)
        ypix = ypix + 34

        self.entry215 = tk.Entry(self.master)
        self.entry215["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=14)
        self.entry215["font"] = ft
        self.entry215["fg"] = "#cc0000"
        self.entry215["justify"] = "center"
        self.entry215["textvariable"] = self.text215
        self.entry215["relief"] = "groove"
        self.entry215.place(x=xpix, y=ypix, width=500, height=30)
        ypix = ypix + 50

        #------------------------------------------------------------
        self.labellog = tk.Label(self.master)
        self.labellog["anchor"] = "center" 
        ft = tkFont.Font(family='Times', size=14)
        self.labellog["font"] = ft
        self.labellog["fg"] = "#5fb878"
        self.labellog["justify"] = "center"
        self.labellog["text"] = "waiting for you ..."
        self.labellog["relief"] = "flat"
        self.labellog.place(x=xpix, y=ypix, width=400, height=30)
        return

    def filenew(self):
        self.text101.set("")
        self.text102.set("")
        self.text103.set("")
        self.text104.set("")
        self.text105.set("")
        self.text106.set("")
        self.text107.set("")
        self.text108.set("")
        self.text109.set("")
        self.text110.set("")
        self.text111.set("")
        self.text112.set("")
        self.text113.set("")
        self.text114.set("")
        self.text115.set("")
        self.text116.set("")
        self.text117.set("")
        self.text201.set("")
        self.text202.set("")
        self.text203.set("")
        self.text204.set("")
        self.text205.set("")
        self.text206.set("")
        self.text207.set("")
        self.text208.set("")
        self.text209.set("")
        self.text210.set("")
        self.text211.set("")
        self.text212.set("")
        self.text213.set("")
        self.text214.set("")
        self.text215.set("")
        self.labellog["text"]="start a new one"
        return
    
    def fileopen(self):
        file =tk.filedialog.askopenfilename(title='选择文件')
        flag,data=read(file)
        if flag==False:
            self.labellog["text"]="open fail"
            return
        self.text101.set(data.robottype)
        self.text102.set(data.jogacc)
        self.text103.set(data.jogdec)
        self.text104.set(data.jogjerk)
        self.text105.set(data.jogstepvel)
        self.text106.set(data.ataxisacc)
        self.text107.set(data.ataxisdec)
        self.text108.set(data.ataxisjerk)
        self.text109.set(data.atlinemaxvel)
        self.text110.set(data.atposemaxvel)
        self.text111.set(data.atcoordacc)
        self.text112.set(data.atcoorddec)
        self.text113.set(data.atcoordjerk)
        self.text114.set(data.fisrtcycvel)
        self.text115.set(data.emergencysel)
        self.text116.set(data.craftsel)
        self.text117.set(data.enablesel)
        self.text201.set(data.alpha)
        self.text202.set(data.a)
        self.text203.set(data.d)
        self.text204.set(data.axisposlimit)
        self.text205.set(data.axisneglimit)
        self.text206.set(data.coordposlimit)
        self.text207.set(data.coordneglimit)
        self.text208.set(data.reductionratio)
        self.text209.set(data.axislead)
        self.text210.set(data.pulsepercir)
        self.text211.set(data.motortorque)
        self.text212.set(data.motormaxvel)
        self.text213.set(data.jogaxismaxvel)
        self.text214.set(data.jogcordmaxvel)
        self.text215.set(data.atextmaxvel)
        self.labellog["text"]="open success"
        return

    def filesave(self):
        # print('save')
        return

    def filesaveas(self):
        # print("saveas")
        return

    def fileclose(self):
        # print('close')
        return

    def editorquit(self):
        self.destroy()
        self.quit()

    def editorhelp(self):
        # print('help')
        return

    def editorabout(self):
        # print('about')
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
