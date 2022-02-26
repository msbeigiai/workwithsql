import pyodbc

class MakeSqlConnection:
    def __init__(self, database_name, table_name, username, password, server='tcp:localhost,1433'):
        self.command = None
        self.cnxn = None
        self.cursor = None
        self.database_name = database_name
        self.table_name = table_name
        self.username = username
        self.password = password
        self.server = server
        self.check = self.__check_connection()
        if self.check:
            print('CONNECTION ESTABLISHED')

    def __make_connection(self):
        self.cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database_name + ';UID=' + self.username + ';PWD=' + self.password
        )

    def __execution(self):
        self.__make_connection()
        self.cursor = self.cnxn.cursor()

    def execution_command(self, command, params=None, commit=False, command_type=None):
        self.command = command
        if params and commit:
            self.cursor.execute(self.command, params)
            self.cnxn.commit()
            print("Commitment Done!")
        else:
            self.cursor.execute(self.command)
        if not params and commit:
            self.cnxn.commit()

        if command_type == 'select':
            value = self.cursor.fetchone()
            return value[0]

    def __check_connection(self):
        self.__execution()

        if self.cursor:
            return True
        else:
            return False

