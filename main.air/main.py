# -*- encoding=utf8 -*-
__author__ = "zengf"

from airtest.core.api import *

auto_setup(__file__)

touch(Template(r"tpl1649233880124.png", record_pos=(0.001, 0.528), resolution=(1080, 1920)))
while not exists(Template(r"tpl1649234008740.png", record_pos=(-0.184, -0.348), resolution=(1080, 1920)))

touch(Template(r"tpl1649233947470.png", record_pos=(-0.311, 0.065), resolution=(1080, 1920)))
