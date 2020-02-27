'''
Robust framework for building large applications.
If you're displaying more than 1 screen, or running an application continuously,
this is the approach you should take.
'''
import npyscreen


class MainForm(npyscreen.Form):
    '''
    Instead of using the npyscreen.Form(widget, ...)
    we can define our own Form class
    '''

    def create(self):
        '''
        The create() method will be called whenever the form is created.
        '''
        # will store input value
        self.name = self.add(npyscreen.TitleText, name='Name')
        self.department = self.add(
            npyscreen.TitleSelectOne,
            max_height=3,
            name='Department',
            values=['NLP', 'CV', 'Algorithm'],
            scroll_exit=True)
        # scroll_exit: Let the user move out of the widget by navigating
        self.date = self.add(npyscreen.TitleDateCombo, name='Date Employed')

    def afterEditing(self):
        self.parentApp.setNextForm(None)
        # To stop infinitely displaying forms.


class MyApplication(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN", MainForm, name='New Employee')
        # Application will continually display the form for you to edit, until
        # you press ^C, this is because the NPSAppManaged class continually
        # display whatever form is named by its "NEXT_ACTIVE_FORM" attribute
        # (in this case "MAIN").

        # To solve this problem, you should add setNextForm() method.


if __name__ == '__main__':
    TestApp = MyApplication().run()
