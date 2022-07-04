# -*- coding: utf-8 -*-
# @Path : C:\Users\zengf\AppData\Local\Programs\Python\Python39
# @Time : 2022/5/1 19:28
# @Author : zengf
# @Email : 944458157@qq.com
# @File : try.py
# @Project : workspace
import sys, wx, time
from wx.lib.mixins.listctrl import CheckListCtrlMixin, ListCtrlAutoWidthMixin
from config import SerialNumber, ComPORT, ComIP, ComPASSWORD, ComUSERNAME, DirPath, DeviceToken
from adb_device import rentDevices, disrentDevices
import paramiko


class remote_control():
    def __init__(self, commond):
        self.cmd = commond
        # 1.创建一个ssh对象
        self.client = paramiko.SSHClient()
        # 2.解决问题:如果之前没有，连接过的ip，会出现选择yes或者no的操作，
        # 自动选择yes
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 3.连接服务器
        self.client.connect(hostname=ComIP, port=ComPORT, username=ComUSERNAME, password=ComPASSWORD, allow_agent=False,
                       look_for_keys=False)

    def run(self):
        # 4.执行操作
        stdin, stdout, stderr = self.client.exec_command(self.cmd)
        return stdin, stdout, stderr

    def stop(self):
        self.client.close()


class RedirectText(object):
    def __init__(self, aWxTextCtrl):
        self.out = aWxTextCtrl

    def write(self, string):
        # self.out.WriteText(string)
        wx.CallAfter(self.out.WriteText, string)


class CheckListCtrl(wx.ListCtrl, CheckListCtrlMixin, ListCtrlAutoWidthMixin):
    def __init__(self, parent):
        wx.ListCtrl.__init__(self, parent, wx.ID_ANY, style=wx.LC_REPORT | wx.SUNKEN_BORDER)
        CheckListCtrlMixin.__init__(self)
        ListCtrlAutoWidthMixin.__init__(self)


def getdircase():
    ls = remote_control('dir ' + DirPath)
    text = ls.run()[1]
    dirs = []
    result = text.read().decode("gbk").encode("utf-8").decode()
    # print(text.read().decode("gbk").encode("utf-8").decode())
    for d in result.split("\r\n"):
        # print(d)
        if 'AutoBattle' in d:
            dirs.append(d.split("          ")[1])
    # print(dirs)
    ls.stop()
    return dirs


