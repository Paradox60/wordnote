from wordnote.wins.main import *
from wordnote.wins.test import *
from wordnote.wins.html import *
from functions.Foo import *
from functions.test_func import *
import toga
import os

html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 50px;
            }

            .button {
                background-color: #3498db;
                color: #ffffff;
                padding: 10px 20px;
                font-size: 16px;
                cursor: pointer;
                border: none;
            }

            .button:hover {
                background-color: #2980b9;
            }
        </style>
        <script>
            function updateButtonStyle() {
                var button = document.getElementById('myButton');
                button.classList.add('button');
            }
        </script>
    </head>
    <body>
        <button id="myButton" onclick="updateButtonStyle()">Click me</button>
    </body>
    </html>
    """



class WordNote(toga.App):
    # Button callback functions
    def main_win(self, widget):
        self.main_window.content = Main(self)

    def add_word(self, widget):
        self.main_window.content = add_words(self)

    def test(self, widget):
        cards = create_library_card()
        test_list = testing_list(self,cards)
        self.main_window.content = test_win(self, test_list)

    def library(self, widget):
        cards = create_library_card()
        self.main_window.content = show_cards(self, cards)

    def html(self, widget):
        webview = toga.WebView(url="https://beeware.org")
        self.main_window.content = webview


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
