import toga
from toga.constants import CENTER, COLUMN, HIDDEN, ROW, VISIBLE, RIGHT
from toga.style import Pack

def test_win(self,cards):
    self.cards = cards
    self.word_id = toga.Label(f"                   [Ghbdrn] :", style=Pack(padding=5, font_size=30))

    btn_style = Pack(flex=1, padding=5)
    self.btn_answer1 = toga.Button(
        "",  style=btn_style)
    self.btn_answer2 = toga.Button(
        "",  style=btn_style)
    self.btn_answer3 = toga.Button(
        "", style=btn_style)
    self.btn_answer4 = toga.Button(
        "", style=btn_style)

    self.btn_back = toga.Button(
        "Back", style=btn_style)
    self.btn_forward = toga.Button(
        "Forward", style=btn_style)
    self.btn_main_btn = toga.Button(
        "Stop test",on_press=self.main_win, style=btn_style)

    self.test_label = toga.Box(
                children=[
                        self.word_id,
                     ],
                     style=Pack(direction=COLUMN, alignment=CENTER),
                 )

    self.test_buttons1_2 = toga.Box(
        children=[
            self.btn_answer1,
            self.btn_answer2,
        ],
        style=Pack(direction=ROW, alignment=CENTER),
    )
    self.test_buttons3_4 = toga.Box(
        children=[
            self.btn_answer3,
            self.btn_answer4,
        ],
        style=Pack(direction=ROW, alignment=CENTER),
    )

    self.test_navigation_btn = toga.Box(
        children=[
            self.btn_back,
            self.btn_forward,
        ],
        style=Pack(direction=ROW, alignment=CENTER, padding=35),
    )

    self.test_main_btn = toga.Box(
        children=[
            self.btn_main_btn,
        ],
        style=Pack(direction=ROW, alignment=CENTER, padding=0),
    )

    self.test_win = toga.Box(
        children=[
            self.test_label,
            self.test_buttons1_2,
            self.test_buttons3_4,
            self.test_navigation_btn,
            self.test_main_btn,
        ],
        style=Pack(direction=COLUMN, alignment=CENTER),
    )

    return self.test_win