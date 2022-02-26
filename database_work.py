from make_sql_connection import MakeSqlConnection
import pandas as pd
from random import randint


class DatabaseWork:
    def __init__(self, database_name, table_name, username, password, server='tcp:localhost,1433'):
        self.mksqlconn = MakeSqlConnection(database_name, table_name, username, password)
        command = 'select * from ' + table_name
        self.table_name = table_name
        self.df = pd.read_sql(command, self.mksqlconn.cnxn)

    def __columns(self):
        return self.df.columns

    def __number_of_records(self):
        return len(self.df.iloc[:])

    def __random_record(self):
        rnd_record = randint(0, self.__number_of_records())
        return rnd_record

    def __columns_to_str(self):
        command_str = ''
        m = len(self.df.columns)
        tag = ', '
        for i in range(m):
            if i == m - 1:
                tag = ''
            command_str += self.df.columns[i] + tag
        return "(" + command_str + ")"

    def __fetch_random_record(self):
        rnd_record = self.__random_record()
        record = self.df.iloc[rnd_record, :]
        return record.values

    def __record_values(self):
        record = self.__fetch_random_record()
        new_value = tuple(i for i in record)
        return new_value

    def __make_question_values(self):
        num = len(self.__record_values())
        str_name = ''
        tag = ', '
        for i in range(num):
            if i == num - 1:
                tag = ''
            str_name += '?' + tag
        str_name = "( " + str_name + " )"
        return str_name

    def make_command(self):
        command_str = self.__columns_to_str()
        str_name = self.__make_question_values()
        command = (
                "INSERT INTO " + self.table_name + command_str +
                                              "VALUES " + str_name
        )
        data = self.__record_values()
        return command, data

    def execute(self):
        command, data = self.make_command()
        self.mksqlconn.execution_command(command=command, params=data, commit=True)