class MyForm(wx.Frame):
    def __init__(self):
        m = wx.DisplaySize()
        screenWidth = m[0]
        screenHigh = m[1]
        wx.Frame.__init__(self, None, title="弹球自动战斗测试工具", size=(screenWidth, screenHigh), pos=(0, 0))

        self.findDlg = None
        self.findData = wx.FindReplaceData()
        self.findData.SetFlags(wx.FR_DOWN)

        self.findCount = 0  # Debug，计算点击查查找钮次数

        # 菜单栏，提供搜索功能
        self.mainMenu = wx.MenuBar()
        menu = wx.Menu()
        findItem = wx.MenuItem(menu, -1, '&Find\tCtrl-F', 'Find in the Demo Code')

        menu.Append(findItem)

        self.Bind(wx.EVT_MENU, self.onHelpFind, findItem)

        self.mainMenu.Append(menu, '&Help')
        self.SetMenuBar(self.mainMenu)

        self.dircase = getdircase()

        self.panel = wx.Panel(self, wx.ID_ANY)
        self.grid = wx.GridBagSizer(hgap=5, vgap=2)  # 行和列的间距  像素

        self.numbers = list(SerialNumber.values())
        print(self.numbers)
        self.l = len(self.numbers)

        self.connectButton = wx.Button(self.panel, label='1.租用设备')
        self.grid.Add(self.connectButton, pos=(0, 2), span=(1, 1))
        self.Bind(wx.EVT_BUTTON, self.onconnectButton, self.connectButton)
        self.disrent = wx.Button(self.panel, label='5.取消租用')
        self.grid.Add(self.disrent, pos=(0, 3), span=(1, 1))
        self.Bind(wx.EVT_BUTTON, self.ondisrent, self.disrent)
        self.deviceTab = wx.StaticText(self.panel, label='STF 设备如下：')
        self.grid.Add(self.deviceTab, pos=(0, 0))
        for i in range(self.l):
            create = """
self.d{0} = wx.CheckBox(self.panel, label=self.numbers[{1}])
self.d{2}.SetValue(0)
self.grid.Add(self.d{4}, pos=({5}, 0), span=(1, 1))
self.Bind(wx.EVT_CHECKBOX, self.checkBox, self.d{6})""".format(i, i, i, i, i, i+1, i)
            exec(create)
        self.chooseButton = wx.Button(self.panel, label='2.选择设备')
        self.chooseButton.Enable(False)
        self.grid.Add(self.chooseButton, pos=(self.l, 2), span=(1, 1))
        self.Bind(wx.EVT_BUTTON, self.onchooseButton, self.chooseButton)
        # self.rechooseButton = wx.Button(self.panel, label='重新选择设备')
        # self.grid.Add(self.rechooseButton, pos=(self.l, 3), span=(1, 1))
        # self.Bind(wx.EVT_BUTTON, self.onrechooseButton, self.rechooseButton)

        self.cases = wx.StaticText(self.panel, label='现有自动化脚本：')
        self.grid.Add(self.cases, pos=(self.l+2, 0))
        self.dl = len(self.dircase)
        for i in range(self.dl):
            create = """
self.dir{0} = wx.CheckBox(self.panel, label=self.dircase[{1}])
self.dir{2}.SetValue(0)
self.grid.Add(self.dir{3}, pos=({4}, 0), span=(1, 1))
self.Bind(wx.EVT_CHECKBOX, self.checkBoxDir, self.dir{5})""".format(i, i, i, i, i + self.l+3, i)
            exec(create)
        self.chooseDir = wx.Button(self.panel, label='3.选择脚本')
        self.grid.Add(self.chooseDir, pos=(self.l+2+self.dl, 2), span=(1, 1))
        self.Bind(wx.EVT_BUTTON, self.onchooseDir, self.chooseDir)
        self.rechooseDir = wx.Button(self.panel, label='重新选择脚本')
        self.grid.Add(self.rechooseDir, pos=(self.l+2+self.dl, 3), span=(1, 1))
        self.Bind(wx.EVT_BUTTON, self.onrechooseDir, self.rechooseDir)
        self.run = wx.Button(self.panel, label='4.用指定设备运行所选脚本')
        self.grid.Add(self.run, pos=(self.l+3+self.dl, 2), span=(1, 1))
        self.Bind(wx.EVT_BUTTON, self.dirRun, self.run)
        self.cases = wx.StaticText(self.panel, label='运行情况如下：')
        self.grid.Add(self.cases, pos=(self.l+4+self.dl, 0))
        for i in range(self.l):
            devstatic = self.numbers[i]
            create = """
self.{0} = wx.StaticText(self.panel, label='设备：XX正在运行脚本XXX', size=(400,20))
self.grid.Add(self.{0}, pos=(self.l+5+self.dl+i, 0))
self.{0}Stop = wx.Button(self.panel, label='停止')
self.grid.Add(self.{0}Stop, pos=(self.l+5+self.dl+i, 2), span=(1, 1))
self.{0}Stop.Enable(False)
self.Bind(wx.EVT_BUTTON, self.stopCmd, self.{0}Stop)""".format(devstatic)
            exec(create)
        self.clearButton = wx.Button(self.panel, label='清空')
        self.grid.Add(self.clearButton, pos=(34, 2))
        self.Bind(wx.EVT_BUTTON, self.onclearButton, self.clearButton)

        self.logger = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE | wx.HSCROLL | wx.TE_RICH2 | wx.TE_READONLY)  #

        hSizer = wx.BoxSizer(wx.HORIZONTAL)
        hSizer.Add(self.grid, 0, wx.ALL, 5)
        hSizer.Add(self.logger, 1, wx.ALL | wx.EXPAND, 5)
        self.panel.SetSizer(hSizer)

        # 打印重定向到self.logger
        redir = RedirectText(self.logger)
        sys.stdout = redir

    def checkBox(self, event):
        self.chooseButton.Enable(True)

    def checkBoxDir(self, event):
        self.check = True
        for i in range(len(self.dircase)):
            temp = """
if not self.dir{0}.IsChecked():
    self.dir{1}.Enable(False)
else:
    self.check = False""".format(i, i)
            exec(temp)
        if self.check:
            for j in range(len(self.dircase)):
                temp = """
self.dir{0}.Enable(True)
""".format(j)
                exec(temp)

    def onconnectButton(self, event):
        self.getChooseDev("d")
        rent = {}
        for d in self.chooseDev:
            for s, n in SerialNumber.items():
                if d == n:
                    rent[s] = n
        self.dip = rentDevices(rent)
        for d, ip in self.dip.items():
            print(d, ip)
        for i in range(len(self.numbers)):
            temp = """
self.d{0}.Enable(True)""".format(i)
            exec(temp)

    def ondisrent(self, event):
        rent = {}
        for d in self.chooseDev:
            for s, n in SerialNumber.items():
                if d == n:
                    rent[s] = n
        disrentDevices(rent)

    def getChooseDev(self, event):
        self.chooseDev = []
        self.chooseDir = ''
        if event == "d":
            for i in range(self.l):
                temp = """
if self.d{0}.IsChecked():
    self.chooseDev.append(self.d{1}.Label)""".format(i, i)
                exec(temp)
        if event == "dir":
            for i in range(len(self.dircase)):
                temp = """
if self.dir{0}.IsChecked():
    self.dir{1}.Enable(False)
    self.chooseDir = self.dir{2}.Label""".format(i, i, i)
                exec(temp)

    def onchooseButton(self, event):
        self.getChooseDev("d")
        if self.chooseDev == []:
            print("没有选择任何一台设备！！！！！")
        else:
            print(self.chooseDev)
        self.connectDev()
        return self.chooseDev

    def onrechooseButton(self, event):
        self.chooseDev = []
