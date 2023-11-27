import sqlite3

class Create_cursor():
    def __init__(self):
    #Open Database
        self.file_name = 'project_db'

        try:
            self.conn = sqlite3.connect(self.file_name)
        except Error as e:
            print(e)

        # Create a cursor to allow to execute SQL commands
        self.cursor = self.conn.cursor()

    def Create_table(self):

        # Create a SQL Table
        sql_command = '''
                         CREATE TABLE IF NOT EXISTS words(
                             Id INTEGER PRIMARY KEY AUTOINCREMENT, 
                             New_word TEXT, 
                             Translation TEXT,
                             Progress INTEGER, 
                             Time INTEGER
                         )'''

        self.cursor.execute(sql_command)
        print('Base with words sucsfully open')

        # Commit the changes to the database
        self.conn.commit()

    def Print_data(self):

        select_data = 'SELECT * FROM words'
        self.cursor.execute(select_data)
        rows = self.cursor.fetchall()

        for row in rows:
            print(row)

    def Write_new_word(self, word):
        # Create the sqlite database if it does not exist. If it exist, connect to it.

        insert_data = f"""
                   INSERT INTO words 
                   (New_word, Translation, Progress, Time) 
                   VALUES ( 
                       '{word['New_word']}',
                       '{word['Translation']}',
                       '{word['Progress']}',
                       '{word['Time']}'
                   )
               """
        self.cursor.execute(insert_data)
        # Commit the changes to the database
        self.conn.commit()
        print("Record new word successfully")

    def Number_of_elements(self):

        select_data = 'SELECT * FROM words'
        self.cursor.execute(select_data)
        rows = self.cursor.fetchall()
        i = 0
        for row in rows:
            i = i + 1

        # print(i)
        return i

    def Close_database(self):
        self.conn.close()