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
        if self.cnxn is None:
            raise ValueError(f"Connection for {self.database_name} is not established.")

    def __execution(self):
        self.__make_connection()
        self.cursor = self.cnxn.cursor()
        if self.cursor is None:
            raise ValueError(f"Cursor is None")

    def execution_command(self, command, params=None, commit=False, command_type=None):
        self.command = command
        if params and commit:
            self.cursor.execute(self.command, params)
            self.cnxn.commit()
            print("Commitment Done!")
            commitment = False
            if self.cnxn.commit():
                commitment = True
            return commitment
        else:
            self.cursor.execute(self.command)
        if not params and commit:
            self.cnxn.commit()

        if command_type == 'select':
            value = self.cursor.fetchone()
            # value = [x[0] for x in self.cursor.fetchall()]
            if value is None:
                raise ValueError(f"Vale {self.table_name} is not exist.")
            return value

    def __check_connection(self):
        self.__execution()

        if self.cursor:
            return True
        else:
            return False

