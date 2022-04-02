# -*- coding: utf-8 -*-
# @Path : C:\Users\zengf\AppData\Local\Programs\Python\Python39
# @Time : 2022/4/1 14:41
# @Author : zengf
# @Email : 944458157@qq.com
# @File : addRes.py
# @Project : workspace

import requests

Headers = {
  'Cookie': 'connect.sid=s%3AVte8CShCo4eHXNmxI9p0Ai4r-yhcinqR.fzOHOUsjTTBG2wa8AeIdttifi1%2FshhPRhlAoFq1Huow'
}
SignInUrl = "https://wiki-punball.habby.com/login?serverIdx=0&userId=9999999"
ChangeUrl = "https://wiki-punball.habby.com/addResource?serverIdx=0&resType=xxx&resNum=999&itemId=1010001&otherData=999"
DoType = {"coin": "1", "diamonds": "2", "energy": "30", "level": "19", "exp": "25", "mask": "13", "level_id": "4",
          "level_length": "29", "last_login": "33", "login_days": "75", "money": "88", "big_chest": "34",
          "small_chest": "39", "reset_talent": "41", "small_talent": "72", "big_talent": "73", "reset_dailyshop": "36",
          "reset_share": "74", "dailyshop_refresh": "84", "reset_level_chest": "38", "reset_ad": "52",
          "buy_energy_time": "71", "reset_energy_buy": "76", "clear_equipment": "59", "clear_scroll": "80"}


class UserData:
    def __init__(self, gameuid):
        self.gameuid = str(gameuid)

    def _request(self, *args, **kwargs):
        res = requests.request(*args, **kwargs)
        return res

    def signin(self):
        url = SignInUrl.replace("9999999", self.gameuid)
        print(url)
        res = self._request("GET", url, data="", headers=Headers)
        resdata = res.json()
        if resdata["code"] != 0:
            raise (Exception("登录弹球后台工具失败！"))
        return resdata

    def change_data(self, module, num):  # 通用修改数据的方法，不包括发道具、重置分享领取记录、
        url = ChangeUrl.replace("xxx", DoType[module]).replace("999", str(num))
        res = self._request("GET", url, data="", headers=Headers)
        resdata = res.json()
        if resdata["code"] != 0:
            raise (Exception("修改账号数据失败！"))
        return res

    def add_prop(self, num, itemid, level):  # 添加道具
        url = "https://wiki-punball.habby.com/addResource?serverIdx=0&resType=3&resNum={0}&itemId={1}&otherData={2}".format(num, itemid, level)
        res = self._request("GET", url, data="", headers=Headers)
        resdata = res.json()
        Headers["Cookie"] = str(res.request.headers["Cookie"])
        if resdata["code"] != 0:
            raise (Exception("给账号添加道具失败！"))
        return res

    def delete_equipment(self):  # 删除装备
        url = "https://wiki-punball.habby.com/addResource?serverIdx=0&resType=59&resNum=1&itemId=1020001&otherData=1"
        res = self._request("GET", url, data="", headers=Headers)
        resdata = res.json()
        if resdata["code"] != 0:
            raise (Exception("删除账号装备失败！"))
        return res

    def delete_account(self):  # 删除账号
        url = "https://wiki-punball.habby.com/addResource?serverIdx=0&resType=22&resNum=1&itemId=1040031&otherData=1"
        res = self._request("GET", url, data="", headers=Headers)
        resdata = res.json()
        if resdata["code"] != 0:
            raise (Exception("删除账号失败！"))
        return res


if __name__ == '__main__':
    equiplevel = '200'
    petlevel = '100'
    userid = [90005402]
    equipid = ['3020103']
    for i in equipid:
        user = UserData(i)
        # user.delete_equipment()
        # print(user.signin())
        user.add_prop('1', '3020103', equiplevel)
