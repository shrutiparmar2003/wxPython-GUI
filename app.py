import wx

# app=wx.App(False)
# frame=wx.Frame(None,wx.ID_ANY,"Hello wxPython",size=(500,400))
# panel=wx.Panel(frame,wx.ID_ANY)
# text=wx.StaticText(panel,label="Hello Shruti! Welcome to wxPython",pos=(60,40))
# frame.Show()
# app.MainLoop()

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Greeting App", size=(500, 400))
        panel=wx.Panel(self)

        self.input_box=wx.TextCtrl(panel,pos=(20,30),size=(500,50))
        button=wx.Button(panel,label="Say hello")
        self.output_label=wx.StaticText(panel,label="",pos=(20,80))

        sizer=wx.BoxSizer(wx.VERTICAL)
        sizer.Add(wx.StaticText(panel, label="What's your name?"),0,  wx.ALL, 5)
        sizer.Add(self.input_box, 0, wx.ALL | wx.EXPAND, 5)
        sizer.Add(button, 0, wx.ALL | wx.CENTER, 5)
        sizer.Add(self.output_label, 0, wx.ALL | wx.CENTER, 5)

        panel.SetSizer(sizer)

        # Bind button click event
        button.Bind(wx.EVT_BUTTON, self.say_hello)

    def say_hello(self, event):
        name = self.input_box.GetValue()
        self.output_label.SetLabel(f"Hello, {name}! 😊")


# Run the app
app = wx.App(False)
frame = MyFrame()
frame.Show()
app.MainLoop()
