# -*- coding: utf-8 -*-
# @Path : C:\Users\zengf\AppData\Local\Programs\Python\Python39
# @Time : 2022/7/6 10:55
# @Author : zengf
# @Email : 944458157@qq.com
# @File : SSH.py
# @Project : workspace
import paramiko
from config import ComPORT, ComIP, ComPASSWORD, ComUSERNAME


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
        # print(stdin)
        # print(stdout)
        # print(stderr)
        return stdin, stdout, stderr

    def stop(self):
        self.client.close()