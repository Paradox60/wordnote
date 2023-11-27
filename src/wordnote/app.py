
import toga

from wordnote.wins.main import *
from wordnote.SqLt.db_base import *
from functions.Foo import *



class WordNote(toga.App):

    def refresh_win(self,widget):
        Add_word(self)
        Library(self)

    # Button callback functions
    def add_word(self, widget):
        self.main_window.content = Add_words(self)

    def main_win(self, widget):
        self.main_window.content = Main(self)

    def library(self,widget):
        DB = Create_cursor()
        DB.Create_table()
        table_length = DB.Number_of_elements()
        # list_of_words =


        self.card = Library_word_card(5)
        print(self.card)
        self.main_window.content = Library_win.Show_cards(self)


    def test(self,widget):
        self.main_window.content = Library(self)

    def  take_value(self,widget):
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
