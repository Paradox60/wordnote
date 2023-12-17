import toga
from toga.constants import COLUMN
from toga.style import Pack

def html_view(self):
    self.html_content = """
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



    return self.html_content