# -*- coding: utf-8 -*-
# @Path : C:\Users\zengf\AppData\Local\Programs\Python\Python39
# @Time : 2022/4/1 15:20
# @Author : zengf
# @Email : 944458157@qq.com
# @File : add.py
# @Project : workspace

import requests
import json

#  三星Note8 | 三星S10 | OnePlus9 | Realme GT Neo | 三星A51 90005384
Devices = ["9053d2ab125149be768598130a580500", "c32afe8bca31f210307c221ed52ed4ca", "fd2b61f64d569ea41f8c574e0eae43d1",
           "d2605d1fa969ee7a8b7aa8fb43aa2ebc", "1d38177047b1a9f375aca9e7eaa4b035", "04be64cf743b1215baea75187663bfa1",
           "60097f25edf34cb659d42e871ba620fa"]
# Devices = ["fd2b61f64d569ea41f8c574e0eae43d1"]
Version = 17
Header = {"Content-Type": "application/json"}
Url = "https://test-punball-v2.habby.com/internal"
Token = ""
Platform = ""
BodyData = {
    "command": 0,
    "commonParams": {
        "platformUid": Platform,
        "version": Version,
        "deviceId": "",
        "accessToken": ""
    },
    "secret": "acc2eadf31b2729a26efa8589a5dceb4",
}
SignInUrl = "https://wiki-punball.habby.com/login?serverIdx=0&userId=9999999"
Headers = {
  'Cookie': 'connect.sid=s%3AVte8CShCo4eHXNmxI9p0Ai4r-yhcinqR.fzOHOUsjTTBG2wa8AeIdttifi1%2FshhPRhlAoFq1Huow'
}
Equips = []
Pets = []


def login(devId):
    global Token
    BodyData.update({"command": 10101})
    BodyData['commonParams']['deviceId'] = devId
    r = requests.post(url=Url, headers=Header, json=BodyData)
    response = json.loads(r.content)
    print(response)
    Token = response['accessToken']


def de_equip(devId, rowid):
    BodyData.update({"command": 10305})
    BodyData['commonParams']['deviceId'] = devId
    BodyData['rowIds'] = rowid
    r = requests.post(url=Url, headers=Header, json=BodyData)
    response = json.loads(r.content)
    print(response)


def de_pet(devId, rowid):
    BodyData.update({"command": 12005})
    BodyData['commonParams']['deviceId'] = devId
    BodyData['rowIds'] = rowid
    r = requests.post(url=Url, headers=Header, json=BodyData)
    response = json.loads(r.content)
    print(response)


def addResource(item, num, level):
    global Token, Equips, Pets
    BodyData.update({"command": 9003, "resType": 3, "itemId": item, "resNum": num, "otherData": level, "accessToken": Token})
    r = requests.post(url=Url, headers=Header, json=BodyData)
    response = json.loads(r.content)
    if 'equipment' in response['commonData'].keys():
        Equips.append(response['commonData']['equipment'][0]['rowId'])
    if 'pets' in response['commonData'].keys():
        Pets.append(response['commonData']['pets'][0]['rowId'])
    print(response)


def change_chapter(chapter):
    global Token
    BodyData.update({"command": 9003, "resType": 4, "itemId": 1010001, "resNum": chapter, "otherData": chapter, "accessToken": Token})
    r = requests.post(url=Url, headers=Header, json=BodyData)
    response = json.loads(r.content)
    print(response)


def change_level(level):
    global Token
    BodyData.update({"command": 9003, "resType": 19, "itemId": 1010001, "resNum": level, "otherData": level, "accessToken": Token})
    r = requests.post(url=Url, headers=Header, json=BodyData)
    response = json.loads(r.content)
    print(response)


def change_talent_small(talent):
    global Token
    BodyData.update({"command": 9003, "resType": 72, "itemId": 1010001, "resNum": talent, "otherData": talent, "accessToken": Token})
    r = requests.post(url=Url, headers=Header, json=BodyData)
    response = json.loads(r.content)
    print(response)


def change_talent_big(talent):
    global Token
    BodyData.update({"command": 9003, "resType": 73, "itemId": 1010001, "resNum": talent, "otherData": talent, "accessToken": Token})
    r = requests.post(url=Url, headers=Header, json=BodyData)
    response = json.loads(r.content)
    print(response)


def removeequipment():  # ET /addResource?serverIdx=0&resType=119&resNum=1&itemId=1010001&otherData=1 HTTP/1.1
    global Token
    BodyData.update({"command": 9003, "resType": 59, "itemId": 1020001, "resNum": 1, "otherData": 1, "accessToken": Token})
    r = requests.post(url=Url, headers=Header, json=BodyData)
    response = json.loads(r.content)
    print(response)


def removepet():
    global Token
    BodyData.update({"command": 9003, "resType": 119, "itemId": 1010001, "resNum": 1, "otherData": 1, "accessToken": Token})
    r = requests.post(url=Url, headers=Header, json=BodyData)
    response = json.loads(r.content)
    print(response)


if __name__ == '__main__':
    level = '120'
    small = '250'
    big = '30'
    equiplevel = '220'
    petlevel = '100'
    chapter = '1091'
    equipid = ['3010120', '3020120', '3030120', '3040120', '3050120', '3060120']
    petid = ['4012114', '4021114', '4031114']
    for d in Devices:
        login(d)  # 登录
        de_equip(d, [])  # 脱装备
        de_pet(d, [])  # 脱宠物
        removeequipment()  # 删除装备
        removepet()  # 删除宠物
        for e in equipid:  # 添加装备
            addResource(e, '1', equiplevel)
        de_equip(d, Equips)  # 穿装备
        for p in petid:  # 添加宠物
            addResource(p, '1', petlevel)
        de_pet(d, Pets)  # 上阵宠物
        addResource('1040001', '900', 0)  # 添加体力
        addResource('1050004', '50', 0)  # 添加挑战券
        change_chapter(chapter)  # 修改章节
        change_level(level)
        change_talent_small(small)
        change_talent_big(big)
        Equips = []
        Pets = []

