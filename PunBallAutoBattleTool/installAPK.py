# -*- coding: utf-8 -*-
# @Path : C:\Users\zengf\AppData\Local\Programs\Python\Python39
# @Time : 2022/7/6 10:52
# @Author : zengf
# @Email : 944458157@qq.com
# @File : installAPK.py
# @Project : workspace

import subprocess
import threading
import ctypes
import inspect
from airtest.core.api import *
import time


class findThread(threading.Thread):
    def __init__(self, deviceId, ip):
        threading.Thread.__init__(self)
        auto_setup(basedir=__file__, devices=['Android:///{0}'.format(ip)])
        self.deviceId = deviceId

    def run(self):
        if self.deviceId == "Oppo_R15s" or self.deviceId == "Oppo_Find_X":
            while True:
                if exists(Template(r"tpl1657005313599.png", record_pos=(0.007, 0.974), resolution=(1080, 2340))):
                    touch(Template(r"tpl1657005153680.png", record_pos=(0.001, 0.98), resolution=(1080, 2340)))
                    sleep(8)
                    touch(Template(r"tpl1657013143078.png", record_pos=(0.001, 0.981), resolution=(1080, 2340)))
                    break
                elif exists(Template(r"tpl1657013629434.png", record_pos=(-0.006, -0.396), resolution=(1080, 2340))):
                    sleep(1)
                    keyevent("h")
                    keyevent("a")
                    keyevent("b")
                    keyevent("b")
                    keyevent("y")
                    keyevent("9")
                    keyevent("7")
                    keyevent("8")
                    keyevent("16")
                    sleep(1)
                    touch(Template(r"tpl1657012998047.png", record_pos=(0.219, -0.153), resolution=(1080, 2340)))
                    sleep(7)
                    touch(Template(r"tpl1657005153680.png", record_pos=(0.001, 0.98), resolution=(1080, 2340)))
                    sleep(8)
                    touch(Template(r"tpl1657013143078.png", record_pos=(0.001, 0.981), resolution=(1080, 2340)))
                    break
                else:
                    continue
        elif self.deviceId == "Oppo_R11t":
            while True:
                if exists(Template(r"tpl1657006083137.png", record_pos=(-0.016, 0.03), resolution=(1080, 1920))):
                    touch(Template(r"tpl1657013272003.png", record_pos=(0.194, 0.764), resolution=(1080, 1920)))
                    sleep(1)
                    touch(Template(r"tpl1657005153680.png", record_pos=(0.001, 0.98), resolution=(1080, 2340)))
                    sleep(10)
                    touch(Template(r"tpl1657013306327.png", record_pos=(-0.002, 0.739), resolution=(1080, 1920)))
                    break
                elif exists(Template(r"tpl1657006738746.png", record_pos=(0.0, -0.389), resolution=(1080, 1920))):
                    sleep(1)
                    keyevent("h")
                    keyevent("a")
                    keyevent("b")
                    keyevent("b")
                    keyevent("y")
                    keyevent("9")
                    keyevent("7")
                    keyevent("8")
                    keyevent("16")
                    sleep(1)
                    touch(Template(r"tpl1657012998047.png", record_pos=(0.219, -0.153), resolution=(1080, 2340)))
                    sleep(7)
                    touch(Template(r"tpl1657013272003.png", record_pos=(0.194, 0.764), resolution=(1080, 1920)))
                    sleep(1)
                    touch(Template(r"tpl1657005153680.png", record_pos=(0.001, 0.98), resolution=(1080, 2340)))
                    sleep(10)
                    touch(Template(r"tpl1657013306327.png", record_pos=(-0.002, 0.739), resolution=(1080, 1920)))
                    break
                else:
                    continue
        elif self.deviceId == "Oppo_Reno3":
            while True:
                if exists(Template(r"tpl1657007975836.png", record_pos=(-0.195, 0.99), resolution=(1080, 2400))):
                    touch(Template(r"tpl1657007975836.png", record_pos=(-0.195, 0.99), resolution=(1080, 2400)))
                    sleep(10)
                    touch(Template(r"tpl1657008056352.png", record_pos=(0.227, 0.999), resolution=(1080, 2400)))
                    break
                else:
                    continue
        elif self.deviceId == "Realme_GT_Neo":
            while True:
                if exists(Template(r"tpl1657007904764.png", record_pos=(0.0, 0.053), resolution=(1080, 2400))):
                    touch(Template(r"tpl1657007975836.png", record_pos=(-0.195, 0.99), resolution=(1080, 2400)))
                    sleep(10)
                    touch(Template(r"tpl1657010826953.png", record_pos=(0.233, 0.999), resolution=(1080, 2400)))
                    break
                else:
                    continue
        elif self.deviceId == "Vivo_Z5x":
            while True:
                if exists(Template(r"tpl1657014310429.png", record_pos=(0.002, 0.929), resolution=(1080, 2340))):
                    touch(Template(r"tpl1657014335045.png", record_pos=(-0.006, 0.935), resolution=(1080, 2340)))
                    sleep(8)
                    break
                else:
                    continue
        else:
            pass


def installAll(dev, apath, ip):
    unin1 = subprocess.Popen('adb -s ' + ip + ' uninstall com.habby.punball')
    unin2 = subprocess.Popen('adb -s ' + ip + ' uninstall com.habby.archero')
    print('adb -s ' + ip + ' uninstall com.habby.punball')
    print('adb -s ' + ip + ' uninstall com.habby.archero')
    ins = subprocess.Popen('adb -s ' + ip + ' install ' + apath, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding='utf-8')
    print('adb -s ' + ip + ' install ' + apath)
    find = findThread(dev, ip)
    print(dev, ip)
    find.start()
    if "Failure" in ins.communicate()[0]:
        print("{}安装失败！！！".format(dev))
    else:
        print("{}安装成功！！！".format(dev))


# installAll("Oppo_R15s", "D:\\workspace\\Punball_2_0_0(289)Debug.apk", "172.16.18.94:7409")

