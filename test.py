# -*- coding: utf-8 -*-
# @Path : C:\Users\zengf\AppData\Local\Programs\Python\Python39
# @Time : 2022/4/8 17:15
# @Author : zengf
# @Email : 944458157@qq.com
# @File : test.py
# @Project : workspace
#
# import random
#
# list = [1, 2, 3, 4, 5, 6]
# print(random.sample(list, 1))
import wx

class MyFrame1(wx.Frame):


    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame1.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        self.frame=wx.Frame.__init__(self, *args, **kwds)
        self.panel_1 = wx.Panel(self, -1)
        self.f3 = wx.Frame(None,-1,'Edit Tags')

        self.editTag = wx.Button(self.panel_1, -1, "Edit Tags", size=(100, 50))
        self.editTag.Bind(wx.EVT_BUTTON, self.editTags)

        self.Bind( wx.EVT_CLOSE, self.CloseAll)



        # end wxGlade

#-------------------------------------------------------------------------------
    def editTags(self, event):  # wxGlade: MyFrame.<event_handler>
        samples={
              "Face1":"(100,100)", \
              "Face2":"(50,40)", \
              "Car":"(500,230)", \
              "Wallclock":"(120,230)"

            }

        self.f3.okButton = wx.Button(self.f3, label="OK")
        self.f3.okButton.Bind(wx.EVT_BUTTON, self.onOK)
        self.f3.okButton.SetPosition((40,200))

        spacer=0

        for k, v in sorted(samples.iteritems()):

            spacer=spacer+40

        self.f3.new_TextControl = wx.TextCtrl(self.f3, -1, value=k)
        self.f3.new_TextControl.SetPosition((40,spacer))


        self.f3.Show()

   #-------------------------------------------------------------------------------
    def onOK(self, event):  # wxGlade: MyFrame.<event_handler>
        self.f3.Hide()
   #-------------------------------------------------------------------------------

    def CloseAll(self, event):
        self.DestroyChildren()  # First destroy child frames
        self.Destroy()          # Then destroy the parent frame
        self.f3.Close()
        self.Close()
   #-------------------------------------------------------------------------------

    # end of class MyFrame1
if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    frame_1 = MyFrame1(None, -1, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()