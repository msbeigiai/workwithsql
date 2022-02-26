import unittest
from make_sql_connection import MakeSqlConnection


class MakeSqlConnectionTest(unittest.TestCase):
    @staticmethod
    def initialize_vlue():
        database = 'MicrosoftDynamicsAX'
        username = 'sa'
        password = 'testpassword'
        table_name = 'dbo.RETAILTRANSACTIONTABLE'
        list_values = [database, username, password, table_name]
        return list_values

    def test_established_connection(self):
        list_values = self.initialize_vlue()
        make_connection = MakeSqlConnection(list_values[0], list_values[3], list_values[1], list_values[2])
        self.assertEqual(make_connection.check, True)

    def test_execution_command(self):
        list_values = self.initialize_vlue()
        make_connection = MakeSqlConnection(list_values[0], list_values[3], list_values[1], list_values[2])
        command = 'select count(*) from ' + list_values[3]
        row = make_connection.execution_command(command=command, command_type='select')
        self.assertEqual(row, 5511)

    def test_commitment(self):
        list_values = self.initialize_vlue()
        make_connection = MakeSqlConnection(list_values[0], list_values[3], list_values[1], list_values[2])
        command = (
                "INSERT INTO " + list_values[3] + "(store_id, store_name, store_address, store_sell) "
                                              "VALUES (?, ?, ?, ?)"
        )
        data = (6632, "Mohsen", "Sattarkhan", 12365)

        result = make_connection.execution_command(command, data)
        self.assertTrue(result)


unittest.main()
