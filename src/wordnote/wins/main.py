import toga
from toga.constants import COLUMN
from toga.style import Pack

from wordnote.wins.add_words import *
from wordnote.wins.library import *

def Main(self):

    btn_style = Pack(flex=1, padding=5)
    btn_add_word_win = toga.Button(
        "Add_word", on_press=self.add_word, style=btn_style
    )
    btn_test_win = toga.Button(
        "Test",  style=btn_style
    )
    btn_library_win = toga.Button(
        "Library", on_press=self.library, style=btn_style
    )

    self.inner_box1 = toga.Box(
        children=[
            btn_add_word_win,
            btn_test_win,
            btn_library_win,
        ],
        style=Pack(direction=COLUMN),
    )

    self.add_words_win = Add_words(self)
    self.add_library_win = Library(self)

    return self.inner_box1