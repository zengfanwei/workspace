# -*- encoding=utf8 -*-
__author__ = "stars"

from airtest.core.api import *

auto_setup(__file__)

width, height = device().get_current_resolution()
Looptime=20


for i in range(Looptime):
    #主界面#
    if exists(Template(r"tpl1647940523463.png", record_pos=(0.003, 0.21), resolution=(1080, 2280))):
        print('select boss')
        touch(v=(0.3*width,0.534*height))
        sleep(1)
        touch(Template(r"tpl1647940054175.png", record_pos=(-0.01, 0.235), resolution=(1080, 2280)))
        sleep(6)

    #选择技能#    
    if exists(Template(r"tpl1647940143074.png", record_pos=(0.001, -0.446), resolution=(1080, 2280))):
        touch(v=(0.2*width,0.55*height))
        sleep(5)


    #开始战斗#
    while exists(Template(r"tpl1647940281869.png", record_pos=(0.001, -0.837), resolution=(1080, 2280))):
         swipe(v1=(0.11*width,0.7*height),v2=(0.11*width,0.71*height))
         sleep(5)

    #结算#
    if exists(Template(r"tpl1647940851729.png", record_pos=(-0.007, 0.026), resolution=(1080, 2280))):
        touch(v=(0.5*width,0.9*height))
        sleep(5)
        touch(v=(0.5*width,0.9*height))

    if exists(Template(r"tpl1647941086467.png", record_pos=(-0.005, -0.034), resolution=(1080, 2280))):
        touch(Template(r"tpl1647941097478.png", record_pos=(-0.367, 0.79), resolution=(1080, 2280)))
        sleep(2)



