# -*- encoding=utf8 -*-
__author__ = "zengf"

import random
from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()
using("add.air")
from add import login, del_skills, addResource, de_skill, SkillsList

width, height = device().get_current_resolution()
direction='left'
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
useSkill = False

for i in range(100):
    if poco("ButtonWorldBoss").exists():
        poco("ButtonWorldBoss").click()
        print('Into '+ str(i) +'WorldBoss')   
        sleep(2)
        
    if poco("DownPart").child("PlayBtn").child("PlayBtn").exists():
        poco("DownPart").child("PlayBtn").child("PlayBtn").click()
        print('(Boss)Round '+ str(i) +':Battle start') 
        sleep(6)
        
    while True:
        if poco("ChooseSkillUIPanel").exists():
            sleep(1.5)
            poco("Item0").click()
            print('(Boss)Round '+ str(i) +':Select Skill')
            
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
                
        if poco("GameOverUIPanel").exists():
            sleep(8)
            if poco("childParent").exists():
                poco("childParent").click()
                sleep(5)
            if poco("childParent").exists():
                poco("childParent").click()
                sleep(2)
            if poco("PiggyPurchasePanel").exists():
                poco("root").offspring("PiggyRoot").child("ButtonClose").child("ButtonClose").click()
            break
        #开始战斗#
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
    home()
    de_skill(deviceId, random.sample(SkillsList, 3))
    start_app("com.habby.punball")
    sleep(2)
    useSkill = False
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                