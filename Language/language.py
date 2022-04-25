# -*- coding: utf-8 -*-
# @Time : 2022/3/28 11:46
# @Author : zengf
# @Email : 944458157@qq.com
# @File : language.py
# @Project : Language

import xlrd
import wx
import sys
import csv


class Language():
    def __init__(self, oldpath, newpath):
        self.oldpath = oldpath
        self.newpath = newpath
        self.old = None
        self.new = None
        self.country = []
        self.newids = []
        self.add = []

    def read_file(self):
        old = xlrd.open_workbook(self.oldpath)
        new = xlrd.open_workbook(self.newpath)
        self.old = old.sheet_by_name('Language')
        self.new = new.sheet_by_name('Language')
        self.country = self.new.row_values(2, start_colx=3)
        olddic = {}
        newdic = {}
        oldids = self.old.col_values(1)
        self.newids = self.new.col_values(1)
        oldtip = self.old.col_values(3)
        newtip = self.new.col_values(3)
        for i in range(len(oldids)):
            olddic[oldids[i]] = oldtip[i]
        for j in range(len(self.newids)):
            newdic[self.newids[j]] = newtip[j]

        lose = list(set(oldids).difference(set(self.newids)))
        # 检查新版本的language对比上个版本有没有缺失
        if lose != []:
            print("新版本丢失的多语言：{0}".format(lose) + "\n")
        else:
            print("*****新版本没有丢失多语言*****\n")
        temp = list(set(oldids) - set(lose))
        self.add = list(set(self.newids).difference(set(oldids)))
        ch = 0
        for l in temp:
            if olddic[l] != newdic[l]:
                ch += 1
                self.add.append(l)

        print("*****新版本修改了{0}".format(ch)+"条多语言*****")
        for i in self.add[-ch:]:
            print(olddic[i])
        print()
        print("*****新版本新增了{0}".format(len(self.add)-ch)+"条多语言*****\n")

    def check_country_null(self):
        csvFile2 = open('LanguageDiff.csv', 'w', newline='', encoding='utf-8')  # 设置newline，否则两行之间会空一行
        # csvFile2.truncate()
        writer = csv.writer(csvFile2)
        writer.writerow(['多语言', '亚洲最长语言', '亚洲最长', '其他最长语言', '其他最长'])

        for i in range(len(self.add)):
            ind = self.newids.index(self.add[i])
            countrys = self.new.row_values(ind, start_colx=3)
            asia = countrys[2:4] + countrys[0:1] + countrys[8:9]
            other = countrys[4:8] + countrys[1:2] + countrys[9:]
            # 检查新增的多语言有哪些没有配置全
            if '' in countrys:
                writer.writerow([countrys[0], '多语言配置不全!!!!!'])
            else:
                asiaLongest = max(asia, key=len, default='')
                otherLongest = max(other, key=len, default='')
                asial = self.country[countrys.index(asiaLongest)]
                otherl = self.country[countrys.index(otherLongest)]
                writer.writerow([countrys[0], asial, asiaLongest, otherl, otherLongest])

        csvFile2.close()


class RedirectText(object):
    def __init__(self, aWxTextCtrl):
        self.out = aWxTextCtrl

    def write(self, string):
        self.out.WriteText(string)


class MyApp(wx.App):
    def OnInit(self):
        mm = wx.DisplaySize()
        self.frame = wx.Frame(parent=None, title="多语言辅助工具", size=(mm[0], mm[1]))
        panel = wx.Panel(self.frame, -1)
        self.label1 = wx.StaticText(panel, -1, "旧版本language.xls", pos=(10, 10))
        self.text1 = wx.TextCtrl(panel, -1, pos=(150, 10), size=(250, 20))
        self.choose1 = wx.Button(panel, -1, '选择文件', pos=(450, 10))
        self.label2 = wx.StaticText(panel, -1, "新版本language.xls", pos=(10, 60))
        self.text2 = wx.TextCtrl(panel, -1, pos=(150, 60), size=(250, 20))
        self.choose2 = wx.Button(panel, -1, '选择文件', pos=(450, 60))
        self.log = wx.TextCtrl(panel, wx.ID_ANY, pos=(20, 200), size=(1500, 700),
                          style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL)
        self.button = wx.Button(panel, -1, '检查', pos=(80, 110))
        self.cl = wx.Button(panel, -1, '清空', pos=(250, 110))

        # 按钮绑定事件
        self.Bind(wx.EVT_BUTTON, self.check, self.button)
        self.Bind(wx.EVT_BUTTON, self.clear, self.cl)
        self.Bind(wx.EVT_BUTTON, self.chooseOldFile, self.choose1)
        self.Bind(wx.EVT_BUTTON, self.chooseNewFile, self.choose2)

        # redirect text here
        redir = RedirectText(self.log)
        sys.stdout = redir

        self.frame.Show()
        return True

    def chooseOldFile(self, event):
        dlg = wx.FileDialog(self.frame, u"选择文件夹", style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            self.text1.SetValue(dlg.GetPath())
        dlg.Destroy()

    def chooseNewFile(self, event):
        dlg = wx.FileDialog(self.frame, u"选择文件夹", style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            self.text2.SetValue(dlg.GetPath())
        dlg.Destroy()

    def check(self, event):
        oldfile = self.text1.GetValue()
        newfile = self.text2.GetValue()
        lan = Language(oldfile, newfile)
        lan.read_file()
        lan.check_country_null()
        print('*****文件写入完毕*****\n')

    def clear(self, event):
        self.log.Clear()


if __name__ == '__main__':
    app = MyApp()  # 启动
    app.MainLoop()  # 进入消息循环