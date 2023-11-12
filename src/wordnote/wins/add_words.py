import toga
from toga.constants import COLUMN
from toga.style import Pack

def Add_words(self):
    Padding =5

    btn_style = Pack(flex=1, padding=5)
    #Window elements
    self.input_word_label = toga.Label("Enter new word", style=Pack(padding=Padding))
    self.input_translate_label = toga.Label("Enter translation", style=Pack(padding=Padding))

    self.input_word= toga.TextInput(
        placeholder="Input word",
        style=Pack(padding=Padding),
    )
    self.input_translate = toga.TextInput(
        placeholder="Input translate",
        style=Pack(padding=Padding),
    )

    btn_accept = toga.Button(
        "Accept", on_press=self.main_win, style=btn_style    )
    btn_main_win = toga.Button(
        "Back", on_press=self.main_win, style=btn_style
    )

    self.add_words_win = toga.Box(
        children=[
            self.input_word_label,
            self.input_word,
            self.input_translate_label,
            self.input_translate,
            btn_accept,
            btn_main_win
        ],
        style=Pack(direction=COLUMN),
    )



    return self.add_words_win