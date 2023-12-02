import toga
from toga.constants import CENTER, COLUMN, HIDDEN, ROW, VISIBLE, RIGHT
from toga.style import Pack


def Show_cards(self,cards):
    self.cards  = cards
    self.scroll_container = toga.ScrollContainer(style=Pack(flex=1))
    children = []
    for card in self.cards:
        self.Padding = 5
        self.font_size = 20
        self.word_id = toga.Label(f"[{card.card_id}] :", style=Pack(padding=self.Padding, font_size=self.font_size))
        self.word_label = toga.Label(f"[{card.word}] /", style=Pack(padding=self.Padding, font_size=self.font_size))
        self.translate_label = toga.Label(f"/ [{card.translate}]", style=Pack(padding=self.Padding, font_size=self.font_size))
        self.progress_label = toga.Label(f"Progress :{card.progress}%", style=Pack(padding=self.Padding, font_size=self.font_size))

        self.add_card_label = toga.Box(
            children=[
                    self.word_id,
                    self.word_label,
                    self.translate_label,
                    self.progress_label
                 ],
                 style=Pack(direction=ROW, alignment=RIGHT),
             )


        btn_style = Pack(flex=1, padding=5)
        self.btn_edit_card = toga.Button(
                "Edit", on_press=self.edit_card(card), style=btn_style)
        self.btn_delete_card = toga.Button(
                "Delete", on_press=self.delete_handler(card.card_id), style=btn_style)

        self.add_edit_buttons = toga.Box(
            children=[
                self.btn_edit_card,
                self.btn_delete_card
            ],
            style=Pack(direction=ROW),
        )

        self.add_card = toga.Box(
            children=[
                self.add_card_label,
                self.add_edit_buttons
            ],
            style=Pack(direction=COLUMN),
        )

        children.append(self.add_card)

    self.add_cards = toga.Box(
        children=children,
        style=Pack(direction=COLUMN),
    )

    btn_style = Pack(flex=1, padding=5)
    btn_main_win = toga.Button(
        "Back", on_press=self.main_win, style=btn_style
    )
    self.main_win_button = toga.Box(
        children=[
            btn_main_win
        ],
        style=Pack(direction=COLUMN),
    )

    self.scroll_container.content = self.add_cards

    self.add_library_win = toga.Box(
        children=[
            self.scroll_container,
            self.main_win_button,
        ],
        style=Pack(direction=COLUMN),
    )

    return self.add_library_win


class Library_word_card:
    def __init__(self, card_id, word, translate, progress, sec_time):
        self.card_id = card_id
        self.word = word
        self.translate = translate
        self.progress = progress
        self.sec_time = sec_time
    def __repr__(self):
        return f"card#{self.card_id}"


