from make_sql_connection import MakeSqlConnection
from database_work import DatabaseWork

database = 'TestDb1'
username = 'sa'
password = 'testpassword'
table_name = 'dbo.Store'

# make_connection = MakeSqlConnection(database, table_name, username, password)

command = (
   "INSERT INTO " + table_name + "(store_id, store_name, store_address, store_sell) "
   "VALUES (?, ?, ?, ?)"
)
data = (6632, "Mohsen", "Sattarkhan", 12365)

# make_connection.execution_command(command=command, params=data, commit=True)

dbwork = DatabaseWork(database, table_name, username, password)
# print(dbwork.columns())
# print(dbwork.number_of_records())
# print(dbwork.random_record())
# command_str = dbwork.columns_to_str()
# print(command_str)
record = dbwork.fetch_random_record()

print(record)