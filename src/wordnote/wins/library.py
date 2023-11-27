import toga
from toga.constants import COLUMN
from toga.style import Pack

class Library_word_card:
    def __init__(self, card_id):
        self.card_id = card_id

    def __str__(self):
        return f"I'm a card with id {self.card_id}"
    def fill_up_card(self):
        self.input_word_label = toga.Label("Enter new word", style=Pack(padding=Padding))
        self.input_translate_label = toga.Label("Enter translation", style=Pack(padding=Padding))

class Library_win:
    def __init__(self, cards: Library_word_card):
        self.container = []
        self.container.extend(cards)

    def Show_cards(self):
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

