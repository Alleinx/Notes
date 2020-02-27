import npyscreen

# Use a wrapper:


def my_functions(*args):
    # define the form:
    F = npyscreen.Form(name='function wrapper')

    # add a widget onto it
    # will store iput value.
    text_wid = F.add(npyscreen.TitleText, name='First Widget')

    # Display the window, and allow user to edit the content
    F.edit()
    # return the value input
    return text_wid.value


if __name__ == '__main__':
    # use function wrapper
    print(npyscreen.wrapper_basic(my_functions))
