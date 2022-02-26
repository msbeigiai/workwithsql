from make_sql_connection import MakeSqlConnection


database = 'MicrosoftDynamicsAX'
username = 'sa'
password = 'testpassword'
table_name = 'dbo.RETAILTRANSACTIONTABLE'

make_connection = MakeSqlConnection(database, 'dbo.RETAILTRANSACTIONTABLE', username, password)