#         for i in range(self.l):
#             temp = """
# self.d{0}.Enable(True)""".format(i)
#             exec(temp)

    def connectDev(self):
        for d in self.chooseDev:
            cmd = 'adb connect ' + self.dip[d]
            adb = remote_control(cmd)
            adb.run()
            adb.stop()

    def onchooseDir(self, event):
        self.getChooseDev("dir")
        if '' == self.chooseDir:
            print("没有选择任何一个脚本！！！！！")
        else:
            print(self.chooseDir)
        return self.chooseDir

    def onrechooseDir(self, event):
        for i in range(len(self.dircase)):
            temp = """
self.dir{0}.Enable(True)""".format(i)
            exec(temp)

    def dirRun(self, event):
        for dev in self.chooseDev:
            runcmd = "airtest run " + DirPath + "\\" + self.chooseDir + " --device Android:///" + \
                     self.dip[dev] + "?" + DeviceToken[dev]
            print("执行命令行：{0}".format(runcmd))
            # autorun = remote_control(runcmd)
            # autorun.run()
            create = """
self.{0}.SetLabel("设备：{1}正在运行脚本{2}")
self.{3}Stop.Enable(True)""".format(dev, dev, self.chooseDir, dev)
            exec(create)
            sshclient = """
self.{0}ssh = remote_control(runcmd)
self.{1}ssh.run()""".format(dev, dev)
            exec(sshclient)

    def stopCmd(self, event):
        target = event.Id
        for i in range(self.l):
            dev = self.numbers[i]
            over = """
if target == self.{0}Stop.Id:
    self.{0}ssh.stop()
    self.{0}Stop.Enable(False)
    self.{0}.SetLabel("设备：XX正在运行脚本XXX")
    s = 'adb disconnect ' + self.dip['{0}']
    st = remote_control(s)
    st.run()
    st.stop()
    time.sleep(1)
    c = 'adb connect ' + self.dip['{0}']
    con = remote_control(c)
    con.run()
    con.stop()""".format(dev)
            exec(over)

    def onHelpFind(self, event):
        '''处理菜单栏查找按钮功能'''
        if self.findDlg != None:
            return
        self.findDlg = wx.FindReplaceDialog(self, self.findData, "Find",
                                            wx.FR_NOMATCHCASE | wx.FR_NOWHOLEWORD)
        self.findDlg.Show(True)

    def onclearButton(self, event):
        self.logger.Clear()


if __name__ == '__main__':
    app = wx.App()
    frame = MyForm().Show()
    app.MainLoop()