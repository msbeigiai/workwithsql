from make_sql_connection import MakeSqlConnection


database = 'TestDb1'
username = 'sa'
password = 'testpassword'
table_name = 'dbo.Store'

make_connection = MakeSqlConnection(database, table_name, username, password)

command = (
   "INSERT INTO " + table_name + "(store_id, store_name, store_address, store_sell) "
   "VALUES (?, ?, ?, ?)"
)
data = (6632, "Mohsen", "Sattarkhan", 12365)

make_connection.execution_command(command=command, params=data, commit=True)

