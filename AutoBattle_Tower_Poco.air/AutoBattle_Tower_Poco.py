# -*- encoding=utf8 -*-
__author__ = "zengf"

import random
from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
import requests
import json
import sys
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
apoco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
poco = UnityPoco()
using("add.air")
from add import login, del_skills, addResource, de_skill, SkillsList

width, height = device().get_current_resolution()
direction = True
addattack = 0
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
len = len(sys.argv)
deviceId = sys.argv[len-1].split("?")[1]
# deviceId = "79618bb4a50274dcfe40e7a154ea77b7"
# deviceId = ""
sk = ['7001020', '7002020', '7003020', '7004020', '7005020', '7006020', '7007020', '7008020', '7009020', '7010020', '7101020']
login(deviceId)
del_skills()
for i in sk:
    addResource(i, '1', '1')
de_skill(deviceId, random.sample(SkillsList, 3))
home()
start_app("com.habby.punball")
useSkill = False

def login(devId):
    global Token
    BodyData.update({"command": 10101})
    BodyData['commonParams']['deviceId'] = devId
    r = requests.post(url=Url, headers=Header, json=BodyData)
    response = json.loads(r.content)
    print(response)
    Token = response['accessToken']

def add_dailytime(time=0):
    global Token
    BodyData.update({"command": 9003, "resType": 132, "itemId": 1010001, "resNum": time, "otherData": time, "accessToken": Token})
    r = requests.post(url=Url, headers=Header, json=BodyData)
    response = json.loads(r.content)
    print(response)

    
for i in range(100):
    if poco("DailyActiveChange").exists():
        poco("DailyActiveChange").click()
        print("点击进入副本界面！！！！！！！！！！！！！！！！！！！！")
        sleep(3)
    if poco(text="进入试炼").exists():
        pos = poco(text="进入试炼").get_position()
        pos[1] = pos[1] + 0.01
        poco.click(pos)
        print("点击进入爬塔界面！！！！！！！！！！！！！！！！！！！！")
        sleep(3)
    for i in range(12):
        poco("TowerMapUIPanel(Clone)").child("root").child("root").offspring("Container").child("TowerRoomItem(Clone)")[2].offspring("roomCurrentLayerNode").child("bossPos_1").click()    
        print("选择了Boss！！！！！！！！！！！！！！！！！！！！")
        sleep(1)
        poco("challengeBtn").click()
        print("点击挑战开始战斗！！！！！！！！！！！！！！！！！！！！")
        sleep(1)
        if poco("Tips_UI_Normal(Clone)").exists():
            poco("TowerMapUIPanel(Clone)").child("root").child("root").offspring("Container").child("TowerRoomItem(Clone)")[3].offspring("roomCurrentLayerNode").child("bossPos_1").click()
            sleep(1)
            poco("challengeBtn").click()
            print("点击挑战开始战斗！！！！！！！！！！！！！！！！！！！！")
            sleep(1)
        sleep(10)
        
        if poco("ChooseSkillUIPanel").exists():
            sleep(3)
            poco("Item0").click()
            print('Round '+ str(i) +':Select Skill')
            sleep(2)
        if poco("ChooseSkillUIPanel").exists():
            sleep(3)
            poco("Item0").click()
            print('Round '+ str(i) +':Select Skill')
            sleep(2)
        if poco("ChooseSkillUIPanel").exists():
            sleep(3)
            poco("Item0").click()
            print('Round '+ str(i) +':Select Skill')
            sleep(2)

        if not useSkill:
            time = 0
            while poco("Panel").child("SkillTemplate(Clone)")[0].exists():
                poco("Panel").child("SkillTemplate(Clone)")[0].child("Skill").click()
                sleep(1)
                if poco("Cancel").exists():
                    poco("Mask(Clone)").click()
                    sleep(1)
                    if poco("Cancel").exists():
                        pospos = poco("Mask(Clone)").get_position()
                        pospos[0] = pospos[0] + 0.1
                        poco.click(pospos)
                    time += 1
                if time == 3:
                    break
            useSkill = True
        
        if addattack > 0:
            while not poco("PauseUIPanel(Clone)").exists():
                pp = poco("Button_Pause").get_position()
                pp[1] = pp[1] + 0.03
                poco.click(pp)
                sleep(1)
            poco("Button_Test").click()
            att = str(addattack * 100000)
            touch(v=(0.5*width,0.37*height))
#             if deviceId == "1d38177047b1a9f375aca9e7eaa4b035":
#                 text("")
#                 text(att)
#             else:
#                 apoco("android.widget.EditText").set_text(att)
            apoco("android.widget.EditText").set_text(att)
            poco("ScrollView_Game").child("Viewport").offspring("AtkSetting").offspring("BtnSetDevice").click()
            sleep(1)
            poco("Button_Close").click()
            sleep(1)

        while poco("Button_SpeedUp").exists():
            if direction:
                touch(v=(0.16*width, 0.8*height), duration=0.5)
                print("发射！！！！！！！！！！！！！！！！！！")
            if not direction:
                touch(v=(0.84*width, 0.8*height), duration=0.5)
                print("发射！！！！！！！！！！！！！！！！！！")
            direction = not direction
            sleep(5)
            
        if poco("ImageTitleFail").exists():
            sleep(3)
            poco("TextClose").click()
            print("关闭失败结算界面！！！！！！！！！！！！！！！！！")
            sleep(2)
            addattack += 1

        if poco("ImageTitleWin").exists():
            sleep(4)
            poco("childParent").click()
            print("关闭结算界面！！！！！！！！！！！！！！！！！")
            sleep(3)
            addattack = 0

        if poco("CommonRewardUIPanel").exists():
            sleep(3)
            poco("Text_TapToClose").click()
            print("关闭奖励界面！！！！！！！！！！！！！！！！！")
            sleep(2)
            
        if poco("TowerSkillSelectPanel").exists():
            sleep(3)
            poco("Button_giveup").click()
            print("点击放弃卡牌！！！！！！！！！！！！！！！！！")
            sleep(2)
            
        home()
        de_skill(deviceId, random.sample(SkillsList, 3))
        start_app("com.habby.punball")
        sleep(2)
        useSkill = False
        
    if poco("IconBack").exists():
        poco("IconBack").click()
        sleep(2)
    if poco("BackBtnRoot").exists():
        poco("BackBtnRoot").click()
        sleep(3)
    home()
    login(deviceId)
    add_dailytime()
    start_app("com.habby.punball")
    sleep(2)


