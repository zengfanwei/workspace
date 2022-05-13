# -*- coding: utf-8 -*-
# @Path : C:\Users\zengf\AppData\Local\Programs\Python\Python39
# @Time : 2022/4/26 17:53
# @Author : zengf
# @Email : 944458157@qq.com
# @File : adb.py
# @Project : workspace
import os

import time

print("===============================================================")

print(" 欢迎使用多设备投屏工具 ")

print(" code by smilediao QQ 379389449 2020.12.27 ")

print("本程序仅做了多开投屏快捷操作，投屏功能主要由gihub中开源的scrcpy")

print("===============================================================")

s=os.popen("adb devices")

a=s.read()

list=a.split('\n')

deviceList=[]

for temp in list:

    if len(temp.split())>1:

        if temp.split()[1]=='device':

            deviceList.append(temp.split()[0])

command=""

print('本次共扫描出%s个安卓设备'%len(deviceList))

for devicename in deviceList:

    print(devicename)

    for device in deviceList:

        print("正在准备%s设备的投屏"%device)

        command="scrcpy -s "+device

        os.popen(command)

        time.sleep(2)
