import pyodbc

class MakeSqlConnection:
    def __init__(self, database_name, table_name, username, password, server='tcp:localhost,1433'):
        self.command = None
        self.database_name = database_name
        self.table_name = table_name
        self.username = username
        self.password = password
        self.server = server
        self.check = self.__check_connection()
        if self.check:
            print('CONNECTION ESTABLISHED')

    def __make_connection(self):
        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database_name + ';UID=' + self.username + ';PWD=' + self.password
        )
        return cnxn

    def __execution(self):
        cnxn = self.__make_connection()
        cursor = cnxn.cursor()
        return cursor

    def execution_command(self, command, commit=False):
        self.command = command
        cursor = self.__execution()
        cursor.execute(self.command)
        if commit:
            cursor.commit()

        value = cursor.fetchone()
        return value[0]

    def __check_connection(self):
        cursor = self.__execution()

        if cursor:
            return True
        else:
            return False

