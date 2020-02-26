import npyscreen

class MainForm(npyscreen.Form):
    def create(self):
        self.add(npyscreen.TitleText, name='Text:', value='hello world!')

    def afterEditing(self):
        self.parentApp.setNextForm(None)

class MyTestApp(npyscreen.NPSAppManaged):
    def onStart(self):
        self.registerForm("MAIN", MainForm())

if __name__ == '__main__':
    TA = MyTestApp()
    TA.run()
