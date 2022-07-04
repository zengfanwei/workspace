# -*- coding: utf-8 -*-
# @Path : C:\Users\zengf\AppData\Local\Programs\Python\Python39
# @Time : 2022/5/1 21:59
# @Author : zengf
# @Email : 944458157@qq.com
# @File : study.py
# @Project : workspace
# import paramiko
#
# ##1.创建一个ssh对象
# client = paramiko.SSHClient()
#
# #2.解决问题:如果之前没有，连接过的ip，会出现选择yes或者no的操作，
# ##自动选择yes
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# # client.load_system_host_keys()
#
# #3.连接服务器
# client.connect(hostname='172.16.18.219', port=22, username="HabbyQA", password="habby2019", allow_agent=False, look_for_keys=False)
#
# #4.执行操作
# stdin,stdout, stderr = client.exec_command('airtest run D:/airtest-case/Punball/AutoBattle_Main_Graphic.air --device Android:///172.16.18.94:7433')
# print(stdin)
# print(stdout)
# print(stderr)
# #5.获取命令执行的结果
# result = stdout.read().decode('utf-8')
# print(result)
# # if stderr.read() == b'':        # 没有发生错误
# #     for line in stdout.readlines():
# #         print(line.strip())
# # else:
# #     print(stderr.read())
#
# #6.关闭连接
# client.close()
from config import SerialNumber, ComPORT, ComIP, ComPASSWORD, ComUSERNAME
from adb_device import rentDevices
import time
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
        stdin, stdout, stderr = self.client.exec_command(self.cmd, get_pty=True)
        return stdin, stdout, stderr

    def stop(self):
        self.client.close()

if __name__ == '__main__':
    # hhhh = remote_control(
    #     'airtest run D:/airtest-case/Punball/AutoBattle_Main_Graphic.air --device Android:///172.16.18.94:7433')
    # vvvv = remote_control(
    #     'airtest run D:/airtest-case/Punball/AutoBattle_Main_Graphic.air --device Android:///172.16.18.94:7401')
    # hhhh.run()
    # vvvv.run()
    # time.sleep(30)
    # hhhh.stop()
    # vvvv.stop()
    ls = remote_control('python -h')
    text = ls.run()[1]
    dirs = []
    result = text.read().decode()
    # text = ls.run()
    # dirs = []
    # result = text.read().decode("gbk").encode("utf-8").decode()
    # # print(text.read().decode("gbk").encode("utf-8").decode())
    # for d in result.split("\r\n"):
    #     print(d)
    #     if 'AutoBattle' in d:
    #         dirs.append(d.split("          ")[1])
    # print(dirs)
