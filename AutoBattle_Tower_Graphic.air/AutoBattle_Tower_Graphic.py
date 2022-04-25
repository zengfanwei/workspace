# -*- encoding=utf8 -*-
__author__ = "zengf"

from airtest.core.api import *
import requests
import json
import sys
auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

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
# Device = "79618bb4a50274dcfe40e7a154ea77b7"
# deviceId = ""

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

    
for i in range(10):
    if exists(Template(r"tpl1649399668423.png", record_pos=(0.414, 0.645), resolution=(1080, 2400))):
        touch(Template(r"tpl1649399640777.png", record_pos=(0.398, 0.656), resolution=(1080, 2400)))
        print("点击进入副本界面！！！！！！！！！！！！！！！！！！！！")
        sleep(2)

        touch(v=(0.75*width,0.25*height))
        print("点击进入爬塔界面！！！！！！！！！！！！！！！！！！！！")
        sleep(4)

        for i in range(15):
            touch(v=(0.75*width,0.6*height))
            touch(v=(0.7*width,0.6*height))
            touch(v=(0.7*width,0.65*height))
            touch(v=(0.65*width,0.7*height))
            print("选择了Boss！！！！！！！！！！！！！！！！！！！！")
            sleep(2)
            touch(Template(r"tpl1649658942821.png", record_pos=(-0.006, 0.612), resolution=(1080, 1920)))
            print("点击挑战开始战斗！！！！！！！！！！！！！！！！！！！！")
            sleep(13)
            if exists(Template(r"tpl1649403385964.png", record_pos=(0.006, -0.394), resolution=(1080, 2400))):
                sleep(1)
                touch(v=(0.5*width,0.55*height))
                touch(v=(0.5*width,0.55*height))
                touch(v=(0.5*width,0.55*height))
                print("选择了技能！！！！！！！！！！！！！！！！！！")
                sleep(6)
            if exists(Template(r"tpl1649403385964.png", record_pos=(0.006, -0.394), resolution=(1080, 2400))):
                sleep(1)
                touch(v=(0.5*width,0.55*height))
                touch(v=(0.5*width,0.55*height))
                touch(v=(0.5*width,0.55*height))
                print("选择了技能！！！！！！！！！！！！！！！！！！")
                sleep(6)
            if exists(Template(r"tpl1649403385964.png", record_pos=(0.006, -0.394), resolution=(1080, 2400))):
                sleep(1)
                touch(v=(0.5*width,0.55*height))
                touch(v=(0.5*width,0.55*height))
                touch(v=(0.5*width,0.55*height))
                print("选择了技能！！！！！！！！！！！！！！！！！！")
                sleep(6)
            
            if addattack > 0:
                touch(Template(r"tpl1649933503543.png", record_pos=(0.429, -0.818), resolution=(1080, 1920)))
                sleep(2)
                hh = 0.73
                ww = 0.33
                for i in range(8):
                    touch(v=(ww*width,hh*height))
                    touch(v=(ww*width,hh*height))
                    hh -= 0.01
                    ww += 0.001
                    sleep(1)
                    if exists(Template(r"tpl1649934325086.png", record_pos=(-0.006, 0.645), resolution=(1080, 2400))):
                        break
                att = str(addattack * 100000)
                touch(v=(0.5*width,0.37*height))
                if deviceId == "1d38177047b1a9f375aca9e7eaa4b035":
                    text("")
                    text(att)
                else:
                    poco("android.widget.EditText").set_text(att)
                touch(v=(0.8*width,0.37*height))
                sleep(1)
                touch(v=(0.8*width,0.365*height))
                sleep(1)
                touch(Template(r"tpl1649934802625.png", record_pos=(-0.421, 0.672), resolution=(1080, 2400)))
                sleep(1)
            while exists(Template(r"tpl1649403511947.png", record_pos=(0.276, -0.979), resolution=(1080, 2400))):
                if direction:
                    touch(v=(0.16*width, 0.8*height), duration=0.5)
                    print("发射！！！！！！！！！！！！！！！！！！")
                if not direction:
                    touch(v=(0.84*width, 0.8*height), duration=0.5)
                    print("发射！！！！！！！！！！！！！！！！！！")
                direction = not direction
                sleep(4)
                
            if exists(Template(r"tpl1650009331442.png", record_pos=(-0.018, 0.303), resolution=(1080, 1920))):
                sleep(2)
                touch(v=(0.5*width, 0.8*height))
                print("关闭失败结算界面！！！！！！！！！！！！！！！！！")
                sleep(2)
                addattack += 1
                
            if exists(Template(r"tpl1649933274888.png", record_pos=(0.003, -0.127), resolution=(1080, 1920))):
                sleep(2)
                touch(v=(0.5*width, 0.8*height))
                print("关闭结算界面！！！！！！！！！！！！！！！！！")
                sleep(2)
                addattack = 0

            if exists(Template(r"tpl1649404621203.png", record_pos=(0.19, -0.086), resolution=(1080, 2400))):
                sleep(2)
                touch(v=(0.5*width, 0.8*height))
                print("关闭奖励界面！！！！！！！！！！！！！！！！！")
                sleep(2)

            if exists(Template(r"tpl1649405268902.png", record_pos=(-0.373, 0.781), resolution=(1080, 2400))):
                sleep(2)
                touch(Template(r"tpl1649405288491.png", record_pos=(-0.369, 0.783), resolution=(1080, 2400)))
                print("点击放弃卡牌！！！！！！！！！！！！！！！！！")
                sleep(2)

        if exists(Template(r"tpl1649406330954.png", record_pos=(-0.416, 1.008), resolution=(1080, 2400))):
            touch(Template(r"tpl1649406345352.png", record_pos=(-0.416, 1.011), resolution=(1080, 2400)))
            sleep(3)
        if exists(Template(r"tpl1649406373289.png", record_pos=(-0.405, 0.657), resolution=(1080, 2400))):
            touch(Template(r"tpl1649406383255.png", record_pos=(-0.405, 0.665), resolution=(1080, 2400)))
            sleep(3)
        home()
        login(deviceId)
        add_dailytime()
        start_app("com.habby.punball")
        sleep(2)







    




    




