from make_sql_connection import MakeSqlConnection
import pandas as pd
from random import randint


class DatabaseWork:
    def __init__(self, database_name, table_name, username, password, server='tcp:localhost,1433'):
        mksqlconn = MakeSqlConnection(database_name, table_name, username, password)
        command = 'select * from ' + table_name

        self.df = pd.read_sql(command, mksqlconn.cnxn)

    def columns(self):
        return self.df.columns

    def number_of_records(self):
        return len(self.df.iloc[:])

    def random_record(self):
        rnd_record = randint(0, self.number_of_records())
        return rnd_record

    def columns_to_str(self):
        command_str = ''
        m = len(self.df.columns)
        tag = ', '
        for i in range(m):
            if i == m - 1:
                tag = ''
            command_str += self.df.columns[i] + tag
        return command_str

    def fetch_random_record(self):
        rnd_record = self.random_record()
        record = self.df.iloc[rnd_record, :]
        return record.values

