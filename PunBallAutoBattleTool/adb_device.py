# -*- coding: utf-8 -*-
# @Path : C:\Users\zengf\AppData\Local\Programs\Python\Python39
# @Time : 2022/5/1 19:31
# @Author : zengf
# @Email : 944458157@qq.com
# @File : adb_device.py
# @Project : workspace


import os
import re
import json
from config import STF1, STF2, TOKEN, URL, CONNECT1, CONNECT2, CONNECT3, SerialNumber, DisCONNECT


def rentDevices():
    deviceIp = {}
    for serial, dev in SerialNumber.items():
        rent = STF1 + serial + STF2 + TOKEN + URL
        # print(rent)
        connect = CONNECT1 + TOKEN + URL + CONNECT2 + serial + CONNECT3
        # print(connect)
        with os.popen(rent) as p:
            text = p.read()
            print("rent: ", type(text), text)
            if '"success":true' not in text:
                print("设备：{0}租用失败！！！！！".format(dev))
        with os.popen(connect) as pp:
            text = pp.read()
            print("connect: ", type(text), text)
            if '"success":true' not in text:
                print("设备：{0}链接失败！！！！！".format(dev))
            else:
                data = json.loads(text)
                deviceIp[dev] = data["remoteConnectUrl"]
    # print(deviceIp)
    return deviceIp


def disrentDevices():
    for serial, dev in SerialNumber.items():
        disrent = DisCONNECT + TOKEN + URL + CONNECT2 + serial
        print(disrent)
        with os.popen(disrent) as pp:
            text = pp.read()
            print("disrent: ", type(text), text)
            if '"success":true' not in text:
                print("设备：{0}取消租用失败！！！！！".format(dev))


def getDevices():
    cmd = 'adb devices'
    with os.popen(cmd) as p:
        text = p.read()
    #    print "text: ", type(text), text

    info = text.replace('List of devices attached', '').strip('\n')
    p = r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?):\d{4,5}$"

    if '' == info:
        return "没有检测到设备！(0)"
    elif re.match(p, info.split("\t")[0]):
        deviceList = info.split('\n')
        return deviceList
    else:
        return text


def connectDevice(ip_port):
    """
    adb连接设备
    :param newDevInfo: str，新设备的 ip:端口
    :return:(bool, str)
    """

    cmd_command = 'adb connect ' + ip_port
    with os.popen(cmd_command) as p:
        text = p.read()

    # 通过json配置文件，获取设备名称
    ipPort_deviceName_dict = getDataFromCof()
    #    print type(ipPort_deviceName_dict)

    device_name = ''
    if ip_port in ipPort_deviceName_dict.keys():
        device_name = ipPort_deviceName_dict[ip_port]

    # 判断连接是否成功
    str = 'connected to ' + ip_port + '\n'
    if text == str:
        return (True, "设备连接成功: %s" % device_name)
    else:
        return (False, text + device_name)


def refreshDevices():
    '''
    获取已连接adb设备信息，刷新工具栏
    return: 如果有设备连接，返回设备信息[(ip_port, state, name)......]；否则返回str
    '''
    cmd_command = 'adb devices'
    with os.popen(cmd_command) as p:
        text = p.read()

    info = text.replace('List of devices attached', '').strip('\n')
    p = r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?):\d{4,5}$"

    if '' == info:  # 没有设备连接
        return "没有检测到设备！(0)"
    elif re.match(p, info.split("\t")[0]):  # 有设备连接
        deviceList = info.split('\n')
        stateList = []
        for device in deviceList:
            ip_port, state = device.split("\t")

            # 通过json配置文件，获取设备名称
            ipPort_deviceName_dict = getDataFromCof()
            name = ipPort_deviceName_dict.get(ip_port, "UnknownDevice")
            if name == "UnknownDevice":
                print("发现未知设备:", ip_port)

            tup = (ip_port, state, name)
            stateList.append(tup)

        #        print "adb_device.py - type(stateList), stateList: ", type(stateList), stateList
        return stateList
    else:
        return text


'''
# 获取运行设备的LOG信息
def getDeviceLog():
    onlineDevicesList = refreshDevices()
    for i in onlineDevicesList:
        if 'device' == i[1]:
            ip = i[0]
            deviceName = i[2]
            #获取当前的进程id
            cmd1 = 'adb -s ' + ip + ' shell "ps | grep com.happyelements.TsumTsumAndroid"'
            processText = os.popen(cmd1)
            process = processText.read()
            infoList = process.split('\n')
            allpid = []
            for info in infoList:
                pidList = info[13:].split(' ')
                allpid.append(pidList[0])
            pid = ''
            #将应用的多个PID的log都输出到LOG_PATH本地
            for tsumPid in allpid:
                if '' != tsumPid:
                    pid = pid + '-e '+ tsumPid + ' '
            cmd2 = 'adb -s ' + ip + ' shell "logcat -d | grep ' + pid + '" > ' + LOG_PATH + deviceName + '.txt'
            os.system(cmd2)
'''

if __name__ == '__main__':
    # devs = refreshDevices()
    rentDevices()
