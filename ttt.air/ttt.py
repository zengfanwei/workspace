# -*- encoding=utf8 -*-
__author__ = "zengf"

from airtest.core.api import *
import sys

auto_setup(__file__)



from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# home()
# start_app("com.habby.punball")
# width, height = device().get_current_resolution()
# touch(v=(0.5*width,0.37*height))
# text("2000000")
text("")
text("333333")
# poco("android.widget.EditText").set_text("1111")
