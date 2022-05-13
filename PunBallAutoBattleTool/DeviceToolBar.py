# -*- coding: utf-8 -*-
# @Path : C:\Users\zengf\AppData\Local\Programs\Python\Python39
# @Time : 2022/5/1 19:29
# @Author : zengf
# @Email : 944458157@qq.com
# @File : DeviceToolBar.py
# @Project : workspace

import wx
import wx.lib.agw.aui as aui
import re
from threading import Thread

import pyimg
from adb_device import connectDevice, refreshDevices
from config import BAT_RUNNER_PATH

# 已连接设备缓存，判断是否刷新工具栏，以及是否更新bat文件
DEVICE_CACHE = []
ID_ToolBar = wx.ID_HIGHEST + 1

'''
引入多线程后，如果adb连接时间较长，前端体验不好，需优化
'''
class ConnectThread(Thread):
    def __init__(self, newDevInfoStr, myToolBar):
        Thread.__init__(self)
        print("正在连接设备 %s......" % newDevInfoStr.encode("utf-8"))
        self.newDevInfoStr = newDevInfoStr.encode("utf-8")
        self.myToolBar = myToolBar

    def run(self):
#         print "Run ConnectThread..."
        r = connectDevice(self.newDevInfoStr)
        is_ok = r[0]
        message = r[1]
        if is_ok:
            print("已连接设备 %s......" % self.newDevInfoStr)
        else:
            showDialog("错误", message)
            return

        # 刷新adb设备列表,获取当前连接设备列表，正确则返回 [( str(ip:端口), str(ADB Status), str"设备名称" ), ()......]
        # 错误返回错误消息
        devs = refreshDevices()
#        print devs
        if type(devs) is list:
            print("ADB连接设备列表: ", devs)
        else:
            showDialog("错误", devs)

        self.myToolBar._refreshToolBar(devs)

class DeviceToolBar(aui.AuiToolBar):
    def __init__(self, parent):
        aui.AuiToolBar.__init__(self, parent)

        #self.SetToolBitmapSize(wx.Size(20, 20))

        self.refresh_icon = pyimg.Refresh.GetBitmap()   # <class 'wx._core.Bitmap'>
        self.device_icon = pyimg.AndroidDevice.GetBitmap()

        self.inputTextCtrl = wx.TextCtrl(self, value="IP:端口号", size=(200, -1))
        # self.inputTextCtrl.SetFont(font)

        # 布局控件和工具
        self.AddControl(self.inputTextCtrl)
        refresh_tool_id = ID_ToolBar + 1
        self.AddSimpleTool(refresh_tool_id, "refresh", self.refresh_icon, short_help_string="无输入--刷新设备列表\nIP:端口号 -- 连接新设备")
        self.AddSeparator()

        # 实现工具栏。添加工具后应调用此函数
        self.Realize()

        self.Bind(wx.EVT_TOOL, self.onUpdateTool, id=refresh_tool_id)  # aui.EVT_AUITOOLBAR_TOOL_DROPDOWN

    def onUpdateTool(self, event):

        newDevInfo = self.inputTextCtrl.GetValue()
        re = self.__checkNewDevInfo(newDevInfo)

        if re == 0: # 新设备信息格式错误
            showDialog("错误", "格式错误，请重新输入(IP:端口号)")

        elif re == 1: # 连接新设备
            # 多线程，防connect时GUI界面卡死
            thread_connecting = ConnectThread(newDevInfo, self)
            thread_connecting.start()

        else:   # 刷新连接设备列表
            devs = refreshDevices()
            #        print devs
            if type(devs) is list:
                print("ADB连接设备列表: ", devs)
            else:
                showDialog("错误", devs)

            self._refreshToolBar(devs)

    def __checkNewDevInfo(self, newDevInfo):
        '''
        :param newDevInfo: 新设备的 ip:端口号
        :return: ip:端口号校验正确，表示需要连接新设备，返回1；
                无输入，表示重新刷新adb设备列表，返回2；
                输入错误，等，表示错误，返回0
        '''
        # IP地址的正则表达式255.255.255.255
        r = r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?):\d{4,5}$"

        if re.match(r, newDevInfo):
            return 1

        if newDevInfo == "IP:端口号".decode("utf-8") or newDevInfo == "":
            return 2

        return 0

    def _refreshToolBar(self, devs):
        '''
        更新工具栏和本地bat文件
        :param devs: 设备列表，当有设备连接时为[]，否则为str
        :return:
        '''

        if isinstance(devs, str):
            devs = []

        j = 2
        updateCache = 0
        global DEVICE_CACHE
        for dev in devs:
            if dev not in DEVICE_CACHE:
                updateCache = 1

        for device_name in DEVICE_CACHE:
            if device_name not in devs:
                updateCache = 1

        if updateCache:
            print("设备信息更新，同步bat文件......")
            # 更新缓存
            DEVICE_CACHE = devs[:]

            # 更新工具条，和bat文件
            # 先清空工具条
            count_tools = self.GetToolCount()
#            print "count_tools: ", count_tools
            if count_tools > 3:
                for i in range(1, count_tools - 2):
#                    print "删除id:", ID_ToolBar + 1 + i
                    self.DeleteTool(ID_ToolBar + 1 + i)

            content_moduleTest = '@echo off\n'
            content_monkeyTest = '@echo off\n'
            for dev in devs:
                short_help_string = dev[0] + "|" + dev[1] + "|" + dev[2]
#                print "增加id:", ID_ToolBar+j
                # 添加工具
                self.AddSimpleTool(ID_ToolBar + j, "device %s" % str(j - 2), self.device_icon, short_help_string)
                #self.AddSeparator()
                j += 1

                # bat文件内容
                ip_port = dev[0]
                dev_name = dev[2]

                c1 = 'start python ' + BAT_RUNNER_PATH.replace("deviceRunner.bat", "runUnittest.py ") + \
                    ip_port + " " + dev_name + "\n"
                content_moduleTest += c1
#                print content_moduleTest

                c2 = 'start python ' + BAT_RUNNER_PATH_MONKEYTEST.replace("monkeyTestRunner.bat", "runUnittest_old.py ") + \
                     ip_port + " " + dev_name + "\n"
                content_monkeyTest += c2

            # 刷新工具条
            self.Realize()
            # 更新bat文件
            with open(BAT_RUNNER_PATH, "w") as b:    # 没有bat文件，创建bat文件
                b.truncate()
                b.write(content_moduleTest)

            with open(BAT_RUNNER_PATH_MONKEYTEST, "w") as b:    # 没有bat文件，创建bat文件
                b.truncate()
                b.write(content_monkeyTest)
        else:
            print("设备信息无变化")


    def __updataBatFile(self):
        pass