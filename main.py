from make_sql_connection import MakeSqlConnection


database = 'TestDb1'
username = 'sa'
password = 'testpassword'
table_name = 'dbo.Store'

make_connection = MakeSqlConnection(database, table_name, username, password)

command = (
   "INSERT INTO Store(store_id, store_name, store_address, store_sell) "
   "VALUES (%s, %s, %s, %s)"
)
data = (6632, "Mohsen", "Sattarkhan", 12365)
try:
    make_connection.execution_command(command, data, True)

except:
    print("Nothing")
