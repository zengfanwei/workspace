# -*- encoding=utf8 -*-
__author__ = "stars"

import random
from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
import time

poco = UnityPoco()
using("add.air")
from add import login, del_skills, addResource, de_skill, SkillsList
poco.use_render_resolution(True,device().get_render_resolution())
shootDirection='left'
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
sk = ['7001020', '7002020', '7003020', '7004020', '7005020', '7006020', '7007020', '7008020', '7009020', '7010020', '7101020']
login(deviceId)
del_skills()
for i in sk:
    addResource(i, '1', '1')
de_skill(deviceId, random.sample(SkillsList, 3))
home()
start_app("com.habby.punball")

for i in range(100):
    StartButton=poco("Button_Play")
    if StartButton.exists():
        print('Battle Start!')
        sleep(0.5)
        StartButton.click()
        sleep(3)
    
    skilltime = 0
    useSkill = False
    while True:
        #Check Skill#
        if poco("ChooseSkillUIPanel(Clone)").exists():
            print('Choose Skill!')
            sleep(2)
            poco("Item0").click()
            sleep(3)

        if not useSkill and skilltime >= 70:
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
            
        #Check Battle Result#
        if poco("GameOverUIPanel(Clone)").exists():
            print('Battle End!')
            sleep(5)
            poco("Down").click()
            sleep(5)
            poco("Down").click()
            sleep(5)
            break

        #Shoot#    
        else:        
            if shootDirection=='left':
                poco.long_click([0.1,0.7],duration=1)
                sleep(3)
                shootDirection='right'
            elif shootDirection=='right':
                poco.long_click([0.8,0.7],duration=1)
                sleep(3)
                shootDirection='left'
            skilltime += 1
            print("skilltime  ", skilltime)
            
    if poco("ChapterUnlockUIPanel(Clone)").exists():
        sleep(2)
        poco("Button_2").click()
        sleep(2)

        
    if poco("PiggyPurchasePanel").exists():
        sleep(2)
        poco("root").offspring("PiggyRoot").child("ButtonClose").child("ButtonClose").click()
        sleep(2)
        
    #Check Gift#
    if poco("LimitGiftPackagePanel").exists():
        sleep(2)
        print('Break Ice Gift pushed!')
        StartButton.click()
        sleep(1)
    
    home()
    de_skill(deviceId, random.sample(SkillsList, 3))
    start_app("com.habby.punball")
    sleep(2)
    

        
    
    