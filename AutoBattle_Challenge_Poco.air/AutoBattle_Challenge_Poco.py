# -*- encoding=utf8 -*-
__author__ = "zengf"

from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
import requests,json
import sys

width, height = device().get_current_resolution()
len = len(sys.argv)
deviceId=sys.argv[len-1].split("?")[1]
# deviceId = "79618bb4a50274dcfe40e7a154ea77b7"
print(deviceId)

def login(devId):
    Header = {"Content-Type": "application/json"}
    Url = "https://test-punball-v2.habby.com/internal"
    BodyData = {
    "command": 10101,
    "commonParams": {
        "platformUid": '',
        "version": 17,
        "deviceId": devId,
        "accessToken": ""
        },
    "secret": "acc2eadf31b2729a26efa8589a5dceb4"
    }
    r = requests.post(url=Url, headers=Header, json=BodyData)
    response = json.loads(r.content)
    Token = response['accessToken']
    print(Token)
    return Token

def resetChallenge(token,devId):
    Header = {"Content-Type": "application/json"}
    Url = "https://test-punball-v2.habby.com/internal"
    BodyData = {
    "command": 9003,
    "commonParams": {
        "platformUid": '',
        "version": 17,
        "deviceId": devId,
        "accessToken": token
        },
    "resType": 91,
    "resNum": 0, 
    "otherData": 0,
    "secret": "acc2eadf31b2729a26efa8589a5dceb4"
    }
    r = requests.post(url=Url, headers=Header, json=BodyData)
    
poco = UnityPoco()
direction = 'left'
for i in range(100):
    if poco("DailyModeBtn").exists():
        poco("DailyModeBtn").click()
        print('Round '+ str(i) + ':Daily Challenge')
        sleep(2)
    if poco("Button_Play").exists():
        poco("Button_Play").click()
        print('Round '+ str(i) + ':Challenge Start')
        sleep(2)
        if poco("Text_Title").exists() and poco("Text_Title").get_text() == '难度确认':
            poco("FullRoot").child("ButtonSure").child("ButtonSure").click()
            print('Round '+ str(i) + ':Challenge Confirm')
            sleep(5)
    while True:
        if poco("ChooseSkillUIPanel").exists():
            sleep(1.5)
            poco("Item0").click()
            print('Round '+ str(i) +':Select Skill')
        if poco("GameOverUIPanel").exists():
            sleep(8)
            if poco("childParent").exists():
                poco("childParent").click()
                sleep(5)
            if poco("childParent").exists():
                poco("childParent").click()
                sleep(2)
            home()
            token=login(deviceId)
            resetChallenge(token,deviceId)
            start_app("com.habby.punball")
            sleep(3)
            if poco("PiggyPurchasePanel").exists():
                poco("root").offspring("PiggyRoot").child("ButtonClose").child("ButtonClose").click()
            break
        else:
            if direction=='left':
                print('Round '+ str(i) +':Attack Left')
                touch(v=(0.11*width,0.7*height),duration=0.5)
                direction='right'
                sleep(3)
            elif direction=='right':
                print('Round '+ str(i) +':Attack Right')
                touch(v=(0.89*width,0.7*height),duration=0.5)
                direction='left'
                sleep(3)


















































