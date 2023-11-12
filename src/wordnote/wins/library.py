import toga
from toga.constants import COLUMN
from toga.style import Pack

def Library(self):

    btn_style = Pack(flex=1, padding=5)
    btn_main_win = toga.Button(
        "Back", on_press=self.main_win, style=btn_style
    )

    self.add_library_win = toga.Box(
        children=[
            btn_main_win
        ],
        style=Pack(direction=COLUMN),
    )



    return self.add_library_win