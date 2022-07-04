# -*- encoding=utf8 -*-
__author__ = "zengf"

from airtest.core.api import *

import requests
import json
import random

#  三星Note8 | 三星S10 | OnePlus9 | Realme GT Neo | 三星A51 | huwei Nova 3 | vivo U3 | vivo X30
Devices = ["9053d2ab125149be768598130a580500", "c32afe8bca31f210307c221ed52ed4ca", "fd2b61f64d569ea41f8c574e0eae43d1",
           "d2605d1fa969ee7a8b7aa8fb43aa2ebc", "1d38177047b1a9f375aca9e7eaa4b035", "f5c481ee2c07ca9259265527e06fb503",
           "60097f25edf34cb659d42e871ba620fa", "d83628c469a24fedd02bfaac5c5ff28d", "9e1031012d3607b6e9028c4948668511"]
# Devices = ["79618bb4a50274dcfe40e7a154ea77b7"]
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
SkillsList = []


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


def de_card(devId, cards):
    BodyData.update({"command": 12507})
    BodyData['commonParams']['deviceId'] = devId
    BodyData['selectSkillIds'] = cards
    BodyData['isGiveUp'] = False
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


def de_skill(devId, rowid):
    BodyData.update({"command": 12803})
    BodyData['commonParams']['deviceId'] = devId
    BodyData['rowIds'] = rowid
    r = requests.post(url=Url, headers=Header, json=BodyData)
    response = json.loads(r.content)
    print(response)


def addResource(item, num, level):
    global Token, Equips, Pets, SkillsList
    BodyData.update({"command": 9003, "resType": 3, "itemId": item, "resNum": num, "otherData": level, "accessToken": Token})
    r = requests.post(url=Url, headers=Header, json=BodyData)
    response = json.loads(r.content)
    # {'code': 0, 'commonData': {'reward': [{'configId': 7001020, 'count': 1, 'type': 7}],
    #                            'artifacts': [{'artifactId': 7001020, 'rowId': '264'}]}}
    if 'equipment' in response['commonData'].keys():
        Equips.append(response['commonData']['equipment'][0]['rowId'])
    if 'pets' in response['commonData'].keys():
        Pets.append(response['commonData']['pets'][0]['rowId'])
    if 'artifacts' in response['commonData'].keys():
        SkillsList.append(response['commonData']['artifacts'][0]['rowId'])
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


def add_dailytime(time=0):
    global Token
    BodyData.update({"command": 9003, "resType": 91, "itemId": 1010001, "resNum": time, "otherData": time, "accessToken": Token})
    r = requests.post(url=Url, headers=Header, json=BodyData)
    response = json.loads(r.content)
    print(response)


def del_skills():
    global Token
    BodyData.update({"command": 9003, "resType": 157, "itemId": 1010001, "resNum": 1, "otherData": 1, "accessToken": Token})
    r = requests.post(url=Url, headers=Header, json=BodyData)
    response = json.loads(r.content)
    print(response)


def towerchapter(time=150):
    global Token
    BodyData.update({"command": 9003, "resType": 135, "itemId": 1010001, "resNum": time, "otherData": time, "accessToken": Token})
    r = requests.post(url=Url, headers=Header, json=BodyData)
    response = json.loads(r.content)
    print(response)


def towercard(time=4):
    global Token
    BodyData.update({"command": 9003, "resType": 145, "itemId": 1010001, "resNum": time, "otherData": time, "accessToken": Token})
    r = requests.post(url=Url, headers=Header, json=BodyData)
    response = json.loads(r.content)
    print(response)


def add_towertime(time=0):
    global Token
    BodyData.update({"command": 9003, "resType": 132, "itemId": 1010001, "resNum": time, "otherData": time, "accessToken": Token})
    r = requests.post(url=Url, headers=Header, json=BodyData)
    response = json.loads(r.content)
    print(response)

def removeequipment():
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
