# -*- encoding=utf8 -*-
__author__ = "stars"

from airtest.core.api import *
import requests

auto_setup(__file__)

width, height = device().get_current_resolution()
Looptime=30
direction='left'

LoopNow=0
for i in range(Looptime):
    LoopNow+=1
    #主界面#
    if exists(Template(r"tpl1648782416542.png", record_pos=(0.0, 0.614), resolution=(1080, 2220))):
        print('Round '+ str(LoopNow) + ':Game Start')
        touch(Template(r"tpl1648782416542.png", record_pos=(0.0, 0.614), resolution=(1080, 2220)))
        sleep(6)
    
    #Round
    while True:
        #选择技能#    
        if exists(Template(r"tpl1648782461084.png", record_pos=(-0.002, -0.488), resolution=(1080, 2220))):
            print('Round '+ str(LoopNow) +':Select Skill')
            touch(v=(0.2*width,0.55*height))
            sleep(5)



        #结算#
        elif exists(Template(r"tpl1648783312509.png", record_pos=(-0.003, -0.011), resolution=(1080, 2220))):
            print('Round '+ str(LoopNow) +':Battle finish')
            sleep(5)
            touch(v=(0.5*width,0.98*height))
            print('Round '+ str(LoopNow) +':touch screen1')
            sleep(5)
            touch(v=(0.5*width,0.98*height))
            print('Round '+ str(LoopNow) +':touch screen2')
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
            
    if exists(Template(r"tpl1648783338121.png", record_pos=(-0.004, -0.021), resolution=(1080, 2220))):
        print('Round '+ str(LoopNow) +':Unlock new chapter')
        touch(v=(0.5*width,0.9*height))
        sleep(5)
        
    if exists(Template(r"tpl1649300074889.png", record_pos=(0.006, 0.003), resolution=(1080, 2220))):             
        touch(v=(0.5*width,0.9*height))
        sleep(3)

        
    if exists(Template(r"tpl1648798238356.png", record_pos=(0.392, -0.832), resolution=(1080, 2220))):
        touch(Template(r"tpl1648798238356.png", record_pos=(0.392, -0.832), resolution=(1080, 2220)))
        print('Round '+ str(LoopNow) +':World Boss Enter')
        sleep(3)

        if exists(Template(r"tpl1648798473262.png", record_pos=(0.001, 0.823), resolution=(1080, 2220))):
            touch(Template(r"tpl1648798473262.png", record_pos=(0.001, 0.823), resolution=(1080, 2220)))

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

        if exists(Template(r"tpl1648798752833.png", record_pos=(-0.361, 0.828), resolution=(1080, 2220))):
            touch(Template(r"tpl1648798752833.png", record_pos=(-0.361, 0.828), resolution=(1080, 2220)))
            print('(Boss)Round '+ str(LoopNow) +':Back to Menu')
            sleep(2)


