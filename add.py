# -*- coding: utf-8 -*-
# @Path : C:\Users\zengf\AppData\Local\Programs\Python\Python39
# @Time : 2022/4/1 15:20
# @Author : zengf
# @Email : 944458157@qq.com
# @File : add.py
# @Project : workspace

import requests
import json
import random

#  三星Note8 | 三星S10 | OnePlus9 | Realme GT Neo | 三星A51 | huwei Nova 3 | vivo U3 | vivo X30
Devices = ["9053d2ab125149be768598130a580500", "c32afe8bca31f210307c221ed52ed4ca", "fd2b61f64d569ea41f8c574e0eae43d1",
           "d2605d1fa969ee7a8b7aa8fb43aa2ebc", "1d38177047b1a9f375aca9e7eaa4b035", "f5c481ee2c07ca9259265527e06fb503",
           "60097f25edf34cb659d42e871ba620fa", "d83628c469a24fedd02bfaac5c5ff28d", "9e1031012d3607b6e9028c4948668511"]
# Devices = ["79618bb4a50274dcfe40e7a154ea77b7"]
# Devices = ["fd2b61f64d569ea41f8c574e0eae43d1", "60097f25edf34cb659d42e871ba620fa",
#            "1d38177047b1a9f375aca9e7eaa4b035", "f5c481ee2c07ca9259265527e06fb503"]
# Devices = ["9e1031012d3607b6e9028c4948668511"]
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


