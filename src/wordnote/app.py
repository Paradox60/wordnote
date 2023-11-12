import asyncio
from datetime import datetime

import toga
from toga.constants import COLUMN
from toga.style import Pack


class WordNote(toga.App):
    # Button callback functions
    def do_next_content(self, widget):
        self.main_window.content = self.next_box

    def do_prev_content(self, widget):
        self.main_window.content = self.main_scroller

    def exit_handler(self, app, **kwargs):
        self.close_count += 1
        if self.close_count % 2 == 1:
            self.main_window.info_dialog("Can't close app", "Try that again")
            return False
        return True

    def close_handler(self, window, **kwargs):
        self.close_count += 1
        if self.close_count % 2 == 1:
            self.main_window.info_dialog("Can't close window", "Try that again")
            return False
        return True

    def new(self):
        print('somthing and somthing')

    def startup(self):
        self.close_count = 0

        # Set up main window
        self.main_window = toga.MainWindow()
        self.on_exit = self.exit_handler

        # Buttons
        btn_style = Pack(flex=1, padding=5)

        btn_change_content = toga.Button(
            "Change content", on_press=self.do_next_content, style=btn_style
        )

        self.inner_box = toga.Box(
            children=[
                btn_change_content
            ],
            style=Pack(direction=COLUMN),
        )
        self.main_scroller = toga.ScrollContainer(
            horizontal=False,
            vertical=True,
            style=Pack(flex=1),
        )
        self.main_scroller.content = self.inner_box

        btn_change_back = toga.Button(
            "Go back", on_press=self.do_prev_content, style=btn_style
        )
        self.next_box = toga.Box(
            children=[btn_change_back], style=Pack(direction=COLUMN)
        )

        restore_command = toga.Command(
            self.do_prev_content,
            text="Restore content",
            tooltip="Restore main window content",
        )

        self.commands.add(restore_command)
        self.main_window.toolbar.add(restore_command)

        # Add the content on the main window
        self.main_window.content = self.main_scroller

        # Show the main window
        self.main_window.show()


def main():
    return WordNote()
