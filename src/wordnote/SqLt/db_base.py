class Create_cursor():
    def __init__(self,file_name):
    #Open Database
        self.file_name = file_name

        try:
            self.conn = sqlite3.connect(self.file_name)
        except Error as e:
            print(e)

        # Create a cursor to allow to execute SQL commands
        self.cursor = self.conn.cursor()