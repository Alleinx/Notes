import npyscreen


def func(*args):
    F = npyscreen.Form(name='Main Form')
    y, x = F.useable_space()

    first_box = F.add(
        npyscreen.BoxTitle,
        name='first box',
        values=['1', '2'],
        scroll_exit=True,
        max_height=5,
        max_width=(
            x//2 - 5))
    # Cancel off the automovement of cursor on x direction.

    second_box = F.add(
        npyscreen.BoxTitle,
        name='second box',
        values=['4', '5'],
        max_height=5,
        scroll_exit=True,
        max_width=(
            x//2 - 5),
        relx=x//2,
        rely=first_box.rely)

    F.edit()


if __name__ == '__main__':
    npyscreen.wrapper_basic(func)