if __name__ == '__main__':
    level = '120'
    small = '250'
    big = '30'
    equiplevel = '220'
    petlevel = '100'
    chapter = '1141'
    skills = ['7001020', '7002020', '7003020', '7004020', '7005020', '7006020', '7007020', '7008020', '7009020', '7010020', '7101020']
    equip1 = ['3010120', '3010220', '3010320', '3010420']
    equip2 = ['3020120', '3020220', '3020320', '3020420']
    equip3 = ['3030120', '3030220', '3030320', '3030420']
    equip4 = ['3040120', '3040220', '3040320', '3040420']
    equip5 = ['3050120', '3050220', '3050320', '3050420']
    equip6 = ['3060120', '3060220', '3060320', '3060420']
    # equipsss = {0:['3010520', '3020520', '3040120', '3030120', '3050120', '3060120'],
    #           1:['3010520', '3020520', '3040220', '3030220', '3050220', '3060220'],
    #           2:['3010520', '3020520', '3040320', '3030320', '3050320', '3060320'],
    #           3:['3010520', '3020520', '3040420', '3030420', '3050420', '3060420'],
    #           4:['3010520', '3020520', '3040320', '3030120', '3050320', '3060420'],
    #           5:['3010520', '3020520', '3040220', '3030420', '3050220', '3060320'],
    #           6:['3010520', '3020520', '3040420', '3030220', '3050120', '3060220'],
    #           7: ['3010520', '3020520', '3040120', '3030320', '3050420', '3060120']}
    equipsss = {0:['3010420', '3020120', '3040120', '3030320', '3050420', '3060120'],
              1:['3010120', '3020320', '3040120', '3030220', '3050320', '3060420'],
              2:['3010320', '3020120', '3040220', '3030120', '3050120', '3060220'],
              3:['3010420', '3020220', '3040320', '3030420', '3050220', '3060320'],
              4:['3010220', '3020420', '3040420', '3030320', '3050420', '3060120'],
              5:['3010320', '3020220', '3040220', '3030420', '3050320', '3060420'],
              6:['3010120', '3020320', '3040320', '3030220', '3050320', '3060420'],
              7: ['3010220', '3020220', '3040420', '3030220', '3050120', '3060220']}
    card = ["6000104","6000204","6000304","6000404","6000504","6000604","6000704","6000804","6000904","6001004","6001104","6001204","6001304","6001404","6001504","6001604","6001704","6001804","6001904","6002004","6002104","6002204","6002304","6002404","6002504","6002604","6002704","6002804","6002904","6003004","6003104","6003204","6003304","6003404","6003504","6003604","6003704","6003804","6003904","6004004","6004104","6004204","6004304","6004404"]
    pets = ['4010114', '4010214', '4010314', '4011114', '4011214', '4020114', '4020214', '4020314', '4021114', '4021214',
            '4030114', '4030214', '4030314', '4031114', '4031214', '4040114', '4040214', '4040314', '4041114', '4041214', "4012114", "4032114"]
    pettt = {0:['4012114', '4021114', '4031114'],
             1:['4011114', '4021214', '4031214'],
             2:['4011214', '4020114', '4041114'],
             3:['4010114', '4020214', '4041214'],
             4:['4010214', '4030314', '4040114'],
             5:['4010314', '4030114', '4040214'],
             6:['4020314', '4030214', '4040314'],
             7:['4040214', '4031214', '4040114']}
    # pettt = {0:['4040214', '4031214', '4040114'],
    #          1:['4010214', '4041114', '4030214'],
    #          2:['4020114', '4010114', '4020214'],
    #          3:['4011214', '4040314', '4011114'],
    #          4:['4020314', '4021214', '4041214'],
    #          5:['4010314', '4031114', '4030314'],
    #          6:['4012114', '4021114', '4030114'],
    #          7:['4011114', '4021214', '4031214']}
    # for d in range(len(Devices)):
    #     login(Devices[d])  # 登录
    #     de_equip(Devices[d], [])  # 脱装备
    #     de_pet(Devices[d], [])  # 脱宠物
    #     removeequipment()  # 删除装备
    #     removepet()  # 删除宠物
    #     addResource(random.sample(equip1, 1)[0], '1', equiplevel)
    #     addResource(random.sample(equip2, 1)[0], '1', equiplevel)
    #     addResource(random.sample(equip4, 1)[0], '1', equiplevel)
    #     addResource(random.sample(equip3, 1)[0], '1', equiplevel)
    #     addResource(random.sample(equip5, 1)[0], '1', equiplevel)
    #     addResource(random.sample(equip6, 1)[0], '1', equiplevel)
    #     de_equip(Devices[d], Equips)  # 穿装备
    #     for p in random.sample(pets, 3):  # 添加宠物
    #         addResource(p, '1', petlevel)
    #     de_pet(Devices[d], Pets)  # 上阵宠物
    #     addResource('1040001', '9000', 0)  # 添加体力
    #     addResource('1050004', '500', 0)  # 添加挑战券
    #     change_chapter(chapter)  # 修改章节
    #     change_level(level)
    #     change_talent_small(small)
    #     change_talent_big(big)
    #     add_dailytime()
    #     towerchapter()
    #     towercard()
    #     add_towertime()
    #     de_card(Devices[d], random.sample(card, 10))
    #     Equips = []
    #     Pets = []
    for d in range(len(Devices)):
        login(Devices[d])  # 登录
        # de_equip(Devices[d], [])  # 脱装备
        # de_pet(Devices[d], [])  # 脱宠物
        # removeequipment()  # 删除装备
        # removepet()  # 删除宠物
        # del_skills()
        # for i in equipsss[d]:
        #     addResource(i, '1', equiplevel)
        # de_equip(Devices[d], Equips)  # 穿装备
        # for j in pettt[d]:
        #     # for j in ["4020314", "4012114", "4032114"]:
        #     addResource(j, '1', petlevel)
        # de_pet(Devices[d], Pets)  # 上阵宠物
        # for s in skills:
        #     addResource(s, '1', '1')
        # de_skill(Devices[d], random.sample(SkillsList, 3))
        # addResource('1040001', '9000', 0)  # 添加体力
        # addResource('1050004', '500', 0)  # 添加挑战券
        change_chapter(chapter)  # 修改章节
        # change_level(level)
        # change_talent_small(small)
        # change_talent_big(big)
        # add_dailytime()
        # towerchapter()
        # towercard()
        # add_towertime()
        # de_card(Devices[d], random.sample(card, 10))
        # # de_card(Devices[d], [6001504,6000204,6000304,6000704,6003404,6003504,6002004,6003304,6002204,6000104])
        # Equips = []
        # Pets = []


