from wordnote.wins.main import *
from wordnote.wins.test import *
from functions.Foo import *



class WordNote(toga.App):

    # Button callback functions
    def main_win(self, widget):
        self.main_window.content = Main(self)
    def add_word(self, widget):
        self.main_window.content = Add_words(self)
    def library(self, widget):
        card = Create_library_card()
        self.main_window.content = Show_cards(self, card)
    def test(self, widget):
        card = Create_library_card()
        self.main_window.content = test_win(self, card)


    def delete_handler(self, button_id):
        async def handler(widget):
            if await self.main_window.confirm_dialog("Delete card", "A you sure?"):
                Delete_row(button_id)
                self.library(self)
            else:
                await self.main_window.info_dialog(
                        "Nothing changed", "Everything is fine"
                    )
        return handler

    def edit_card(self, card):
        def handler(widget):
            Create_new_window_with_data_card(self,card)

        return handler

    def  take_value(self, widget):
        DB = Create_cursor()
        DB.Create_table()
        DB.Print_data()

        print(self.input_word.value)
        print(self.input_translate.value)

        new_w = self.input_word.value
        tran_w = self.input_translate.value
        prog = 5
        time = Now_time()
        word = {'New_word': new_w, 'Translation': tran_w, 'Progress': prog, 'Time': time}
        DB.Write_new_word(word)
        self.input_word.value = ""
        self.input_translate.value = ""
        DB.Close_database()

    def startup(self):

        # Set up main window
        self.main_window = toga.MainWindow()

        # Add the content on the main window
        self.main_window.content = Main(self)

        # Show the main window
        self.main_window.show()


def main():
    return WordNote()
