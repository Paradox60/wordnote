from datetime import datetime
import datetime as date
from wordnote.SqLt.db_base import *
from wordnote.wins.library import *


def now_time():
    current_datetime = datetime.now()

    moment1 = date.datetime(1, 1, 1, 0, 0, 0)
    moment2 = date.datetime(
        current_datetime.year,
        current_datetime.month,
        current_datetime.day,
        current_datetime.hour,
        current_datetime.minute,
        current_datetime.second
    )
    delta = moment2 - moment1

    delta_s = delta.total_seconds()
    delta_s = int(delta_s)
    return delta_s


def create_library_card():
    db = Create_cursor()
    db.Create_table()
    cards_value = db.Number_of_elements()
    all_data = db.Data_list()
    card = []
    for i in range(0, cards_value):
        card.append(Library_word_card(all_data[0][i], all_data[1][i], all_data[2][i], all_data[3][i]))
    db.Close_database()
    return card


def delete_row(number):
    db = Create_cursor()
    db.Create_table()
    db.Delete_Record(number)
    db.Close_database()


def create_new_window_with_data_card(self, card):
    secondary_window = toga.Window('Secondary Window', size=(400, 300))
    # Window elements
    padding = 5
    btn_style = Pack(flex=1, padding=5)
    self.input_word_label = toga.Label("Correct word", style=Pack(padding=padding))
    self.input_translate_label = toga.Label("Correct translation", style=Pack(padding=padding))
    self.input_progress_label = toga.Label("Correct progress", style=Pack(padding=padding))

    self.input_word = toga.TextInput(
        value=f"{card.word}",
        style=Pack(padding=padding),
    )
    self.input_translate = toga.TextInput(
        value=f"{card.translate}",
        style=Pack(padding=padding),
    )
    self.input_progress = toga.TextInput(
        value=f"{card.progress}",
        style=Pack(padding=padding),
    )

    btn_accept = toga.Button(
        "Accept", on_press=apply_changes(self, card), style=btn_style)
    btn_main_win = toga.Button(
        "Back", on_press=lambda widget: secondary_window.close(), style=btn_style)

    self.add_words_win = toga.Box(
        children=[
            self.input_word_label,
            self.input_word,
            self.input_translate_label,
            self.input_translate,
            self.input_progress_label,
            self.input_progress,
            btn_accept,
            btn_main_win
        ],
        style=Pack(direction=COLUMN),
    )
    secondary_window.content = self.add_words_win
    secondary_window.show()


def apply_changes(self, card):
    def handler(widget):
        db = Create_cursor()
        db.Create_table()
        db.Edit_Word_Record(self.input_word.value, card.card_id)
        db.Edit_Translation_Record(self.input_translate.value, card.card_id)
        if int(self.input_progress.value) > 100:
            self.input_progress.value = 100
        if int(self.input_progress.value) < 0:
            self.input_progress.value = 0
        db.Edit_Progress_Record(self.input_progress.value, card.card_id)
        db.Close_database()
        self.library(self)

    return handler


def apply_value(self):
    db = Create_cursor()
    db.Create_table()
    db.Print_data()

    print(self.input_word.value)
    print(self.input_translate.value)

    new_w = self.input_word.value
    tran_w = self.input_translate.value
    prog = 5
    time = now_time()
    word = {'New_word': new_w, 'Translation': tran_w, 'Progress': prog, 'Time': time}
    db.Write_new_word(word)
    self.input_word.value = ""
    self.input_translate.value = ""
    db.Close_database()
