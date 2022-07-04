# -*- encoding=utf8 -*-
__author__ = "stars"

from airtest.core.api import *

auto_setup(__file__)

width, height = device().get_current_resolution()
Looptime=100
direction='left'

LoopNow=0
for i in range(Looptime):
    LoopNow+=1


    if exists(Template(r"tpl1649740003607.png", record_pos=(-0.001, 0.878), resolution=(1080, 2400))):
        touch(Template(r"tpl1649740003607.png", record_pos=(-0.001, 0.878), resolution=(1080, 2400)))
        print('(Boss)Round '+ str(LoopNow) +':Battle start')        
        sleep(5)
        
#     elif exists(Template(r"tpl1649740048295.png", record_pos=(-0.004, 0.895), resolution=(1080, 2340))):
#         touch(Template(r"tpl1649740003607.png", record_pos=(-0.001, 0.878), resolution=(1080, 2400)))
#         print('(Boss)Round '+ str(LoopNow) +':Battle start1')
#         sleep(5)


    #Round
    while True:
        #选择技能#    
        if exists(Template(r"tpl1648782461084.png", record_pos=(-0.002, -0.488), resolution=(1080, 2220))):
            print('(Boss)Round '+ str(LoopNow) +':Select Skill')
            touch(v=(0.2*width,0.55*height))
            sleep(5)

        #结算#
        if exists(Template(r"tpl1648798700354.png", record_pos=(-0.005, 0.014), resolution=(1080, 2220))):
            print('(Boss)Round '+ str(LoopNow) +':Battle finish')
            sleep(5)
            touch(v=(0.5*width,0.98*height))
            print('(Boss)Round '+ str(LoopNow) +':touch screen1')
            sleep(5)
            touch(v=(0.5*width,0.98*height))
            print('(Boss)Round '+ str(LoopNow) +':touch screen2')
            sleep(8)
            break

        #开始战斗#
        else:
            if direction=='left':
                print('Round '+ str(LoopNow) +':Attack Left')
                touch(v=(0.2*width,0.7*height),duration=0.5)
                direction='right'
                sleep(3)
            elif direction=='right':
                print('Round '+ str(LoopNow) +':Attack Right')
                touch(v=(0.8*width,0.7*height),duration=0.5)
                direction='left'
                sleep(3)




