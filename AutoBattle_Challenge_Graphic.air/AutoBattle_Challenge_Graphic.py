# -*- encoding=utf8 -*-
__author__ = "stars"

from airtest.core.api import *
import requests,json
import sys

auto_setup(__file__)
width, height = device().get_current_resolution()
Looptime=100
direction='left'
# vivo X30 deviceID
len = len(sys.argv)
deviceId=sys.argv[len-1].split("?")[1]
# 'd83628c469a24fedd02bfaac5c5ff28d'

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


LoopNow=0
for i in range(Looptime):
    LoopNow+=1
    #主界面#
    if exists(Template(r"tpl1648805401601.png", record_pos=(-0.394, 0.642), resolution=(1440, 3040))):
        touch(Template(r"tpl1648805401601.png", record_pos=(-0.394, 0.642), resolution=(1440, 3040)))
        print('Round '+ str(LoopNow) + ':Daily Challenge')
        sleep(2)
    
    if exists(Template(r"tpl1648805526117.png", record_pos=(0.001, 0.654), resolution=(1440, 3040))):
        touch(Template(r"tpl1648805526117.png", record_pos=(0.001, 0.654), resolution=(1440, 3040)))
        print('Round '+ str(LoopNow) + ':Challenge Start')
        sleep(2)
        if exists(Template(r"tpl1648805749875.png", record_pos=(-0.002, 0.066), resolution=(1440, 3040))):
            print('Round '+ str(LoopNow) + ':Challenge Confirm')
            if exists(Template(r"tpl1648805770254.png", record_pos=(0.182, 0.333), resolution=(1440, 3040))):
                touch(Template(r"tpl1648805770254.png", record_pos=(0.182, 0.333), resolution=(1440, 3040)))
                sleep(5)
            
        while True:
            #选择技能#    
            if exists(Template(r"tpl1648782461084.png", record_pos=(-0.002, -0.488), resolution=(1080, 2220))):
                print('Round '+ str(LoopNow) +':Select Skill')
                touch(v=(0.45*width,0.55*height))
                sleep(5)

            #开始战斗#
            if exists(Template(r"tpl1649231601152.png", record_pos=(-0.43, -0.951), resolution=(1080, 2400))):
                if direction=='left':
                    print('Round '+ str(LoopNow) +':Attack Left')
                    touch(v=(0.11*width,0.7*height),duration=0.5)
                    direction='right'
                    sleep(3)
                elif direction=='right':
                    print('Round '+ str(LoopNow) +':Attack Right')
                    touch(v=(0.89*width,0.7*height),duration=0.5)
                    direction='left'
                    sleep(3)

            #结算#
            if exists(Template(r"tpl1648783312509.png", record_pos=(-0.003, -0.011), resolution=(1080, 2220))):
                print('Round '+ str(LoopNow) +':Battle finish')
                sleep(5)
                touch(v=(0.5*width,0.98*height))
                print('Round '+ str(LoopNow) +':touch screen1')
                sleep(5)
                touch(v=(0.5*width,0.98*height))
                print('Round '+ str(LoopNow) +':touch screen2')
                token=login(deviceId)
                resetChallenge(token,deviceId)
                sleep(8)
                keyevent("HOME")
                sleep(3)
                touch(Template(r"tpl1649215287398.png", record_pos=(-0.119, -0.773), resolution=(1080, 2400)))
                sleep(2)
                touch(Template(r"tpl1649215393909.png", record_pos=(-0.255, 1.018), resolution=(1080, 2400)))
                sleep(2)
                touch(Template(r"tpl1649215410684.png", record_pos=(0.081, 1.018), resolution=(1080, 2400)))
                sleep(2)
                break
                