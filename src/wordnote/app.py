from wordnote.wins.main import *
from wordnote.wins.test import *
from functions.Foo import *
from functions.test_func import *


class WordNote(toga.App):
    # Button callback functions
    def main_win(self, widget):
        self.main_window.content = Main(self)

    def add_word(self, widget):
        self.main_window.content = Add_words(self)

    def test(self, widget):
        cards = create_library_card()
        test_list = testing_list(self,cards)
        self.main_window.content = test_win(self, test_list)

    def library(self, widget):
        cards = create_library_card()
        self.main_window.content = show_cards(self, cards)

    def delete_handler(self, button_id):
        async def handler(widget):
            if await(self.main_window.confirm_dialog("Delete card", "A you sure?")):
                delete_row(button_id)
                self.library(self)
            else:
                await self.main_window.info_dialog("Nothing changed", "Everything is fine")
        return handler

    def edit_card(self, card):
        def handler(widget):
            create_new_window_with_data_card(self, card)
        return handler

    def take_value(self, widget):
        apply_value(self)

    def startup(self):

        # Set up main window
        self.main_window = toga.MainWindow()

        # Add the content on the main window
        self.main_window.content = Main(self)

        # Show the main window
        self.main_window.show()


def main():
    return WordNote()
