import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None,title="User Form",size=(600,400))
        panel=wx.Panel(self)

        name_label=wx.StaticText(panel,label="Name : ")
        self.name_input=wx.TextCtrl(panel)

        gender_label=wx.StaticText(panel,label="Gender :")
        self.radio_male=wx.RadioButton(panel, label="Male",style=wx.RB_GROUP)
        self.radio_female=wx.RadioButton(panel,label="Female")

        color_label=wx.StaticText(panel,label="Favorite Color :")
        self.color_choice=wx.ComboBox(panel,choices=["Red","Blue","Pink","Violet"])

        self.checkbox=wx.CheckBox(panel,label="I accept the terms and condtions")

        submit_btn=wx.Button(panel,label="submit")
        submit_btn.Bind(wx.EVT_BUTTON,self.on_submit)

        self.output=wx.StaticText(panel,label="")

        # Layout using BoxSizer
        sizer=wx.BoxSizer(wx.VERTICAL)
        sizer.Add(name_label,0,wx.ALL,5)
        sizer.Add(self.name_input,0,wx.ALL|wx.EXPAND,5)

        sizer.Add(gender_label,0,wx.ALL,5)
        hbox_gender=wx.BoxSizer(wx.HORIZONTAL)
        hbox_gender.Add(self.radio_male,0,wx.ALL,5)
        hbox_gender.Add(self.radio_female,0,wx.ALL,5)
        sizer.Add(hbox_gender,0,wx.ALL,0)

        sizer.Add(color_label,0,wx.ALL,5)
        sizer.Add(self.color_choice,0,wx.ALL|wx.EXPAND,5)

        sizer.Add(self.checkbox,0,wx.ALL,5)
        sizer.Add(submit_btn,0, wx.ALL | wx.CENTER, 5)
        sizer.Add(self.output, 0, wx.ALL | wx.CENTER, 5)

        panel.SetSizer(sizer)

    def on_submit(self,event):
        name=self.name_input.GetValue()
        gender="Male" if self.radio_male.GetValue() else "Female"
        color=self.color_choice.GetValue()
        accepted=self.checkbox.GetValue()

        if not name or not color or not accepted:
            self.output.setLabel("Please fill everything and accept the terms.")
            return
        self.output.SetLabel(f"Hello {name}! You are {gender} and like {color}. ✅")

app=wx.App(False)
frame=MyFrame()
frame.Show()
app.MainLoop()

