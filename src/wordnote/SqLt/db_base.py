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

    def Data_list(self):

        select_data = 'SELECT * FROM words'
        self.cursor.execute(select_data)
        rows = self.cursor.fetchall()
        all_lists = []
        word_id = []
        learning_words = []
        translated_words = []
        progress_list = []
        sec_time_list = []
        for row in rows:

            word_id.append(row[0])
            learning_words.append(row[1])
            translated_words.append(row[2])
            progress_list.append(row[3])
            sec_time_list.append(row[4])

        all_lists.append(word_id)
        all_lists.append(learning_words)
        all_lists.append(translated_words)
        all_lists.append(progress_list)
        all_lists.append(sec_time_list)

        return all_lists

    def Delete_Record(self,number):

            # Deleting single record now
            sql_update_query = """DELETE from words where id = ?"""
            self.cursor.execute(sql_update_query, (number,))
            self.conn.commit()
            print("Record deleted successfully ")


    def Edit_Word_Record(self, word, word_id):

        sql_update_query = """Update words set  New_word = ?  where id = ?"""
        data = (word, word_id)

        self.cursor.execute(sql_update_query, data)
        self.conn.commit()

    def Edit_Translation_Record(self, word, word_id):

        sql_update_query = """Update words set  Translation = ?  where id = ?"""
        data = (word, word_id)

        self.cursor.execute(sql_update_query, data)
        self.conn.commit()

    def Edit_Progress_Record(self, word, word_id):

        sql_update_query = """Update words set  Progress = ?  where id = ?"""
        data = (word, word_id)

        self.cursor.execute(sql_update_query, data)
        self.conn.commit()


    def Close_database(self):
        self.conn.close()