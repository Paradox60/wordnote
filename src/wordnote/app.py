
import toga
from toga.constants import COLUMN
from toga.style import Pack
#sdfgsdfgsdfgfdsgdfsg
from wordnote.wins.main import *



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
        self.main_window.content = Library(self)

    def test(self,widget):
        self.main_window.content = Library(self)

    def startup(self):

               # Set up main window
        self.main_window = toga.MainWindow()

        # Add the content on the main window
        self.main_window.content = Main(self)

        # Show the main window
        self.main_window.show()


def main():
    return WordNote()
