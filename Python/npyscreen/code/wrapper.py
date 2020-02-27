import npyscreen

# Notes:
# 1. npyscreen.wrapper_basin(func) -> call function for you.
# 2. use npyscreen.Form() to define a form, and use F.add(widget, ...) to add
# widgets on it.
# 3. use F.edit() to allow display and editing


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


def my_func(*args):
    F = MainForm(name='New Employee')
    F.edit()
    return ('create record for ' + F.name.value, (F.name.value,
                                                  F.department.get_selected_objects(), F.date.value))


if __name__ == '__main__':
    result = npyscreen.wrapper_basic(my_func)
    print(result[0])
    print(result[1])
