from wordnote.wins.add_words import *

def Main(self):

    btn_style = Pack(flex=1, padding=5)
    btn_add_word_win = toga.Button(
        "Add_word", on_press=self.add_word, style=btn_style
    )
    btn_test_win = toga.Button(
        "Test", on_press=self.test, style=btn_style
    )
    btn_library_win = toga.Button(
        "Library", on_press=self.library, style=btn_style
    )

    self.inner_box = toga.Box(
        children=[
            btn_add_word_win,
            btn_test_win,
            btn_library_win,
        ],
        style=Pack(direction=COLUMN),
    )


    return self.inner_box